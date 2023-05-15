import unittest
import time
import login

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestUnite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_unit(self):
        driver = self.driver
        login.test_login()

        # ajouter une unite de mesure
        unite = driver.find_element(By.LINK_TEXT, "Unités")
        unite.click()
        time.sleep(10)

        add = driver.find_element(By.LINK_TEXT, 'Ajouter une unité')
        add.click()
        time.sleep(5)

        nom = driver.find_element(By.NAME, 'nomunite')
        typing(nom, 'ml/J')

        bttn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        bttn.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
