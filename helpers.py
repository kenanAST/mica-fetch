from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()


def get_token():
    url = 'https://mica.msuiit.edu.ph/'
    driver = webdriver.Chrome()
    driver.get(url)

    username_xpath = '/html/body/div[1]/main/div[1]/div/div/div/div[1]/div/div[1]/div/form/div[1]/input'
    password_xpath = '/html/body/div[1]/main/div[1]/div/div/div/div[1]/div/div[1]/div/form/div[2]/input'

    username = driver.find_element(By.XPATH, username_xpath)
    username_details = os.getenv('USERNAME')
    username.send_keys(username_details)

    password = driver.find_element(By.XPATH, password_xpath)
    password_details = os.getenv('PASSWORD')
    password.send_keys(password_details)
    password.send_keys(Keys.ENTER)

    token = driver.get_cookie('token')['value']

    print(f"Token: {token}")
    print(f"Data Type: {type(token)}")

    return token


