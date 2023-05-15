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


class TestPatient(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_patient(self):
        driver = self.driver
        login.test_login(driver)

        # Click on patient
        patient = driver.find_element(By.LINK_TEXT, "Patients")
        patient.click()
        time.sleep(30)

        # view a patient
        view_patient = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/a')
        view_patient.click()
        time.sleep(1)

        imprime = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/div/div")
        imprime.click()
        time.sleep(20)

        imprimer = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/button')
        imprimer.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
