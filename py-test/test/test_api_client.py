import unittest
import unittest.mock
import requests

from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    @patch('src.api_client.requests.get') ## PATCH crea una nueva variable dentro de esa misma prueba. Asi mismo mock, simula peticiones de API, para mejorar el rendimiento de los tests
    def test_get_location_returns_expected(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
        'countryName' : 'USA',
        'regionName' : 'FLORIDA',
        'cityName' : 'MIAMI',
    }

        result = get_location('8.8.8.8')

        self.assertEqual(
            result.get('country'), 'USA'
        )
        self.assertEqual(
            result.get('region'), 'FLORIDA'
        )
        self.assertEqual(
            result.get('city'), 'MIAMI'
        )

        mock_get.assert_called_once_with('https://freeipapi.com/api/json/8.8.8.8')

    @patch('src.api_client.requests.get') ## PATCH crea una nueva variable dentro de esa misma prueba. Asi mismo mock, simula peticiones de API, para mejorar el rendimiento de los tests
    def test_get_location_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException('Service Unavailable'),
            unittest.mock.Mock(
                status_code = 200,
                json = lambda: {
                    'countryName' : 'USA',
                    'regionName' : 'FLORIDA',
                    'cityName' : 'MIAMI', 
                }
            )
        ]
        
        
        with self.assertRaises(requests.exceptions.RequestException):
            get_location('8.8.8.8')
        

        result = get_location('8.8.8.8')
        self.assertEqual(result.get('country'), 'USA')
        self.assertEqual(result.get('region'), 'FLORIDA')
        self.assertEqual(result.get('city'), 'MIAMI')

    '''
    def test_get_location_valid_ip(self):
        ip_cases = [
            ('192.168.0.1', True),
            ('8.8.8.8', True),
            ('255.255.255.255', True),
            ('0.0.0.0', True),
            ('256.0.0.1', False),
            ('1.2.3.4.5', False),
            ('192.168.0', False),
            ('192.168.0.a', False),
            ('-192.168.0.1', False),
        ]

        for ip, valid in ip_cases:
            with self.subTest(ip=ip):
                self.assertEqual(get_location(ip), valid, f'La ip no es valida choco papu')
    '''