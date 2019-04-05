import requests

if __name__=="__main__":
    url = "https://app.ecwid.com/api/v3/16941237/profile?token=secret_pcVAYggLXsRg36DKNiHxNgze8aB2BBui"
    response = requests.get(url)
    print(response.text)