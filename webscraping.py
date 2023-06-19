import requests
import bs4


result=requests.get("https://en.wikipedia.org/wiki/Eliud_Kipchoge")
sop=bs4.BeautifulSoup(result.text, "lxml")

print(sop.select('title'))
print(sop.select('p'))