from newspaper import Article
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
url5 = "https://www.ap.org/the-definitive-source/behind-the-news/spain-train-crash-how-a-journalists-quick-thinking-led-to-vital-info/"
URLS = [url1, url2, url3, url4, url5]

print("".ljust(80, "-"))
for title, url in zip(TITLES, URLS):
    print(title)
    print("\n")
    art = Article(url)
    art.download()
    art.parse()
    print(art.text)
    print("".ljust(80, "-"))
