import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators

s = Service('chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Test of AWS website started at {datetime.datetime.now()}')

    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the AWS website
    driver.get(locators.advantage_shopping_cart_url)

    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == ' Advantage Shopping':
        print(f'We are at AWS homepage -- {driver.current_url}. The title of AWS homepage -- {driver.title}')
    else:
        print(f"Fail to navigate to homepage of AWS. Please check your code. ")


def tearDown():
    if driver is not None:
        print(f'Test of AWS website completed at {datetime.datetime.now()}')
        driver.close()
        driver.quit()




