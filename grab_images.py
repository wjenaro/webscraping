import requests
import bs4

results=requests.get("https://en.wikipedia.org/wiki/Monkey")
soup=bs4.BeautifulSoup(results.text, "lxml")


print(soup.select('.image-section')[0])
