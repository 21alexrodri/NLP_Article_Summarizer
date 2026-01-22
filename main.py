from newspaper import Article

# url = "https://link.springer.com/article/10.1186/s12915-020-00925-x"
url = "https://en.nogomania.com/read/Was-it-really-offside-Barca-rage-after-controversial-decision-in-San-Sebastian#goog_rewarded"
# url = "https://goldbroker.com/news/fallacy-inverse-relationship-between-gold-dollar-index-dxy-3363"
# url = "https://www.nbcnews.com/id/wbna3541441"
# url = "https://www.ap.org/the-definitive-source/behind-the-news/spain-train-crash-how-a-journalists-quick-thinking-led-to-vital-info/"
art = Article(url)
art.download()
art.parse()

print(art.text)
