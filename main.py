from re import S
from tokenization.nltk_tokenize import NLTKTokenizer
from tokenization.spacy_tokenize import SpacyTokenizer
from model.article_class import ArticleExtractor

url = "https://link.springer.com/article/10.1186/s12915-020-00925-x"

science_article = ArticleExtractor(url)
print("Title:", science_article.title)
text = science_article.extract_text_bs4_method()






tokenizer = SpacyTokenizer()
tokens = tokenizer.clean_tokenize(text)
print(tokens)