import unittest
import time
import login

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestFamilleExamen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_famille(self):
        driver = self.driver
        login.test_login(driver)

        # View and create famille d'examen
        examens = driver.find_element(By.LINK_TEXT, 'Famille examens')
        examens.click()
        time.sleep(10)

        ajouter = driver.find_element(By.LINK_TEXT, "Ajouter Une Famille d'Examen")
        ajouter.click()
        time.sleep(3)

        nom = driver.find_element(By.NAME, 'nomfamille')
        typing(nom, 'Virus')
        time.sleep(1)

        add = driver.find_element(By.CSS_SELECTOR, 'div.btn-group')
        add.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
