import unittest

from src.api import currencys

SERVER = 'server_b'

class AllAssertsTests(unittest.TestCase):

    def test_assert(self):
        self.assertEqual(10,10)
        self.assertEqual('Hola','Hola')

    def test_assrt_torf(self):
        self.assertTrue(1)
        self.assertFalse(0)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int('No_soy_un_numero')

    def test_assert_in(self):
        self.assertIn(10, [2, 4 ,5 ,10])
        self.assertNotIn(5, [2,4 ,10])  

    def test_assert_dicts(self):
        user = {'first_name' : 'Juan', 'second_name' : 'Sebastian'}
        self.assertDictEqual(
            {
                'first_name' : 'Juan',
                'second_name' : 'Sebastian'
            } , user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    @unittest.skip('Trabajo en progreso, sera habilitada nuevamente')
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(SERVER == 'server_b', 'Saltado porque no estamos en el servidor')
    def test_Skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)


    API_KEY = '3a343fcfad602cad5c9ff1e434cf30c35ee6aa1d462164dbcdb6570c62b82798'
    URL = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
    respuesta = currencys(API_KEY, URL)

    @unittest.skipUnless(respuesta.status_code == 200, 'Hay un error con el JSON')
    def test_failure_api(self):
        datos = self.respuesta.json()
        self.assertIn('bmx', datos, 'Datos no encontrador en BMX')
        self.assertIn('series', datos['bmx'], 'Falta la clave series')