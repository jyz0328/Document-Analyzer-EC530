## upload.py
from flask import jsonify, request
from flask_restful import Resource
from flask_login import login_required
from textanalyzer import analyze_document
import pdfplumber  # 导入pdfplumber库

class FileUpload(Resource):
    @login_required
    def post(self):
        if 'document' not in request.files:
            return jsonify({"error": "No file part"})
        
        file = request.files['document']
        if file.filename == '':
            return jsonify({"error": "No selected file"})

        # 根据文件扩展名决定处理方法
        if file.filename.lower().endswith('.pdf'):
            # 处理PDF文件
            with pdfplumber.open(file) as pdf:
                text = ''
                # 遍历PDF中的每一页
                for page in pdf.pages:
                    text += page.extract_text()  # 从每一页中提取文本
        else:
            # 处理文本文件
            text = file.read().decode("utf-8")

        # 分析文本
        if text:
            analysis_result = analyze_document(text)
            return jsonify(analysis_result)
        else:
            return jsonify({"error": "Unable to extract text from file"})
