import unittest
import time
import login

from selenium import webdriver 
from selenium.webdriver.common.by import By

def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_login(self):
        driver = self.driver
        login.test_login(driver)

        # Tubes
        tubes = driver.find_element(By.LINK_TEXT, 'Tubes')
        tubes.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
