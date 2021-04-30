import spacy
nlp = spacy.load('en_core_web_sm')


def simularity(text_1, text_2):
    doc_1 = nlp(text_1)
    doc_2 = nlp(text_2)
    return doc_1.similarity(doc_2)
