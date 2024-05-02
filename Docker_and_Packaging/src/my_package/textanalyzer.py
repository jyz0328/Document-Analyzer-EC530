# textanalyzer.py
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_document(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]# 命名实体识别
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'ADJ')]# 关键词提取
    blob = TextBlob(text) # 情感分析，使用TextBlob
    sentiment = blob.sentiment 
    summary = '. '.join(text.split('. ')[:3]) + '.'# 摘要生成
    # 创建一个格式化的输出字符串
    result = f"Entities:\n{'; '.join([f'{ent[0]} ({ent[1]})' for ent in entities])}\n\n"
    result += f"Keywords:\n{', '.join(keywords)}\n\n"
    result += f"Sentiment Polarity: {sentiment.polarity}\n\n"
    result += f"Summary:\n{summary}\n"
    #不仅输出result,希望把result保存为result_of_原文件名 怎么做
    # Save result to a file

    return result

def save_analysis_results(result, original_filename):
    # 构建新的文件名
    new_filename = f"result_of_{original_filename.replace('.pdf', '.txt')}"
    
    # 打开文件并写入结果
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(result)

