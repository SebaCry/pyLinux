import unittest, os
from src.bank_account import BankAccount
from unittest.mock import patch, Mock
from src.exceptions import WithdrawalTimeRestrictonError

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:  ## LA FUNCION SETUP, sirve para inicializar vairables, que se usaran en diferentes tests => balance=1000
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file): ## LA FUNCION TEARDOWN, HACER ALGO DESPUES DE CADA TESTS
            os.remove(self.account.log_file)
        ##pass

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())

    def test_deposite(self):
        new_balance = self.account.deposite(500)
        self.assertEqual(new_balance, 1500, 'El balance no es igual')

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, 'El balance no es igual')

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_validation_transfer(self):
        new_balance = self.account.transfer(200) 
        assert new_balance == 800

    def test_error_trasnfer(self):
        with self.assertRaises(ValueError) as context: ## Este bloque de with, captura la excepcion si la hay en el metodo de transfer
            self.account.transfer(1200)
        self.assertEqual(str(context.exception), 'Solo se puede transferir si es menor el monto al balance') ## Aca se valida si la excepcion del meteodo sea la misma que la del test

    def test_transaction_log(self):
        self.account.deposite(500)
        self.assertTrue(os.path.exists('transaction_log.txt'))

    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 2
        self.account.deposite(500)
        assert self._count_lines(self.account.log_file) == 3

    def test_log_transaction_fail(self):
        with self.assertRaises(ValueError) as context:
            self.account.transfer(1200)
        self.assertEqual(str(context.exception), 'Solo se puede transferir si es menor el monto al balance')

        with open(self.account.log_file, 'r') as f:
            log_content = f.read()
        self.assertIn('Intento fallido de transferencia', log_content) 
    
    @patch('src.bank_account.datetime')
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 19
        with self.assertRaises(WithdrawalTimeRestrictonError):
            self.account.withdraw(100)

    def test_deposite_varios_ammounts(self):
        test_cases = [
            {'ammount' : 100, "expected" : 1100},
            {'ammount' : 3000, "expected" : 4000},
            {'ammount' : 4500, "expected" : 5500},
        ]

        for case in test_cases:
            with self.subTest(case=test_cases):
                self.account = BankAccount(balance=1000, log_file='transaction.txt')
                new_balance = self.account.deposite(case['ammount'])
                self.assertEqual(new_balance, case['expected'])