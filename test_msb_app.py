import unittest
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_driver_factory import WebDriverFactory
from web_driver_factory import Platform

logging.basicConfig(level=logging.INFO)

WAIT_TIMEOUT = 5


class MsbAppTests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        log = logging.getLogger('setUp')
        cls.driver = WebDriverFactory.create(Platform.NW)
        log.info('MSB App started')

    @classmethod
    def tearDownClass(cls):
        log = logging.getLogger('tearDown')
        cls.driver.quit()
        log.info('MSB App terminated')

    def test_profile_name(self):
        log = logging.getLogger('test_profile_name')

        # header_button = cls.driver.find_element_by_xpath("//android.widget.Button[@resource-id='header']")

        # header_button = next(f for f in buttons if f.get_attribute("resource-id") == "header")

        header_button = WebDriverWait(MsbAppTests.driver, timeout=WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.ID, "header")))

        # header_button = cls.driver.find_element_by_id("header")
        profile_name = header_button.text
        self.assertEqual(profile_name, "Default", "Profile name must be 'Default'")
        log.info('profile name ok')

    def test_set_login_data(self):
        log = logging.getLogger('test_set_login_data')

        user_input = MsbAppTests.driver.find_element_by_id("userInput")
        user_input.send_keys("ABC")

        password_input = MsbAppTests.driver.find_element_by_id("passwordInput")
        password_input.send_keys("password")

        login_application_input = MsbAppTests.driver.find_element_by_id("loginApplicationInput")
        login_application_input.send_keys("QS1")

        user = user_input.get_attribute('value')
        self.assertEqual(user, "ABC", "User name must be 'ABC'")

        password = password_input.get_attribute('value')
        self.assertEqual(password, "password", "Password name must be 'password'")

        application_name = login_application_input.get_attribute('value')
        self.assertEqual(application_name, "QS1", "Application name must be 'QS1'")

        log.info('login data set')

    def test_setting(self):
        log = logging.getLogger('test_setting')

        settings_button = MsbAppTests.driver.find_element_by_id("settingsButton")
        settings_button.click()

        time.sleep(1)

        cancel_button = MsbAppTests.driver.find_element_by_id("cancelButton")
        MsbAppTests.driver.execute_script("arguments[0].scrollIntoView(true);", cancel_button)
        time.sleep(1)
        cancel_button.click()

        log.info('settings')


if __name__ == '__main__':
    unittest.main()
