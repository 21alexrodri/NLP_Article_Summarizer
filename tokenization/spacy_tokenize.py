# Si no funciona, executar py -m spacy download en_core_web_sm
import spacy


class SpacyTokenizer:
    def __init__(self):
        self.modelo_sp = spacy.load("en_core_web_sm")


    def clean_tokenize(self, text):
        text = text.lower()
        doc = self.modelo_sp(text)
        tokens = [token.text for token in doc if token.is_alpha or token.is_digit]
        return tokens
      