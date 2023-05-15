import unittest
import time
import login
from selenium import webdriver
from selenium.webdriver.common.by import By


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


class TestAssurance(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addCompanie(self):
        driver = self.driver
        login.test_login(driver)
    #     add companie

        assurance = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/section/a[7]")
        assurance.click()
        time.sleep(15)

        ajouter = driver.find_element(By.LINK_TEXT, "Ajouter une Compagnie")
        ajouter.click()
        time.sleep(5)

        name = driver.find_element(By.NAME, "nom")
        typing(name, "Assurance1")
        time.sleep(2)

        email = driver.find_element(By.NAME, "email")
        typing(email, "assurance1@gmail.com")
        time.sleep(2)

        telephone = driver.find_element(By.NAME, "telephone")
        typing(telephone, "+237678978765")
        time.sleep(2)

        address = driver.find_element(By.NAME, "adresse")
        typing(address, "Yaounde, Cameroon")
        time.sleep(2)

        psswd = driver.find_element(By.NAME, "password")
        typing(psswd, "Assurance1_")
        time.sleep(1)

        con_psswd = driver.find_element(By.NAME, "cpassword")
        typing(con_psswd, "Assurance1_")
        time.sleep(2)

        create = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-main")
        create.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
