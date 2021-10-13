import unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):
    """tests that register list holds 88 coins"""

    def setUp(self):
        """Sets up testing environment """
        self.soda_machine = SodaMachine()
    

    def test_register_list(self):
        """Checking to see if list length is 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

    def test_inventory_list(self):
        """Checking to see if list length is 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

    def test_get_coin_quarter(self):
        """Checking each coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_get_coin_dime(self):
        """Checking each coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_get_coin_nickel(self):
        """Checking each coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_get_coin_penny(self):
        """Checking each coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_not_valid_coin(self):
        """Checking to pass in a string that is not a valid coin name will return None"""
        returned_coin = self.soda_machine.get_coin_from_register('Yen')
        self.assertEqual(returned_coin, None)

if __name__ == '__main__':
    unittest.main()