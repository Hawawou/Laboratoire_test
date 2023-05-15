import unittest
import time
import login

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


# This test prints a bill
class TestFacture(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_facture(self):
        driver = self.driver
        login.test_login(driver)

        facture = driver.find_element(By.LINK_TEXT, 'Factures')
        facture.click()
        time.sleep(15)

        print_fac = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]/div/a')
        print_fac.click()
        time.sleep(5)

        imprimer = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-mains')
        imprimer.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
