import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_employee(self):
        driver = self.driver
        driver.get("http://51.38.42.38:3016/")

        username = driver.find_element(By.NAME, "email")
        typing(username, "laurine.tcheudje@abyster.com")
        time.sleep(1)

        pwd = driver.find_element(By.NAME, "password")
        # open pwd file
        with open('pwd.txt', 'r') as myfile:
            password = myfile.read().replace('\n', '')
        typing(pwd, password)
        time.sleep(1)

        button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-main")
        button.click()
        time.sleep(10)

# Create emloyee
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
        typing(email, "johndoe2@gmail.com")
        time.sleep(1)

        phone = driver.find_element(By.NAME, "telephone")
        typing(phone, "+237672345892")
        time.sleep(1)

        agence = Select(driver.find_element(By.NAME, 'matricule_ag'))
        agence.select_by_visible_text("Agence 2")
        time.sleep(1)

        # service = Select(driver.find_element(By.NAME, 'matricule_serv'))
        # service.select_by_visible_text("biologiste")
        # time.sleep(1)

        psswd = driver.find_element(By.NAME, "password")
        # open pwd file
        with open('pwd_create.txt', 'r') as myfile:
            password = myfile.read().replace('\n', '')
        typing(psswd, password)
        time.sleep(1)

        psswd_confirm = driver.find_element(By.NAME, "cpassword")
        # open pwd file
        with open('pwd_create.txt', 'r') as myfile:
            password = myfile.read().replace('\n', '')
        typing(psswd_confirm, password)
        time.sleep(1)

        create = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        create.click()

        time.sleep(5)

        def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()

    