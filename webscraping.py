import requests
import bs4


result=requests.get("https://en.wikipedia.org/wiki/Eliud_Kipchoge")
sop=bs4.BeautifulSoup(result.text, "lxml")

#print(sop.select('title'))
print(sop.select('p')[1].get_text())
print('____________________________________________________')
for item in sop.select('.vector-toc-text'):
    print (item.text)
print("======================================================")
print(sop.select('.vector-toc-text')[1])