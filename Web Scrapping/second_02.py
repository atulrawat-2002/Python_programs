from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import requests


BASE_URL = 'https://books.toscrape.com/'
START_PAGE = 'catalogue/page-1.html'
OUTPUT_PAGE = 'books_data.json'
TARGET_COUNT = 70

def scrape_page(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e :
        print(e)
        return [], None
    
    soup = BeautifulSoup(response.text, "html.parser")
   
    for article in soup.select("articel.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()
        print(title)


scrape_page(BASE_URL)