import unittest

import user_interface


class TestUser_Iterface(unittest.TestCase):
    """Testing the different methods in User interface file"""


    def test_validate_main_menu(self):
        user_input = 1
        user_interface.validate_main_menu(user_input)
        self.assertEqual((user_input), (True, 1))



if __name__ == '__main__':
    unittest.main()
