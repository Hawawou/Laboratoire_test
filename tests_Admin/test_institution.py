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


class TestInstitution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addInstitution(self):
        driver = self.driver
        login.test_login(driver)

        # institution
        institution = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/section/a[8]")
        institution.click()
        time.sleep(15)

        add = driver.find_element(By.LINK_TEXT, "Ajouter une Institution")
        add.click()
        time.sleep(5)

        #     ajouter une institution
        name = driver.find_element(By.NAME, "nom")
        typing(name, "Institution1")
        time.sleep(1)

        email = driver.find_element(By.NAME, "email")
        typing(email, "institution1@gmail.com")
        time.sleep(1)

        telephone = driver.find_element(By.NAME, "telephone")
        typing(telephone, "+237687976542")
        time.sleep(1)

        address = driver.find_element(By.NAME, "adresse")
        typing(address, "Yaounde, Cameroon")
        time.sleep(1)

        psswd = driver.find_element(By.NAME, "password")
        typing(psswd, "Institution1_")
        time.sleep(1)

        con_psswd = driver.find_element(By.NAME, "cpassword")
        typing(con_psswd, "Institution1_")
        time.sleep(1)

        create = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-main")
        create.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
