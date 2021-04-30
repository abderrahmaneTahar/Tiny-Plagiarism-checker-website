import pypandoc
from nltk.tokenize import sent_tokenize
import random
import scrap
import similarity


def docx_to_string(docxFilename):
    return pypandoc.convert_file(docxFilename, 'plain')

def get_random_sentence(string):
    return random.choice(sent_tokenize(string))

def process_file(file):
    file_string = docx_to_string(file)
    sentences = sent_tokenize(file_string)
    sims = []
    for i in range(2):
        sentence = random.choice(sentences)
        top_texts = scrap.get_top_texts(sentence)
        sim = [similarity.simularity(text, file_string)  for text in top_texts]
        print(sim)
        sims.append(sim)
    return sims

