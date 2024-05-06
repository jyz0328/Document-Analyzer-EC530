#if [python3 textanalyzer_seperate.py] , we can get return 1
#if [python3 textanalyzer_seperate.py none.txt], we can get return 2
#if [python3 textanalyzer_seperate.py grade.pdf], we can get return 3
#if [python3 textanalyzer_seperate.py test.txt], we can get return 4
#这个代码是在单独运行textanalyzer并汇报错误或者正确情况
#报错都和return都在[analyze_doucment]进行，而不是在mianpart进行，并且每个情况保存为return 数字
#如果，根本没有输入文件，print("error:do not enter a document for text analyze“）输出并让[analyze_doucment]return1
#如果，输入根本不存在的文件，print("error:document does not exist“）输出并让[analyze_doucment]return2
#如果，输入存在的文件但是不是txt，print("error:document exists but this module only accept txt. we use upload.py to transfer document into txt and then put it into textanalyzer.py “）输出并让[analyze_doucment]return3
#如果，输入存在的txt，print("successfully“）输出并让return4
#这个代码叫textanalyzer_seperate.py，现在创建test_textanalyzer.py，通过[pytest test_part.py]和def test，assert  == 1/2/3/4的方式构建 怎么弄
import spacy
from textblob import TextBlob
import sys
import os

nlp = spacy.load("en_core_web_sm")

def analyze_document(filename):
    if filename is None:
        print("error 1: do not enter a document for text analysis")
        return 1

    if not os.path.exists(filename):
        print("error 2: document does not exist")
        return 2

    if not filename.endswith('.txt'):
        print("error 3: document exists but this module only accepts txt. We use upload.py to get txt of document and then put it into textanalyzer.py")
        return 3
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return 4
    '''  
    with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'ADJ')]
    blob = TextBlob(text)
    sentiment = blob.sentiment
    summary = '. '.join(text.split('. ')[:3]) + '.'
    result = (f"Entities:\n{'; '.join([f'{ent[0]} ({ent[1]})' for ent in entities])}\n\n"
              f"Keywords:\n{', '.join(keywords)}\n\n"
              f"Sentiment Polarity: {sentiment.polarity}\n\n"
              f"Summary:\n{summary}\n")
    print(result)
    print("situation 4: analyze text successfully")
    new_filename = f"result_of_{filename.replace('.pdf', '.txt')}"
    
    # 打开文件并写入结果
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(result)
    return 4

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    status = analyze_document(filename)
    sys.exit(status)  # Use the status code as the exit code

if __name__ == '__main__':
    main()

    
