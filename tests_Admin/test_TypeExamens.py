import unittest
import time
import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestTypeExamens(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        login.test_login(driver)

        examens = driver.find_element(By.LINK_TEXT, 'Type examens')
        examens.click()
        time.sleep(4)

        ajouter = driver.find_element(By.CSS_SELECTOR, 'a.btn-link-green')
        ajouter.click()
        time.sleep(4)

        nom = Select(driver.find_element(By.NAME, 'codebfamille'))
        nom.select_by_visible_text("COVID-19")
        time.sleep(1)

        nom_type = driver.find_element(By.NAME, 'nom')
        typing(nom_type, 'virus')
        time.sleep(2)

        ajouter = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        ajouter.click
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
