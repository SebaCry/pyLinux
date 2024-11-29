import requests

def currencys(api_key, api_url):
    headers = {
        'Bmx-token' : api_key
    }
    response = requests.get(api_url, headers=headers)

    return response

