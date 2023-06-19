#webscrapping test
'''
objectives:
+get books with three ratings
+ extract their titles 
'''
#import necessary modules
import requests
import bs4
pageurl="http://books.toscrape.com/catalogue/category/books_1/page-{}.html"

'''declare container for the titles '''
booktitles=[] # it is empty ---- needs fillings
'''
the site has 50 pages....hence
we will iterate in all of them to check for the books with three star ratings
'''
for n in range(0,51):
    '''
    get request for each page
    '''
    pageRequests=requests.get(pageurl.format(n))
    '''
    get soap for each page
    '''
    pageSoap=bs4.BeautifulSoup(pageRequests.text, 'lxml')
    '''
    select books by class
    +++ book items represented by ".product_pod"
    '''
    books= pageSoap.select('.product_pod')
    '''
    iterate
    '''
    for book in books:
        if len(book.select('.star-rating.Three')) != 0:
            booktitles.append(book.select('a')[1]['title'])

st=""
for titles in booktitles:
        st += titles
print(st)