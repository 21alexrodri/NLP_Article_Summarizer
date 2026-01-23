from re import S
from model.nltk_tokenize_class import NLTKTokenizer
from model.spacy_tokenize_class import SpacyTokenizer
from model.article_extractor_class import ArticleExtractor

url = "https://link.springer.com/article/10.1186/s12915-020-00925-x"

science_article = ArticleExtractor(url)
print("Title:", science_article.title)
text = science_article.extract_text_bs4_method()






tokenizer = SpacyTokenizer()
tokens = tokenizer.clean_tokenize(text)
print(tokens)


