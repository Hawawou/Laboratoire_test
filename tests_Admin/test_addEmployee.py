import time
import unittest
import HtmlTestRunner
import login
import utills

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


typing = utills.typing()


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_employee(self):
        driver = self.driver
        login.test_login(driver)

        # Create employee
        employees = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/section/a[2]")
        employees.click()
        time.sleep(1)

        add_employee = driver.find_element(By.LINK_TEXT, 'Ajouter un employé')
        add_employee.click()

        fname = driver.find_element(By.NAME, "nom")
        typing(fname, "John")
        time.sleep(1)

        lname = driver.find_element(By.NAME, "prenom")
        typing(lname, "Doe")
        time.sleep(1)

        email = driver.find_element(By.NAME, "email")
        typing(email, "johndoe3@gmail.com")
        time.sleep(1)

        phone = driver.find_element(By.NAME, "telephone")
        typing(phone, "+237672365892")
        time.sleep(1)

        agence = Select(driver.find_element(By.NAME, 'matricule_ag'))
        agence.select_by_visible_text("Agence 2")
        time.sleep(1)

        # service = Select(driver.find_element(By.NAME, 'matricule_serv'))
        # service.select_by_visible_text("biologiste")
        # time.sleep(1)

        psswd = driver.find_element(By.NAME, "password")
        # open pwd file
        typing(psswd, "Johndoe@")
        time.sleep(1)

        psswd_confirm = driver.find_element(By.NAME, "cpassword")
        # open pwd file
        typing(psswd_confirm, "Johndoe@")
        time.sleep(1)

        create = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        create.click()

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Report'))
