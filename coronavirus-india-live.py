import requests
from bs4 import BeautifulSoup

def start():
 page = requests.get("https://economictimes.indiatimes.com/news/politics-and-nation/coronavirus-cases-in-india-live-news-latest-updates-march22/liveblog/74754630.cms")
 soup = BeautifulSoup(page.content, 'html.parser')
 counting = soup.find(class_="textDiv l1")
 print(counting.h1.get_text())
 print("\n")
 start()

start()
