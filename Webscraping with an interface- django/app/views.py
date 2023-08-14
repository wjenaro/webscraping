from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    if request.method=="POST":
        url=request.POST.get('url', '')
        dom_type = request.POST.get('domType', '')  
        class_name = request.POST.get('class', '') 
        pdom_type = request.POST.get('pdomType', '')  
        pclass_name = request.POST.get('pclass', '') 
        '''get response'''

        response=   requests.get(url)
        #check whether the there is connection
      
        if response.status_code==200:#if the connection is successful
            #get soup
            soup=BeautifulSoup(response.content, "html.parser")
            #get prices and vehicle names based on data provided
            vehicle_name=soup.find_all(dom_type, class_=class_name)
            vehicle_price = soup.find_all(pdom_type, class_=pclass_name)
            cars=[]
            car_prices=[]
            for name_element, price_element in zip(vehicle_name, vehicle_price):
                name = name_element.get_text(strip=True)
                p = price_element.get_text(strip=True)
                cars.append(name)
                car_prices.append(p)
                re=zip(cars,car_prices)
                


            
            context={"url":url, "myzip":re,"vehicles": cars, "prices": car_prices}
            return render(request, 'app/index.html', context)
        else:
            msg="Failed to fetch the page:"
            return render(request, "app/index.html", {"msg":msg})
    else:
        return render(request, "app/index.html")