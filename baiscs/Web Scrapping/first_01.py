import os
import requests
import csv
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"

def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("network error", e)
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")

    posts = []
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get("href").strip()
        posts.append({"title": title, "url": url})
        return posts

def save_to_csv(posts):
    if not posts:
        print("Nothing to save ")
        return
    with open(CSV_FILE, "w", encoding="utf") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(posts)
        print("✅ Done ")

def main():
    print("Scrappng the hacker news post...")
    posts = fetch_top_post()
    print("Collecting the data to save...")
    save_to_csv(posts)


if __name__ == "__main__":
    main()

    