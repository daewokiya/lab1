import unittest
from account import *

class Account(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.account_name, "John")
        self.assertEqual(self.accont_balance, 0)

    def test_deposit(self):
        self.assertEqual(Account.deposit(self, 100), 100)

    def test_withdraw(self):
        self.assertEqual(Account.withdraw(self, 50), 50)

if __name__ == '__main__':
    unittest.main()