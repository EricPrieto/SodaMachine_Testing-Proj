import unittest
import user_interface



class TestGetWalletCoin(unittest.TestCase):
    """Test for user_interface_module  """

    def test_validate_main_menu_one(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu(1)
        
        print(return_tuple)
        self.assertEqual(return_tuple,(False,None))

    def test_validate_main_menu_two(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu(2)
        
        print(return_tuple)
        self.assertEqual(return_tuple,(False,None))


    def test_validate_main_menu_three(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu(3)
        
        print(return_tuple)
        self.assertEqual(return_tuple,(False,None))

    def test_validate_main_menu_four(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu(4)
        
        print(return_tuple)
        self.assertEqual(return_tuple,(False,None))

    def test_validate_main_menu_false(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu(5)
        
        print(return_tuple)
        self.assertEqual(return_tuple,(False,None))


if __name__ == '__main__':
    unittest.main()