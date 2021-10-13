import unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):
    """test that register list has a len of 88"""

    def setUp(self):
        self.soda_machine = SodaMachine()
    

    def test_register_list(self):
        """Checking to see if list length is 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

class TestFillInventory(unittest.TestCase):
    """test that its inventory list has a len of 30"""

    def setUp(self):
        self.soda_machine = SodaMachine()


    def test_inventory_list(self):
        """Checking to see if list length is 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

class TestGetCoinFromRegister(unittest.TestCase):
    """Test each type of coin can be returned from register"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_get_coin_quarter(self):
        """Checking quarter coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_get_coin_dime(self):
        """Checking dime coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_get_coin_nickel(self):
        """Checking nickel coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_get_coin_penny(self):
        """Checking penny coin type can be returned from register"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_not_valid_coin(self):
        """Checking to pass in a string that is not a valid coin name will return None"""
        returned_coin = self.soda_machine.get_coin_from_register('Yen')
        self.assertEqual(returned_coin, None)

class TestRegisterHasCoin(unittest.TestCase):
    """Testing coin names in register are True or False"""

    def setUp(self):
        self.soda_machine = SodaMachine()  

    def test_coin_true_quarter(self):
        """Checking that Quarter type of coin will return True"""
        returned_coin = self.soda_machine.register_has_coin('Quarter')
        self.assertEqual(returned_coin, True)

    def test_coin_true_dime(self):
        """Checking that Dime type of coin will return True"""
        returned_coin = self.soda_machine.register_has_coin('Dime')
        self.assertEqual(returned_coin, True)

    def test_coin_true_nickel(self):
        """Checking that Nickel type of coin will return True"""
        returned_coin = self.soda_machine.register_has_coin('Nickel')
        self.assertEqual(returned_coin, True)

    def test_coin_true_penny(self):
        """Checking that Penny type of coin will return True"""
        returned_coin = self.soda_machine.register_has_coin('Penny')
        self.assertEqual(returned_coin, True)

    def test_coin_false(self):
        """Checking that a non-valid coin name will return False"""
        returned_coin = self.soda_machine.register_has_coin('Yen')
        self.assertFalse(returned_coin, False)

if __name__ == '__main__':
    unittest.main()