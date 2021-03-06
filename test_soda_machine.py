from typing import List
import unittest
from unittest import result
from cans import Can, Cola, OrangeSoda, RootBeer
from coins import Coin, Dime, Penny, Nickel, Quarter
from soda_machine import SodaMachine
from user_interface import coin_selection, soda_selection

class TestFillRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()


    def test_fill_register(self):
        self.assertEqual(88, len(self.soda_machine.register))

class TestFillInventory(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_fill_inventory(self):
        self.assertEqual(30, len(self.soda_machine.inventory))

class TestGetCoinFromRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_nickel_from_register(self):
        return_coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(return_coin.value, .05)

    def test_dime_from_register(self):
        return_coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(return_coin.value, .10)

    def test_penny_from_register(self):
        return_coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(return_coin.value, .01) 
    
    def test_quarter_from_register(self):
        return_coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(return_coin.value, .25)

    def test_string_invalid(self):
        return_none = self.soda_machine.get_coin_from_register("None")
       
        self.assertIsNone(return_none)

class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_register_has_nickel(self):
        return_coin = self.soda_machine.register_has_coin("Nickel")
        self.assertEqual(return_coin, True)

    def test_register_has_dime(self):
        return_coin = self.soda_machine.register_has_coin("Dime")
        self.assertEqual(return_coin, True)
    
    def test_register_has_penny(self):
        return_coin = self.soda_machine.register_has_coin("Penny")
        self.assertEqual(return_coin, True)
    
    def test_register_has_quarter(self):
        return_coin = self.soda_machine.register_has_coin("Quarter")
        self.assertEqual(return_coin, True)

    def test_non_valid(self):
        return_none = self.soda_machine.register_has_coin("None")
        self.assertFalse(return_none)
        
class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_with_higher_payment(self):
        return_a = self.soda_machine.determine_change_value(.80,0)
        return_b = self.soda_machine.determine_change_value(0,.60)
        self.assertGreater(return_a,return_b) 

    def test_with_soda_price_higher(self):
        return_a = self.soda_machine.determine_change_value(0,.60)
        return_b = self.soda_machine.determine_change_value(.30,0)
        self.assertLess (return_a,return_b)

    def test_soda_equal_payment(self):
        return_a = self.soda_machine.determine_change_value(0,0)
        return_b = self.soda_machine.determine_change_value(0,0)
        self.assertEqual(return_a,return_b)   

class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()
       
    def test_coin_list_value(self):
        List = [Quarter(), Dime(), Nickel(), Penny()]
        
        result = self.soda_machine.calculate_coin_value(List)              
        print(result)
        self.assertEqual(result, 0.41)

    def test_coin_list_emtpy(self):
        List = []

        result = self.soda_machine.calculate_coin_value(List)              
        print(result)
        self.assertEqual(result, 0.)
        
class GetInventorySoda(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_inventory_cola(self):
        return_soda_name = self.soda_machine.get_inventory_soda("Cola")
        self.assertIsInstance(return_soda_name, Cola)

    def test_inventory_cola(self):
        return_soda_name = self.soda_machine.get_inventory_soda("OrangeSoda")
        self.assertIsInstance(return_soda_name, OrangeSoda)

    def test_inventory_cola(self):
        return_soda_name = self.soda_machine.get_inventory_soda("RootBeer")
        self.assertIsInstance(return_soda_name, RootBeer)

    def test_inventory_cola(self):
        return_soda_name = self.soda_machine.get_inventory_soda("MountianDew")
        self.assertEqual(return_soda_name, None)


class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_return_inventory(self):
        cola = Cola()
        self.soda_machine.return_inventory(cola)
        self.assertEqual(31, len(self.soda_machine.inventory))

class TestDepositCoinsIntoRegister(unittest.TestCase):
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_deposit_list(self):
        list = [Quarter(), Dime(), Penny(), Nickel()]
        self.soda_machine.deposit_coins_into_register(list)
        self.assertEqual(len(self.soda_machine.register), 92) 
        









if __name__ == '__main__':
    unittest.main()


       
