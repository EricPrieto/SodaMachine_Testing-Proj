import unittest
from coins import Coin, Dime, Penny, Quarter
from customer import Customer
from user_interface import coin_selection

class TestGetWalletCoin(unittest.TestCase):
    """ Test for Customer's get_wallet_coin """

    def setUp(self):
        self.customer = Customer()

    def test_can_return_penny(self):
        """Pass in Penny, method should return a Penny instance"""
        return_coin = self.customer.get_wallet_coin("Penny")

        self.assertEqual(return_coin.value, .01)

    def test_can_return_nickel(self):
        """Pass in Nickel, method should return a Nickel instance"""
        return_coin = self.customer.get_wallet_coin("Nickel")

        self.assertEqual(return_coin.value, .05)
    
    def test_can_return_dime(self):
        """Pass in Dime, method should return a Dime instance"""
        return_coin = self.customer.get_wallet_coin("Dime")

        self.assertEqual(return_coin.value, .10)

    def test_can_return_quarter(self):
        """Pass in Quarter, method should return a Quarter instance"""
        return_coin = self.customer.get_wallet_coin("Quarter")

        self.assertEqual(return_coin.value, .25)

    def test_string_invaild(self):
        """Pass a String, method should return None"""
        return_none = self.customer.get_wallet_coin("None")

        self.assertIsNone(return_none)

class TestAddCoinsToWallet(unittest.TestCase):
    """ Test for Customer's add_coins_to_wallet """
   
    def setUp(self):
        self.customer = Customer()

    def test_can_pass_list(self):
        """Pass in list of 3 coins, method should return customer wallet list up by 3"""
        list = [Quarter(), Dime(), Penny()]
        self.customer.add_coins_to_wallet(list)

        self.assertEqual(len(self.customer.wallet.money), 91)
        # for item in self.add_coins_to_wallet:
        #     print(len(item))
        # self.assertEqual()

    def test_can_pass_empty_list(self):
        """Pass in list of 3 coins, method should return customer wallet list up by 3"""
        self.add_coins_to_wallet = []
        for item in self.add_coins_to_wallet:
            if len(item) == 0:
                print("Len remained the same")




if __name__ == '__main__':
    unittest.main()



