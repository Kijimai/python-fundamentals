import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
import requests
import json
import datetime as dt
load_dotenv()


API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

# Twilio environment variables
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_ACC_SID = os.getenv("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

parameters = {
    "lat":  10.42,
    "lon": 122.431297,
    "exclude": "current,minutely,daily",
    "appid": os.getenv('OWM_API_KEY')
}


response = requests.get(API_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# with open('./weather_data.json',mode='w') as weather_file:
#     json.dump(weather_data, weather_file)

# with open('./weather_data.json', mode="r") as file:
#   weather_data = json.load(file)

hourly_data = weather_data["hourly"]
first_twelve = hourly_data[:12]

# print(first_twelve)

client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
# BODY_MESSAGE = input("Whats your message to yourself?")

# for item in first_twelve:
condition_code = first_twelve[0]["weather"][0]["id"]
if condition_code < 700:
  print("Bring an umbrella, it's going to rain!")
  FROM_NUMBER = TWILIO_NUMBER
  TO_NUMBER = os.getenv('MY_NUMBER')
  message = client.messages.create(body="It's gonna rain today! Bring an umbrella!", from_=FROM_NUMBER, to=TO_NUMBER)
  # else:
  #   current_id = item["weather"][0]["id"]
  #   print(f"Weather's fine :) {current_id}")

