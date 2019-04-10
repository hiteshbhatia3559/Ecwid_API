from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv
import requests


def openurl_function(username, password):
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get(
        'https://my.ecwid.com/api/oauth/authorize?client_id=custom-app-avantgardegifts&client_secret=Gh9FXunMCPc5E2yPn8Rl9czLWwfsVSoH&response_type=code&scope=UPDATE_ORDERS+READ_ORDERS+CREATE_CATALOG+UPDATE_CATALOG+READ_CATALOG&redirect_uri=http://127.0.0.1')
    sleep(5)
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("SIF.sIB").click()
    sleep(100)
    url = driver.current_url
    code = url.split("=")
    driver.quit()
    return code[1]


if __name__ == "__main__":
    url = "https://app.ecwid.com/api/v3/16941237/profile?token=secret_pcVAYggLXsRg36DKNiHxNgze8aB2BBui"
    response = requests.get(url)
    print(openurl_function(username="web@avantgardegifts.co.uk", password="P^7!RklE&kthjo2@j1fC"))
