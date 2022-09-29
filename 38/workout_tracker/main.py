from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NUTRX_API_KEY")
APP_ID = os.getenv("APP_ID")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"
SHEETY_URL = f"https://api.sheety.co/5b0f238e12cc0aac4770a3a2d3e59bd4/{PROJECT_NAME}/{SHEET_NAME}"
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "Authorization": "Basic " + BEARER_TOKEN
}

request_body = {
    "query": input("What kind of exercise did you do today: "),
    "gender": "male",
    "weight_kg": 63.5,
    "height_cm": 158.5,
    "age": 30
}

response = requests.post(API_ENDPOINT, json=request_body, headers=api_headers)
result = response.json()

todays_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print(todays_date, now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(SHEETY_URL, json=sheet_inputs)

print(sheet_response.text)
