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

    def test_coin_type(self):
        """Checking each coin type can be returned from register"""
        

if __name__ == '__main__':
    unittest.main()