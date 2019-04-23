from lib import openurl_function, get_access_token, write_data
import requests

if __name__ == "__main__":
    code = openurl_function(username="web@avantgardegifts.co.uk", password="P^7!RklE&kthjo2@j1fC")
    client_id = 'custom-app-avantgardegifts'
    client_secret = 'Gh9FXunMCPc5E2yPn8Rl9czLWwfsVSoH'
    store_id = 15833734
    access_token = get_access_token(client_id, client_secret, code)['access_token']
    pages = []
    with open("data.txt", "w+") as writefile:
        for page in range(0, 11):
            url = 'https://app.ecwid.com/api/v3/{}/products?offset={}&limit=100&token={}'.format(store_id, page,
                                                                                                 access_token)
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

    write_data("Results.csv", items)
