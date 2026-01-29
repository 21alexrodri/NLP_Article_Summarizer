from re import S
from model.nltk_tokenize_class import NLTKTokenizer
from model.spacy_tokenize_class import SpacyTokenizer
from model.article_extractor_class import ArticleExtractor
from model.article_summarizer_class import ArticleSummarizer
url = "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded"

science_article = ArticleExtractor(url)
print("Title:", science_article.title)
text = science_article.extract_text_bs4_method()


summarizer = ArticleSummarizer()
summary = summarizer.summarize(text)

print("\nRESUM DE L'ARTICLE:\n")
print(summary)



# tokenizer = SpacyTokenizer()
# tokens = tokenizer.clean_tokenize(text)
# print(tokens)


