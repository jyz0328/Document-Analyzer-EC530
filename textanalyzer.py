# textanalyzer.py
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_document(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    keywords = [token.text for token in doc if token.pos_ in ('NOUN', 'ADJ')]
    blob = TextBlob(text)
    sentiment = blob.sentiment
    summary = '. '.join(text.split('. ')[:3]) + '.'
    return {
        "entities": entities,
        "keywords": keywords,
        "sentiment": sentiment.polarity,
        "summary": summary
    }

