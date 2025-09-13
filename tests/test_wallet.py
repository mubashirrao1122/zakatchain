import unittest
from src.wallet.wallet import Wallet

class TestWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet(initial_balance=1000)

    def test_initial_balance(self):
        self.assertEqual(self.wallet.balance, 1000)

    def test_deduct_zakat(self):
        zakat_amount = self.wallet.deduct_zakat()
        self.assertEqual(zakat_amount, 25)  # 2.5% of 1000
        self.assertEqual(self.wallet.balance, 975)

    def test_update_balance(self):
        self.wallet.update_balance(500)
        self.assertEqual(self.wallet.balance, 1475)  # 975 + 500

    def test_deduct_more_than_balance(self):
        self.wallet.deduct_zakat()  # Deduct Zakat first
        self.wallet.update_balance(-1000)  # Attempt to deduct more than balance
        self.assertEqual(self.wallet.balance, 475)  # Should not go below zero

if __name__ == '__main__':
    unittest.main()