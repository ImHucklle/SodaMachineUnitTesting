import unittest 
from customer import Customer 
from wallet import Wallet 
from coins import Coin, Dime, Penny, Quarter
from backpack import Backpack
from cans import Can, RootBeer

class TestGetWalletCoin(unittest.TestCase):
    """Test for customers get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter' method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_can_return_dime(self):
        """Pass in 'Dime' method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel' method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_can_return_penny(self):
        """Pass in 'Penny' method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_can_return_none(self):
        """Pass in a string that is non a valued coin to return none"""
        returned_none = self.customer.get_wallet_coin('none')
        self.assertIsNone(returned_none)
        


class TestAddWalletCoins(unittest.TestCase):  
    """Testing the add_coins_to_wallet method""" 

    def  setUp(self):
        self.customer = Customer()
        self.coin_list = [Dime(), Quarter(), Penny()]

    def test_adding_wallet(self):
        """Pass in coins to wallet and make sure wallet index went up the correct amount"""
        self.customer.add_coins_to_wallet(self.coin_list)
        self.assertEqual(len(self.customer.wallet.money), 91)
    


class TestAddToBackPack(unittest.TestCase):
    """To test if length of backpack goes up when a item is added"""

    def setUp(self):
        self.customer = Customer()
        self.can = Can(RootBeer, .50)

    def test_add_can_to_backpack(self):
        
        self.customer.add_can_to_backpack(self.can)
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)


if __name__ == '__main__':
    unittest.main()

