import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://autochek.africa/ke/cars-for-sale?price_low=330000&price_high=1560000&page_number=1"

# Send an HTTP GET request
response = requests.get(url)
if response.status_code==200:
   soup=BeautifulSoup(response.content, "html.parser")
   print(soup.text)
   # Find all elements with class "b-list-advert-base__data__price"
   prices = soup.find_all("p", class_="MuiTypography-root MuiTypography-body1 css-1bztvjj")
   vehicle_name=soup.find_all("h6", class_="MuiTypography-root MuiTypography-h6 css-1g399u0")
    
    # Extract and print the text from each price element    class=""
    # Iterate through both price and vehicle name elements in parallel
   for price_element, name_element in zip(prices, vehicle_name):
        price = price_element.get_text(strip=True)
        name = name_element.get_text(strip=True)
        print("Vehicle:", name)
        print("Price:", price)
        print("-" * 50)
    # Open a text file for writing
   with open("results_autocheck.txt", "w") as file:
        # Iterate through both price and vehicle name elements in parallel
        for price_element, name_element in zip(price, vehicle_name):
            price = price_element.get_text(strip=True)
            name = name_element.get_text(strip=True)
            file.write("Vehicle: " + name + "\n")
            file.write("Price: " + price + "\n")
            file.write("-" * 50 + "\n")
else:
    print("No connection ")
