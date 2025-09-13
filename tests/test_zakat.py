import unittest
from src.zakat.calculator import calculate_zakat
from src.zakat.rules import ZakatRules

class TestZakatCalculation(unittest.TestCase):

    def setUp(self):
        self.balance = 1000.0
        self.expected_zakat = 25.0  # 2.5% of 1000
        self.zakat_rules = ZakatRules()

    def test_calculate_zakat(self):
        zakat = calculate_zakat(self.balance)
        self.assertEqual(zakat, self.expected_zakat)

    def test_zakat_rules(self):
        self.assertTrue(self.zakat_rules.is_eligible_for_zakat(self.balance))
        self.assertFalse(self.zakat_rules.is_eligible_for_zakat(0))

    def test_zakat_logging(self):
        zakat = calculate_zakat(self.balance)
        # Assuming there's a method to log the transaction
        transaction_log = self.zakat_rules.log_transaction(self.balance, zakat)
        self.assertIn('Zakat deducted', transaction_log)

if __name__ == '__main__':
    unittest.main()