from re import S
from model.nltk_tokenize_class import NLTKTokenizer
from model.spacy_tokenize_class import SpacyTokenizer
from model.article_extractor_class import ArticleExtractor
from model.article_summarizer_class import ArticleSummarizer
url = "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded"

# science_article = ArticleExtractor(url)
# print("Title:", science_article.title)
# text = science_article.extract_text_bs4_method()


# summarizer = ArticleSummarizer()
# summary = summarizer.summarize(text)

# print("\nRESUM DE L'ARTICLE:\n")
# print(summary)

print("===================================")
print("| Welcome to the NLP Article Test |")
print("===================================\n")
print(" · This is a simple test of how NLP would works")
print(" · This test includes text extraction, tokenization, thematic classification and article summarization.\n")

print("Please, select an article to analyze:")
print("1 - Grasshopper Genome Expansion")
print("2 - Controversial Offside Leaves Barcelona Fuming")
print("3 - Debunking the Gold vs. Dollar Index Fallacy")
print("4 - Albino gorilla dies in Spain")
print("5 - Journalistic Ingenuity in Spain Train Disaster Coverage")

choice = input("Enter the number of your choice (1-5): ")

article_urls = {
    "1": "https://link.springer.com/article/10.1186/s12915-020-00925-x",
    "2": "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded",
    "3": "https://goldbroker.com/news/fallacy-inverse-relationship-between-gold-dollar-index-dxy-3363",
    "4": "https://www.nbcnews.com/id/wbna3541441",
    "5": "https://www.ap.org/the-definitive-source/behind-the-news/spain-train-crash-how-a-journalists-quick-thinking-led-to-vital-info/"
}

if choice in article_urls:
    url = article_urls[choice]
    
else:
    print("Invalid choice. Exiting the program.")




# tokenizer = SpacyTokenizer()
# tokens = tokenizer.clean_tokenize(text)
# print(tokens)


