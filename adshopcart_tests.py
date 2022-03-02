import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdShopCartAppPositiveTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        methods.setUp()

    @classmethod
    def tearDownClass(cls):
        methods.tearDown()

    def setUp(self):
        print('\n===== Start of test:', self.shortDescription())

    def tearDown(self):
        print('===== End of test:', self.shortDescription())

    @staticmethod
    def test_case_a_homepage_functionality():
        """Home Page Functionality"""
        methods.check_categories()
        methods.check_top_navi_menu()
        methods.check_main_logo()
        methods.check_contact_form()

    @staticmethod
    def test_case_b_register_sign_in_out_delete():
        """Register-Sign-in-Sign-out-Delete"""
        methods.log_fake_data()
        methods.register_new_account()
        methods.check_new_user_info()
        methods.sign_out()
        methods.sign_in_with_right_credentials(locators.user_name, locators.password)
        methods.delete_account()
        methods.sign_in_with_wrong_credentials(locators.user_name, locators.password)

