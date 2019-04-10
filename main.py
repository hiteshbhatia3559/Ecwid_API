from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import socket
import csv
import requests
from ast import literal_eval

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
    sleep(3)
    url = driver.current_url
    code = url.split("=")
    driver.quit()
    return code[1]

def get_access_token(client_id, client_secret,code):
    url = 'https://my.ecwid.com/api/oauth/token?client_id={}&client_secret={}&code={}&redirect_uri=http://127.0.0.1&grant_type=authorization_code'.format(
        client_id, client_secret, code)
    response = requests.get(url)
    print(response.text)
    return literal_eval(response.text)

if __name__ == "__main__":
    code = openurl_function(username="web@avantgardegifts.co.uk", password="P^7!RklE&kthjo2@j1fC")
    client_id = 'custom-app-avantgardegifts'
    client_secret = 'Gh9FXunMCPc5E2yPn8Rl9czLWwfsVSoH'
    store_id = 15833734
    access_token = get_access_token(client_id,client_secret,code)['access_token']
    pages = []
    with open("data.txt","w+") as writefile:
        for page in range(0,11):
            url = 'https://app.ecwid.com/api/v3/{}/products?offset={}&limit=100&token={}'.format(store_id,page,access_token)
            response = requests.get(url).json()
            pages.append(response)
    a = ""
    items = []
    for page in pages:
        for item in page['items']:
            try:
                a = item['quantity']
                items.append(item)
            except:
                pass

    for item in items:
        print(len(item.keys())) # numbers are different... dont know why
