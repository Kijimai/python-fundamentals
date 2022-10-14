import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

EMAIL = os.getenv("MY_EMAIL")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://secure-retreat-92358.herokuapp.com/")
f_input = driver.find_element(By.NAME, "fName")
l_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.XPATH, '/html/body/form/button')
f_input.send_keys("Jibby")
l_input.send_keys("Jams")
email_input.send_keys(EMAIL)
btn.click()


# driver.quit()