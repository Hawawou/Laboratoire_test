import unittest
import time
import login

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestModifFamille(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        login.test_login(driver)

        examens = driver.find_element(By.LINK_TEXT, 'Famille examens')
        examens.click()
        time.sleep(10)

        edit = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[6]/td[4]/div/a')
        edit.click()
        time.sleep(2)

        modif = driver.find_element(By.NAME, 'nomfamille')
        typing(modif, 'Covid')
        time.sleep(2)

        btn = driver.find_element(By.CSS_SELECTOR, 'div.btn-group')
        btn.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
