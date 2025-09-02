import pandas as pd
import requests
from bs4 import BeautifulSoup

name = []
price = []
rating = []

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

try:
    r = requests.get(url)
    r.raise_for_status()  
    soup = BeautifulSoup(r.text, "lxml")

    products = soup.select(".product-wrapper.card-body")

    for product in products:
        try:
            name.append(product.select_one("a.title").get_text(strip=True))
            price.append(product.select_one("h4.price").get_text(strip=True))
            rating.append(len(product.select(".ws-icon.ws-icon-star")))
        except AttributeError:
            name.append("error")
            price.append("error")
            rating.append("error")

    df = pd.DataFrame({"Product Name": name, "Price": price, "Rating": rating})
    df.to_csv("C:/Users/khem4/OneDrive/Desktop/projects/Webscraping/tablets.csv", index=False)
    print("CSV file created successfully")

except requests.exceptions.RequestException:
    print("This site cannot allow data scraping")