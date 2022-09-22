import os
from dotenv import load_dotenv
import smtplib
import pandas as pd
import datetime as dt
from random import choice

##################### Extra Hard Starting Project ######################

load_dotenv()
CURR_EMAIL = os.getenv('MY_EMAIL')
CURR_PW = os.getenv('MY_PW')

with open('./letter_templates/letter_1.txt') as letter:
    letter_one = letter.readlines()
    letter_one = ''.join([paragraph for paragraph in letter_one])

with open('./letter_templates/letter_2.txt') as letter:
    letter_two = letter.readlines()
    letter_two = ''.join([paragraph for paragraph in letter_two])

with open('./letter_templates/letter_3.txt') as letter:
    letter_three = letter.readlines()
    letter_three = ''.join([paragraph for paragraph in letter_three])

letters = [letter_one, letter_two, letter_three]

email_options = {
    "yahoo": "smtp.mail.yahoo.com",
    "hotmail": "smtp.live.com",
    "outlook": "outlook.office365.com",
    "gmail": "smtp.gmail.com"
}
    
bday_csv_data = pd.read_csv('./birthdays.csv')
bday_list = bday_csv_data.to_dict(orient="records")
current_date = dt.datetime.now()
day = current_date.day
month = current_date.month

# Send the letter and randomize from a choice of letters to send to the person with the birthday
for person in bday_list:
    if person["month"] == month and person["day"] == day:
        print(person)
        choice_letter = choice(letters).replace("[NAME]", person['name'])
        with smtplib.SMTP(email_options["gmail"], port=587) as connection:
            # Starts a secure connection with the server
            connection.starttls()
            connection.login(user=CURR_EMAIL, password=CURR_PW)
            connection.sendmail(from_addr=CURR_EMAIL,
                                to_addrs=person['email'], msg=f"Subject:Happy Birthday!\n\n{choice_letter}")