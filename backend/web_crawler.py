import requests
from bs4 import BeautifulSoup

def start_crawling():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for article in soup.select("a.gs-c-promo-heading"):
        title = article.get_text()
        link = article["href"]
        articles.append({"title": title, "link": f"https://www.bbc.com{link}"})

    return articles[:5]