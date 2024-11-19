import unittest

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