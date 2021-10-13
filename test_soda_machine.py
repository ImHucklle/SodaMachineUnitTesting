import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """tests that register list holds 88 coins"""

    def setUp(self):
        """Sets up testing environment """
        self.soda_machine = SodaMachine()

    def test_register_list(self):
        """Checking to see if list length is 88"""
        check_register = self.soda_machine.fill_register(range())
        self.assertEqual(self.check_register.len(88))

if __name__ == '__main__':
    unittest.main()