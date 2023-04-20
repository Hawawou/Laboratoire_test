import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from login_test.testLogin import TestLogin


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)

class LaboratoireTestPatient(unittest.TestCase): 
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_patient(self):
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

# Click on patient
        patient = driver.find_element(By.LINK_TEXT, "Patients")
        patient.click()
        time.sleep(30)

        # view a patient
        view_patient = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/a')
        view_patient.click()
        time.sleep(1)

        print = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/div/div")
        print.click()
        time.sleep(20)

        imprimer = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/button') 
        imprimer.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main()
 

