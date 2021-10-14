import unittest
from unittest.case import TestCase

import user_interface
from cans import Cola, OrangeSoda, RootBeer
from coins import Penny, Dime, Nickel, Quarter


class TestUser_Iterface(unittest.TestCase):
    """Testing the different methods in User interface file"""


    def test_validate_main_menu_one(self):
        """Test to see if input 1 is true to the function"""
        user_input_one = user_interface.validate_main_menu(1)
        self.assertTrue(user_input_one, (True, 1))

    def test_validate_main_menu_two(self):
        """Test to see if input 2 is true to the function"""
        user_input_two = user_interface.validate_main_menu(2)
        self.assertTrue(user_input_two, (True, 2))

    def test_validate_main_menu_three(self):
        """Test to see if input 3 is true to the function"""
        user_input_three = user_interface.validate_main_menu(3)
        self.assertTrue(user_input_three, (True, 3))

    def test_validate_main_menu_four(self):
        """Test to see if input 4 is true to the function"""
        user_input_four = user_interface.validate_main_menu(4)
        self.assertTrue(user_input_four, (True, 4))

    def test_validate_main_menu_five(self):
        """Test to see if input 5 is false to the function"""
        user_input_five = user_interface.validate_main_menu(5)
        self.assertTrue(user_input_five, (True, 5))

    
class TestTry_parse(unittest.TestCase):
    """Testing to see if try_parse method working"""

    def test_try_parse_int(self):
        """Test to see if number string changes to int"""
        returned_value = user_interface.try_parse_int('10')
        self.assertEqual(returned_value, 10)

    def test_try_parse_int_word(self):
        """Test to see if a word returns as a zero if it cant translate word to int"""
        returned_value = user_interface.try_parse_int('hello')
        self.assertEqual(returned_value, 0)

class Testget_unique_can_name(unittest.TestCase):
    """Testing the unique can name method"""

    def test_get_unique_can_names(self):
        """Test to see if adding multiple drink names to list and doesnt repeat a name"""
        my_cans = [Cola(), OrangeSoda(), RootBeer()]
        can_names = user_interface.get_unique_can_names(my_cans)
        self.assertEqual(len(can_names), 3)

    def test_get_unigue_names_no_list(self):
        """Testing to see if empty list is passed in then a empty list is returned"""
        my_list = []
        can_names = user_interface.get_unique_can_names(my_list)
        self.assertEqual(len(can_names), 0)


class test_display_payemnt_value(unittest.TestCase):
    """Testing the method display payment value"""

    def test_display_payment_value(self):
        """Testing to see if method i adding and returning the correct value"""
        my_coins = [Quarter(), Nickel(), Dime(), Penny()]
        my_purchase = user_interface.display_payment_value(my_coins)
        self.assertEqual(my_purchase, .41)

    def test_display_payment_value_no_list(self):
        """Testing to see if method i adding and returning the correct value"""
        my_coins = []
        my_purchase = user_interface.display_payment_value(my_coins)
        self.assertEqual(my_purchase, .00)

class Test_validate_coins_selection(unittest.TestCase):
    """Testing the method validte coins selection"""

    def test_validate_coin_selection_one(self):
        """Test to see if input 1 is true to the function"""
        user_input_one = user_interface.validate_coin_selection(1)
        self.assertTrue(user_input_one, (True, "Quarter"))
    
    def test_validate_coin_selection_two(self):
        """Test to see if input 2 is true to the function"""
        user_input_two = user_interface.validate_coin_selection(2)
        self.assertTrue(user_input_two, (True, "Dime"))

    def test_validate_coin_selection_three(self):
        """Test to see if input 3 is true to the function"""
        user_input_three = user_interface.validate_coin_selection(3)
        self.assertTrue(user_input_three, (True, "Nickel"))
    
    def test_validate_coin_selection_four(self):
        """Test to see if input 4 is true to the function"""
        user_input_four = user_interface.validate_coin_selection(4)
        self.assertTrue(user_input_four, (True, "Penny"))

    def test_validate_coin_selection_five(self):
        """Test to see if input 1 is true to the function"""
        user_input_five = user_interface.validate_coin_selection(5)
        self.assertTrue(user_input_five, (True, "Done"))

    def test_validate_coin_selection_seven(self):
        """Test to see if input 7 is true to the function"""
        user_input_seven = user_interface.validate_coin_selection(7)
        self.assertTrue(user_input_seven, (False, None))
    



if __name__ == '__main__':
    unittest.main()
