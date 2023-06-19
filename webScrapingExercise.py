#Web Scraping Exercise
#import libraries 
import requests
import bs4

res= requests.get("http://quotes.toscrape.com/")
'''get soap'''
soap=bs4.BeautifulSoup(res.text,'lxml')
'''
get author using class attr  .author
'''
authors=soap.select('.author')
'''iterate'''
for author in authors:
    print(author.text) #print authors 

