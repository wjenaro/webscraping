import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://jiji.co.ke/cars?query=manual%20in%20cars&price_max=500000"

# Send an HTTP GET request
response = requests.get(url)
if response.status_code==200:
   soup=BeautifulSoup(response.content, "html.parser")
   # Find all elements with class "b-list-advert-base__data__price"
   price_elements = soup.find_all("div", class_="b-list-advert-base__data__price")
   vehicle_name=soup.find_all("div", class_="qa-advert-list-item-title b-list-advert-base__item-title")
    
    # Extract and print the text from each price element
    # Iterate through both price and vehicle name elements in parallel
   for price_element, name_element in zip(price_elements, vehicle_name):
        price = price_element.get_text(strip=True)
        name = name_element.get_text(strip=True)
        print("Vehicle:", name)
        print("Price:", price)
        print("-" * 50)
    # Open a text file for writing
   with open("results.txt", "w") as file:
        # Iterate through both price and vehicle name elements in parallel
        for price_element, name_element in zip(price_elements, vehicle_name):
            price = price_element.get_text(strip=True)
            name = name_element.get_text(strip=True)
            file.write("Vehicle: " + name + "\n")
            file.write("Price: " + price + "\n")
            file.write("-" * 50 + "\n")
else:
    print("No connection ")
