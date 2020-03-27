import requests
from bs4 import BeautifulSoup

def start():
 page = requests.get("https://www.worldometers.info/coronavirus/country/india")
 soup = BeautifulSoup(page.content, 'html.parser')
 counting = soup.find(class_="maincounter-number")
 print("coronavirus total cases in india"+ counting.get_text())
 start()

start()
