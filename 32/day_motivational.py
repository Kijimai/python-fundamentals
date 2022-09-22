import pandas as pd
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
from random import choice

with open('./Birthday Wisher (Day 32) start/quotes.txt') as quote_file:
    quote_list = quote_file.readlines()
stripped_quotes = [quote.strip() for quote in quote_list]

days_dict = {
    "0": "Monday",
    "1": "Tuesday",
    "2": "Wednesday",
    "3": "Thursday",
    "4": "Friday",
    "5": "Saturday",
    "6": "Sunday",
}

current_day = days_dict[str(dt.datetime.now().weekday())]
print(current_day)


load_dotenv()

CURR_EMAIL = os.getenv('MY_EMAIL')
CURR_PW = os.getenv('MY_PW')

email_options = {
    "yahoo": "smtp.mail.yahoo.com",
    "hotmail": "smtp.live.com",
    "outlook": "outlook.office365.com",
    "gmail": "smtp.gmail.com"
}

connection = smtplib.SMTP(email_options["gmail"], port=587)
with smtplib.SMTP(email_options["gmail"], port=587) as connection:
    # Starts a secure connection with the server
    motivation_quote = choice(stripped_quotes)
    connection.starttls()
    connection.login(user=CURR_EMAIL, password=CURR_PW)
    connection.sendmail(from_addr=CURR_EMAIL,
                        to_addrs="jdbucog@yahoo.com", msg=f"Subject:{current_day} Motivation\n\n{motivation_quote}")
