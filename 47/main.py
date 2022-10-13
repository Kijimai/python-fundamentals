import requests as rq
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PW = os.getenv("MY_PW")

# Headers required for GETting amazon html response
req_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

product_url = "https://www.amazon.com/ASUS-IPS-Type-i7-11800H-Processor-FX506HEB-IS73/dp/B0B13Y8LK2?ref_=Oct_DLandingS_D_06d8baa3_69&smid=ATVPDKIKX0DER"

response_html = rq.get(product_url, headers=req_headers).text

prod_soup = BeautifulSoup(response_html, "lxml")

try:
    product_name = prod_soup.select("span#productTitle")[0].getText().strip().encode("ascii", "ignore")
except AttributeError:
    print("Product not found! The webpage may have been altered in its html.")

product_price = float(prod_soup.select_one(
    "span.a-price span.a-offscreen").getText().strip("$"))
print(product_price)
print(product_name)

BUY_PRICE = 1000

if product_price < BUY_PRICE:
    message = f"Subject:Amazon Price Change Alert\n\n{product_name} is now {product_price}. \n{product_url}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PW)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=message)
