import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests
import json
from dotenv import load_dotenv

load_dotenv()

STOCK = "META"
COMPANY_NAME = "Meta Platforms Inc"
STOCK_URL_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_URL_ENDPOINT = "https://newsapi.org/v2/everything"
MY_NUMBER = os.getenv("MY_NUMBER")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.getenv('AV_API_KEY')
}

proxy_client = TwilioHttpClient(
    proxy={'http': os.getenv('http_proxy'), 'https': os.getenv('https_proxy')})

client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)

# =========== Stock API init ===================================

# stock_response = requests.get(STOCK_URL_ENDPOINT, params=stock_parameters)
# stock_data = stock_response.json()

# print(stock_data)

# with open('./stock_data.json', mode="w") as file:
#   json.dump(stock_data, file)

with open('./stock_data.json', mode="r") as file:
    daily_stock_data = json.load(file)
daily_data = daily_stock_data["Time Series (Daily)"]

daily_data_list = [closing for day, closing in daily_data.items()]

yesterday_closing_price = float(daily_data_list[1]["4. close"])
day_before_closing_price = float(daily_data_list[2]["4. close"])

print(yesterday_closing_price, day_before_closing_price)

positive_diff = abs(yesterday_closing_price - day_before_closing_price)

percentage_diff = round((positive_diff / yesterday_closing_price) * 100, 2)
print(percentage_diff)

# adjusted required number for testing purposes
# if percentage_diff > 0.1:
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": os.getenv("NEWS_API_KEY")
}
news_data = requests.get(NEWS_URL_ENDPOINT, params=news_parameters)
news_json = news_data.json()['articles'][:3]
articles = [
    f"Headline: {article['title']}. \nBrief: {article['description']}" for article in news_json]
for article in articles:
    print(article)
    client.messages.create(body=article, from_=TWILIO_NUMBER, to=MY_NUMBER)
    # with open('./news_data.json', mode="w") as data:
    #     json.dump(news_json, data)

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
