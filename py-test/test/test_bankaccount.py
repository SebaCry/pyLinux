import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):

    def setUp(self) -> None:  ## LA FUNCION SETUP, sirve para inicializar vairables, que se usaran en diferentes tests => balance=1000
        self.account = BankAccount(balance=1000)

    def test_deposite(self):
        new_balance = self.account.deposite(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_validation_transfer(self):
        new_balance = self.account.transfer(200) 
        assert new_balance == 800

    def test_error_trasnfer(self):
        new_balance = self.account.transfer(1200)
        assert new_balance == 1200