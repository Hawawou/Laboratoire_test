import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class AddPatient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_patient(self):
        driver = self.driver
        driver.get("http://51.38.42.38:3016/")

        #         Log in to acceuil
        name = driver.find_element(By.NAME, "email")
        typing(name, "christopherosei@gmail.com")
        time.sleep(1)

        password = driver.find_element(By.NAME, "password")
        typing(password, "Osei@123.")
        time.sleep(1)

        button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-main")
        button.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
