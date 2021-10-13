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
        

if __name__ == '__main__':
    unittest.main()


       
