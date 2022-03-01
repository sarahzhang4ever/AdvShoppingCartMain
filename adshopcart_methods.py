import datetime
import sys
import adshopcart_locators as locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from time import sleep

s = Service('chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Test of ASC website started at {datetime.datetime.now()}')

    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the ASC website
    driver.get(locators.advantage_shopping_cart_url)

    # Three ways to indicate non-breaking space in code as follows.
    # if driver.current_url == locators.advantage_shopping_cart_url and driver.title == ' Advantage Shopping':
    # if driver.current_url == locators.advantage_shopping_cart_url and driver.title == '\xa0Advantage Shopping':
    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == '\u00A0Advantage Shopping':
        print(f'We are at ASC homepage -- {driver.current_url}. The title of ASC homepage -- {driver.title}')
    else:
        print(f"Fail to navigate to homepage of ASC. Please check your code. ")


def tearDown():
    if driver is not None:
        print(f'Test of ASC website completed at {datetime.datetime.now()}')
        driver.close()
        driver.quit()


def register_new_account():
    assert driver is not None
    assert driver.current_url == locators.advantage_shopping_cart_url
    assert driver.find_element(By.ID, "hrefUserIcon").is_displayed()
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(4)
    driver.find_element(By.LINK_TEXT, "CREATE NEW ACCOUNT").click()
    sleep(0.25)
    driver.find_element(By.XPATH, "//input[@name='usernameRegisterPage']").send_keys(locators.user_name)
    driver.find_element(By.XPATH, "//input[@name='emailRegisterPage']").send_keys(locators.email)
    driver.find_element(By.XPATH, "//input[@name='passwordRegisterPage']").send_keys(locators.password)
    driver.find_element(By.XPATH, "//input[@name='confirm_passwordRegisterPage']").send_keys(locators.password)

    driver.find_element(By.XPATH, "//input[@name='first_nameRegisterPage']").send_keys(locators.first_name)
    driver.find_element(By.XPATH, "//input[@name='last_nameRegisterPage']").send_keys(locators.last_name)
    driver.find_element(By.XPATH, "//input[@name='phone_numberRegisterPage']").send_keys(locators.phone_number)

    Select(driver.find_element(By.XPATH, "//select[@name='countryListboxRegisterPage']")).select_by_visible_text("Canada")
    driver.find_element(By.XPATH, "//input[@name='cityRegisterPage']").send_keys(locators.city)
    driver.find_element(By.XPATH, "//input[@name='addressRegisterPage']").send_keys(locators.street_address)
    driver.find_element(By.XPATH, "//input[@name='state_/_province_/_regionRegisterPage']").send_keys(locators.province)
    driver.find_element(By.XPATH, "//input[@name='postal_codeRegisterPage']").send_keys(locators.postal_code)

    sleep(0.5)
    if not driver.find_element(By.XPATH, "//input[@name='i_agree']").is_selected():
        assert not driver.find_element(By.ID, "register_btnundefined").is_enabled()
        driver.find_element(By.XPATH, "//input[@name='i_agree']").click()

    driver.find_element(By.ID, "register_btnundefined").click()
    sleep(1)
    print(f"-----Create new user account passed-----. Username created: {locators.user_name}")


def check_new_user_info():
    # check my account for user_name.
    assert driver.find_element(By.XPATH, f"//span[text()='{locators.user_name}']") is not None
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(0.25)
    element = driver.find_element(By.XPATH, "//label[contains(., 'My account')]")
    driver.execute_script("arguments[0].click();", element)
    sleep(1)
    assert driver.find_element(By.XPATH, f"//label[contains(., '{locators.full_name}')]").is_displayed()
    assert driver.find_element(By.XPATH, f"//h3[contains(., 'Account details')]/../div/div/label[contains(., '{locators.full_name}')]").is_displayed()
    print(f"My account page is good with right full name displayed: {locators.full_name}")

    # check my order is empty
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(0.25)
    element = driver.find_element(By.XPATH, "//label[contains(., 'My orders')]")
    driver.execute_script("arguments[0].click();", element)
    assert driver.find_element(By.XPATH, "//label[text()=' - No orders - ']").is_displayed()
    print(f"My orders page is good with no order. Username: {locators.user_name}")

    print(f"-----Check new user account and order page passed----- Username: {locators.user_name}")


def sign_out():
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(0.25)
    element = driver.find_element(By.XPATH, "//label[contains(., 'Sign out')]")
    driver.execute_script("arguments[0].click();", element)
    sleep(3)
    print(f"-----Sign out passed----- from username: {locators.user_name}")


def sign_in_with_right_credentials(username, password):
    assert driver is not None
    assert driver.find_element(By.ID, "hrefUserIcon").is_displayed()
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    assert driver.find_element(By.XPATH, f"//span[text()='{username}']") is not None
    print(f"-----Sign in passed----- username: {username}")


def sign_in_with_wrong_credentials(username, password):
    assert driver is not None
    assert driver.find_element(By.ID, "hrefUserIcon").is_displayed()
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.ID, "sign_in_btnundefined").click()
    assert driver.find_element(By.XPATH, "//label[text()='Incorrect user name or password.']") is not None
    print(f"-----Sign in with wrong credential passed----- wrong credentials : {username}")


def delete_account():
    driver.find_element(By.ID, "hrefUserIcon").click()
    sleep(0.25)
    element = driver.find_element(By.XPATH, "//label[contains(., 'My account')]")
    driver.execute_script("arguments[0].click();", element)
    sleep(0.25)
    driver.find_element(By.XPATH, "//button[contains(., 'Delete Account')]").click()
    sleep(5)
    # driver.find_element(By.XPATH, "//div[text()='YES']").click()
    driver.find_element(By.XPATH, "//div[@class='deletePopupBtn deleteRed']").click()
    sleep(6)
    print(f"-----Delete user account passed----- deleted user account : {locators.user_name}")


def log_fake_data():
    old_instance = sys.stdout
    log_file = open('message.log', 'w')  # 'a'
    sys.stdout = log_file

    print(f"----------Fake user data------------")
    print(f"user_name: {locators.user_name}")
    print(f"password: {locators.password}")
    print(f"email: {locators.email}")
    print(f"----------------------------------")

    print(f"first_name: {locators.first_name}")
    print(f"last_name: {locators.last_name}")
    print(f"full_name: {locators.full_name}")
    print(f"phone_number: {locators.phone_number}")
    print(f"----------------------------------")

    print(f"country: {locators.country}")
    print(f"city: {locators.city}")
    print(f"street_address: {locators.street_address}")
    print(f"state: {locators.province}")
    print(f"postal_code: {locators.postal_code}")
    print(f"----------------------------------")

    sys.stdout = old_instance
    log_file.close()
