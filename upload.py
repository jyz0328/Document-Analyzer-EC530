## upload.py
from flask import jsonify, request
from flask_restful import Resource
from flask_login import login_required
import pdfplumber
import threading
import queue
from werkzeug.utils import secure_filename
import os
from textanalyzer import analyze_document

def process_pdf(file_path, task_queue):
    # 处理PDF文件并将结果放入队列
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    task_queue.put(text)

def process_nlp(text, result_queue):
    # 处理文本分析并将结果放入另一个队列
    analysis_result = analyze_document(text)
    result_queue.put(analysis_result)

class FileUpload(Resource):
    @login_required
    def post(self):
        if 'document' not in request.files:
            return jsonify({"error": "No file part"})
        
        file = request.files['document']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        
        # 确保文件名的安全性
        filename = secure_filename(file.filename)
        file_path = os.path.join('/tmp', filename)
        file.save(file_path)

        # 为PDF处理和NLP分析创建队列
        task_queue = queue.Queue()
        result_queue = queue.Queue()

        if filename.lower().endswith('.pdf'):
            # 启动一个线程来处理PDF
            threading.Thread(target=process_pdf, args=(file_path, task_queue)).start()
            text = task_queue.get()  # 等待PDF处理完成
            
            #  启动另一个线程进行NLP分析
            threading.Thread(target=process_nlp, args=(text, result_queue)).start()
            analysis_result = result_queue.get()  # 等待NLP分析完成
            
            # 清理操作：删除临时文件
            os.remove(file_path)
            
            return jsonify(analysis_result)
        else:
            # 清理操作：删除临时文件
            os.remove(file_path)
            return jsonify({"error": "Unsupported file type"})
