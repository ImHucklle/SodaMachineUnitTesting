import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_Add_to_list_of_money(self):
        """Add to the wallet the correct number of new coins"""
        self.assertEqual(len(self.wallet.money), 88)

if __name__ == '__main__':
    unittest.main()