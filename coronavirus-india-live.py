import requests
from bs4 import BeautifulSoup

def start():
 page = requests.get("https://www.worldometers.info/coronavirus/country/india")
 soup = BeautifulSoup(page.content, 'html.parser')
 titles = soup.find_all(class_="maincounter-number")
 list1 = ["Total cases","Deaths","Recovered"]
 a = 0
 for title in titles:
   print(list1[a]+" = "+title.text.strip())
   a=a+1

start()
