from typing import Container
import unittest
from soda_machine import SodaMachine
from coins import Quarter, Dime, Nickel, Penny


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

class TestDetermineChangeValue(unittest.TestCase):
    """Testing change values"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_payment_higher(self):
        """Checking the total payment is  higher than the price of the soda"""
        higher_payment = self.soda_machine.determine_change_value(0.75, 0.50)
        self.assertGreater(higher_payment, 0.24)

    def test_soda_higher(self):
        """Checking the price of the soda is  higher than the payment"""
        higher_price = self.soda_machine.determine_change_value(0.25, 0.40)
        self.assertLess(higher_price, 0.76)

    def test_payment_soda_equal(self):
        """Checking the price of the soda and the payemnt are equal"""
        equal_value = self.soda_machine.determine_change_value (1.20, 0.60)
        self.assertEqual(equal_value, 0.60)

class TestCalculateCoinValue(unittest.TestCase):
    """Testing the value of the coin types"""
    
    def setUp(self):
        self.soda_machine = SodaMachine()
        
    def test_coin_value_total(self):
        """Checking the total value of all four coin types is 0.41"""
        my_coins = [Quarter(), Nickel(), Dime(), Penny()]
        my_purchase = self.soda_machine.calculate_coin_value(my_coins)
        self.assertEqual(my_purchase, .41)

    def test_display_payment_value(self):
        """Checking to see passing an empty list returns zero"""
        my_coins = []
        my_purchase = self.soda_machine.calculate_coin_value(my_coins)
        self.assertEqual(my_purchase, .00)

    
class TestGetInventorySoda(unittest.TestCase):
    """Testing the inventory list of the soda cans"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_inventory_cola(self):
        """Checking to pass the Cola into the method to return as Cola"""
        return_soda = self.soda_machine.get_inventory_soda("Cola")
        self.assertEqual(return_soda.name, "Cola")
    
    def test_inventory_orange(self):
        """Checking to pass the Orange Soda into the method to return as Orange Soda"""
        return_soda = self.soda_machine.get_inventory_soda("Orange Soda")
        self.assertEqual(return_soda.name, "Orange Soda")

    def test_inventory_root(self):
        """Checking to pass the Root Beer into the method to return as Root Beer"""
        return_soda = self.soda_machine.get_inventory_soda("Root Beer")
        self.assertEqual(return_soda.name, "Root Beer")

    def test_inventory_m(self):
        """Checking to pass a soda not on the list returns None"""
        return_soda = self.soda_machine.get_inventory_soda("Mountain Dew")

class Testdepositcoinsintoregister(unittest.TestCase):
    """Seeing if adding a list of coins correctly adds to register"""

    def setUp(self):

        self.soda_machine = SodaMachine()

    def test_deposit_coins_into_register(self):
        """Passing in 4 coins and seeing if register goes up by four"""
        my_coins = [Penny(), Dime(), Nickel(), Quarter()]
        self.soda_machine.deposit_coins_into_register(my_coins)
        self.assertEqual(len(self.soda_machine.register), 92)

if __name__ == '__main__':
    unittest.main()