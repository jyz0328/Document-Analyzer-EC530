## if run[python3 upload_separate.py] on terminal we can return 1
## if run[python3 upload_separate.py none.txt] on terminal  we can return 2
## if run[python3 upload_separate.py sample.png] on terminal we can return 3
## if ru [python3 upload_separate.py grade.pdf] on terminal we can return 4
#seperate upload from auth.py app.py nowclient.py
import os
import pdfplumber
import threading
import queue
import textanalyzer
import sys

def process_pdf(file_path, task_queue):
    # 处理PDF文件并将结果放入队列
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    task_queue.put(text)

def process_text(file_path, task_queue):
    # 处理文本文件并将内容放入队列
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    task_queue.put(text)

def process_nlp(text, result_queue):
    # 处理文本分析并将结果放入另一个队列
    analysis_result = textanalyzer.analyze_document(text)
    result_queue.put(analysis_result)

def main(file_path):
    # 检查是否提供了文件路径
    if not file_path:
        print("error 1:  do not enter a document for uploaded")
        return 1

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print("error 2: cannot find this document, document does not exist")
        return 2
    
    #但是还是想把没有上传文件的情况加上怎么弄
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    if file_path.lower().endswith('.pdf'):
        threading.Thread(target=process_pdf, args=(file_path, task_queue)).start()
    elif file_path.lower().endswith('.txt'):
        threading.Thread(target=process_text, args=(file_path, task_queue)).start()
    else:
        print("error 3: upload a Unsupported file type")
        return 3

    text = task_queue.get()

    threading.Thread(target=process_nlp, args=(text, result_queue)).start()
    analysis_result = result_queue.get()

    filename = os.path.basename(file_path)
    textanalyzer.save_analysis_results(analysis_result, filename)

    print("situation 4:Successfully processed the document.")
    return 4

if __name__ == '__main__':
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    main(file_path)
