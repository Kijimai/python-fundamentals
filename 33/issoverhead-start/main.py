import os
import requests
import smtplib
from datetime import datetime
from dotenv import load_dotenv
import time

# 60 second interval
# time.sleep(60)

load_dotenv()

MY_LAT = 51.678516  # Your latitude
MY_LONG = -61.773300  # Your longitude

CURR_EMAIL = os.getenv('MY_EMAIL')
CURR_PW = os.getenv('MY_PW')

email_options = {
    "yahoo": "smtp.mail.yahoo.com",
    "hotmail": "smtp.live.com",
    "outlook": "outlook.office365.com",
    "gmail": "smtp.gmail.com"
}

# Your position is within +5 or -5 degrees of the ISS position.


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        print("Within range")
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# while True:
if is_iss_overhead() and is_night():
    with smtplib.SMTP(email_options["gmail"], port=587) as connection:
        # Starts a secure connection with the server
        connection.starttls()
        connection.login(user=CURR_EMAIL, password=CURR_PW)
        connection.sendmail(from_addr=CURR_EMAIL,
                            to_addrs="jdbucog@yahoo.com", msg="Subject:ISS Overhead!\n\nLook up at the sky!!")   