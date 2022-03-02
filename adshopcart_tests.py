import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdShopCartAppPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_case_a_homepage_functionality():
        methods.setUp()

        methods.check_categories()
        methods.check_top_navi_menu()
        methods.check_main_logo()
        methods.check_contact_form()

    @staticmethod
    def test_case_b_register_sign_in_out_delete():
        methods.log_fake_data()
        methods.register_new_account()
        methods.check_new_user_info()
        methods.sign_out()
        methods.sign_in_with_right_credentials(locators.user_name, locators.password)
        methods.delete_account()
        methods.sign_in_with_wrong_credentials(locators.user_name, locators.password)

        methods.tearDown()

