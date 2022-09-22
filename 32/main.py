# import os
# from dotenv import load_dotenv
# import smtplib

# load_dotenv()

# CURR_EMAIL = os.getenv('MY_EMAIL')
# CURR_PW = os.getenv('MY_PW')

# email_options = {
#     "yahoo": "smtp.mail.yahoo.com",
#     "hotmail": "smtp.live.com",
#     "outlook": "outlook.office365.com",
#     "gmail": "smtp.gmail.com"
# }

# print(CURR_EMAIL, CURR_PW)


# Take off port=587 options for non-gmail email
# connection = smtplib.SMTP(email_options["gmail"], port=587)
# with smtplib.SMTP(email_options["gmail"], port=587) as connection:
#     # Starts a secure connection with the server
#     connection.starttls()
#     connection.login(user=CURR_EMAIL, password=CURR_PW)
#     connection.sendmail(from_addr=CURR_EMAIL,
#                         to_addrs="jdbucog@yahoo.com", msg="Subject:HElllooo Test\n\nThis is the body of my email!")

import datetime as dt

# Returns current date and time
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
seconds = now.second
weekday = now.weekday()
# Also has hour, minutes, etc.
print(year, month, day, seconds)
print(weekday)

date_of_birth = dt.datetime(year=1991, month=11, day=25, hour=4)
print(date_of_birth)
