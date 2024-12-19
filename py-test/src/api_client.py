import requests
import ipaddress

def get_location(ip):
    try:
        ipaddress.ip_address(ip)

        url = f'https://freeipapi.com/api/json/{ip}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'country' : data["countryName"],
            'region' : data['regionName'],
            'city' : data['cityName'],
        }
    except ValueError:
        return False