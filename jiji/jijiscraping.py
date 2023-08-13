import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://jiji.co.ke/"#input(" Provide URL: ")
result_file=input("name of the file: ")

# Send an HTTP GET request
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all elements with class "b-list-advert-base__data__price"
    price_elements = soup.find_all("div", class_="b-list-advert-base__data__price")
    
    # Find all elements with class "qa-advert-list-item-title b-list-advert-base__item-title"
    vehicle_name_elements = soup.find_all("div", class_="qa-advert-list-item-title b-list-advert-base__item-title")
    
    # Create a list to store data
    data = []

    # Iterate through both price and vehicle name elements in parallel
    for price_element, name_element in zip(price_elements, vehicle_name_elements):
        price = price_element.get_text(strip=True)
        name = name_element.get_text(strip=True)
        data.append([name, price])
    
    # Create a DataFrame using pandas
    df = pd.DataFrame(data, columns=["Vehicle Name", "Price"])
    
    # Save the DataFrame to a CSV file
    df.to_csv(result_file, index=False)
    
    print(f"Results saved in {result_file}")
else:
    print("No connection")
