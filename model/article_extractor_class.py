import requests
from bs4 import BeautifulSoup
from newspaper import Article

class ArticleExtractor:
    def __init__(self, url, title = None):
        self.url = url
        if title is None:
            self.title = self.extract_title()
        else:
            self.title = title
        
    
    def extract_text_newspaper_method(self):
        art = Article(self.url)
        art.download()
        art.parse()
        return art.text

    def extract_text_bs4_method(self):
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        article = soup.find("article")

        if article:
            text = article.get_text(separator=" ", strip=True)
        else:
            text = soup.get_text(separator=" ", strip=True)
        
        return text
    
    def extract_title(self):
        text = self.extract_text_bs4_method()
        response = requests.get(self.url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
        else:
            title = soup.find("title").get_text(strip=True)
        
        return title
