from time import sleep
from selenium import webdriver
import csv
import requests
from ast import literal_eval


def openurl_function(username, password):
    print("Please wait, Chrome will now open to retreive the access token")
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


def get_access_token(client_id, client_secret, code):
    url = 'https://my.ecwid.com/api/oauth/token?client_id={}&client_secret={}&code={}&redirect_uri=http://127.0.0.1&grant_type=authorization_code'.format(
        client_id, client_secret, code)
    response = requests.get(url)
    # print(response.text)
    print("Got access token\n")
    return literal_eval(response.text)


def write_data(name_of_file, net):
    temp = []
    for item in net:
        temp.append(len(list(item.keys())))
    index = temp.index(max(temp))

    keys = net[index].keys()
    with open(name_of_file, 'w+', newline='') as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(net)
        print("Done writing to Results.csv\n")
