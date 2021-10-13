import unittest

from user_interface import 

class TestUser_Iterface(unittest.TestCase):
    """Testing the different methods in User interface file"""


    def test_validate_main_menu(user_imput):
        user_imput = 1
        assertEqual(validate_main_menu(), True, 1)



if __name__ == '__main__':
    unittest.main()
