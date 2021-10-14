import unittest
import user_interface



class TestGetWalletCoin(unittest.TestCase):
    """Test for user_interface_module  """

    def test_validate_main_menu(self):
        """Test Main Menu to ensure Tuple is returned"""
        #self.user_interface = user_interface()

        return_tuple = user_interface.validate_main_menu 
        
        print(return_tuple)
        self.assertEqual(return_tuple,[False,None])


    