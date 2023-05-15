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
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_examen(self):
        driver = self.driver
        login.test_login(driver)

        # examen
        examen = driver.find_element(By.LINK_TEXT, 'Examens')
        examen.click()
        time.sleep(3)

        ajouter = driver.find_element(By.LINK_TEXT, 'Ajouter examen')
        ajouter.click()
        time.sleep(3)

        types = Select(driver.find_element(By.NAME, 'matriculefam'))
        types.select_by_visible_text("SANG")
        time.sleep(1)

        nom_examen = driver.find_element(By.NAME, 'nom')
        typing(nom_examen, 'typhoid')
        time.sleep(1)

        prix = driver.find_element(By.NAME, 'prix')
        typing(prix, '5000')
        time.sleep(3)

        tube = Select(driver.find_element(By.NAME, 'verre'))
        tube.select_by_visible_text('Tube EDTA')
        time.sleep(1)

        add = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        add.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
