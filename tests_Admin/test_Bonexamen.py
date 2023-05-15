import unittest
import time
import login

from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestBonexamen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_bonexamen(self):
        driver = self.driver
        login.test_login(driver)

        # Bon d'examen
        patient = driver.find_element(By.LINK_TEXT, "Bon d'examens")
        patient.click()
        time.sleep(40)

        view = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a')
        view.click()

        back = driver.find_element(By.LINK_TEXT, "Retour aux bon d'examens")
        back.click()
        time.sleep(5)

        # imprimer
        imprimer = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/div/div/div")
        imprimer.click()
        time.sleep(5)

        imprime = driver.find_element(By.CSS_SELECTOR, "button.btn.tnm-main")
        imprime.click()
        time.sleep(5)

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
