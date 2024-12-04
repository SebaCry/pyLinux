import unittest
from test_bankaccount import BankAccountTests



def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests('test_deposite'))
    suite.addTest(BankAccountTests('test_withdraw'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())