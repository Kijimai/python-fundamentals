import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
load_dotenv()

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)


product_url = "https://www.amazon.com/ASUS-IPS-Type-i7-11800H-Processor-FX506HEB-IS73/dp/B0B13Y8LK2?ref_=Oct_DLandingS_D_06d8baa3_69&smid=ATVPDKIKX0DER"


# sleep(5)
# wait = WebDriverWait(driver, 10)

driver.get(product_url)

# wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "a-offscreen")))

# price_el = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(price_el.text)

# Locating, clicking, input, and submitting a search query in amazon
# search_bar_el = driver.find_element(By.NAME, "field-keywords")
# print(search_bar_el)
# submit_btn = driver.find_element(By.ID, "nav-search-submit-button")
# search_bar_el.click()
# search_bar_el.send_keys("Hello World")
# submit_btn.click()

# Using xpath to locate an element
search_bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
search_bar.send_keys("Hello World")
submit_btn = driver.find_element(By.XPATH, '//*[@id="nav-search-submit-button"]')
submit_btn.click()
# Closes the tab
# driver.close()

# Closes the whole browser
# driver.quit()
