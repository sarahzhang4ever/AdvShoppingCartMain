import unittest
import adshopcart_methods as methods


class AdShopCartAppPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_home_page():
        methods.setUp()
        methods.tearDown()
