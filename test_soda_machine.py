import unittest
from soda_machine import SodaMachine

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

        






























if __name__ == '__main__':
    unittest.main()


       
