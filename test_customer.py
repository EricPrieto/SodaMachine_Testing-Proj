import unittest
from cans import Cola, OrangeSoda, RootBeer
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
        """Pass in list of 3 coins, method should increase customer wallet list by 3"""
        list = [Quarter(), Dime(), Penny()]
        self.customer.add_coins_to_wallet(list)

        self.assertEqual(len(self.customer.wallet.money), 91)
      
    def test_can_pass_empty_list(self):
        """Pass in an empty list, method should not change lenth of money list"""
        list = []
        self.customer.add_coins_to_wallet(list)

        self.assertEqual(len(self.customer.wallet.money), 88)

class TestAddCanToBackPack(unittest.TestCase):
    """ Test for Customer's add_can_to_backpack """
   
    def setUp(self):
        self.customer = Customer()

    def test_pass_object_soda(self):
        """Pass in a Cola object, method should increase customers backpace list by 1"""
        list =[Cola()]
        self.customer.add_can_to_backpack(Cola())

        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)

    def test_pass_object_orangesoda(self):
        """Pass in Orange Soda object, method should increase customers backpace list by 1"""
        list =[OrangeSoda()]
        self.customer.add_can_to_backpack(OrangeSoda())

        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)

    def test_pass_object_rootbeer(self):
        """Pass in a Root Beer object, method should increase customers backpace list by 1"""
        list =[RootBeer()]
        self.customer.add_can_to_backpack(RootBeer())

        self.assertEqual(len(self.customer.backpack.purchased_cans), 1) 

   





if __name__ == '__main__':
    unittest.main()



