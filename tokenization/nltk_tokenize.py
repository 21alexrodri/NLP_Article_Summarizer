import nltk
from nltk.tokenize import word_tokenize
import re

class NLTKTokenizer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('punkt_tab')

    def clean_tokenize(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zà-ú0-9\s]', '', text)
        tokens = word_tokenize(text)
        return tokens
