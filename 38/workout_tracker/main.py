import os
import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("NUTRX_API_KEY")
APP_ID = os.getenv("APP_ID")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
data = pd.read_csv('./My Workouts - workouts.csv')

print(data)

api_headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
  "Content-Type": "application/json"
}

request_body = {
  "query": input("What kind of exercise did you do today: "),
  "gender": "male",
  "weight_kg": 63.5,
  "height_cm": 158.5,
  "age": 30
}

response = requests.post(API_ENDPOINT, json=request_body, headers=api_headers)

print(response.text)