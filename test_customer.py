import unittest
from coins import Quarter
from customer import Customer

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

#class TestAddCoinsToWallet(unittest.TestCase):
 #   """ Test for Customer's add_coins_to_wallet """



if __name__ == '__main__':
    unittest.main()



