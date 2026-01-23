import requests
from bs4 import BeautifulSoup
from tokenization.nltk_tokenize import NLTKTokenizer

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

response = requests.get(url2)
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
print(tokens)
