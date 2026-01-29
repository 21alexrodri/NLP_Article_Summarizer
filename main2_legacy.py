import requests
from bs4 import BeautifulSoup
from model.nltk_tokenize_class import NLTKTokenizer
from model.topic_classifier_class import TopicClassifier


TITLES = [
    "ARTICLE MARC",
    "LAMINE YAMAL",
    "INVERSIO OR",
    "GORILA ALBINO",
    "TREN DE ESPANYA MORT"
]
url1 = "https://link.springer.com/article/10.1186/s12915-020-00925-x"
url2 = "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded"
url3 = "https://goldbroker.com/news/fallacy-inverse-relationship-between-gold-dollar-index-dxy-3363"
url4 = "https://www.nbcnews.com/id/wbna3541441"
# url5 crashes amb BeautifulSoup
url5 = "https://www.ap.org/the-definitive-source/behind-the-news/spain-train-crash-how-a-journalists-quick-thinking-led-to-vital-info/"
URLS = [url1, url2, url3, url4, url5]

response = requests.get(url1)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

article = soup.find("article")

if article:
    text = article.get_text(separator=" ", strip=True)
else:
    text = soup.get_text(separator=" ", strip=True)


# PRINT TITLE
h1 = soup.find("h1")
if h1:
    title = h1.get_text(strip=True)
else:
    title = soup.find("title").get_text(strip=True)

# PAS 2 - TOKENITZACIÓ I NORMALITZACIÓ DEL TEXT
tokenizer = NLTKTokenizer()
tokens = tokenizer.clean_tokenize(text)

# PAS 3 - CLASSIFICACIÓ DEL TEXT
classifier = TopicClassifier()
text_tokenized = " ".join(tokens[:500])
classification = classifier.classify(text_tokenized)

for label, score in zip(classification['labels'], classification['scores']):
    print(f"{label:<15}: {score:.4f}")

    '''
    TEXT TOKENIZED ARTICLE MARC (1500)
        Entertainment  : 0.1715
        Business       : 0.1512
        Science        : 0.1380
        Politics       : 0.1239
        Technology     : 0.1215
        Sports         : 0.1115
        Health         : 0.0986
        Society        : 0.0839

    TEXT NORMAL ARTICLE MARC (1500)
        Health         : 0.1893
        Science        : 0.1741
        Technology     : 0.1740
        Business       : 0.1416
        Society        : 0.1109
        Politics       : 0.0780
        Entertainment  : 0.0665
        Sports         : 0.0656

    TEXT NORMAL ARTICLE MARC (full)
        Entertainment  : 0.3059
        Business       : 0.1783
        Technology     : 0.1348
        Science        : 0.1192
        Society        : 0.0849
        Health         : 0.0816
        Sports         : 0.0487
        Politics       : 0.0467

    TEXT TOKENIZED ARTICLE MARC (full)
        Entertainment  : 0.1715
        Business       : 0.1512
        Science        : 0.1380
        Politics       : 0.1239
        Technology     : 0.1215
        Sports         : 0.1115
        Health         : 0.0986
        Society        : 0.0839
    '''