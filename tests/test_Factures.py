import unittest
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By

def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)


# This test prints a bill
class TestFacture(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_login(self):
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
        time.sleep(5)

        facture = driver.find_element(By.LINK_TEXT, 'Factures')
        facture.click()
        time.sleep(10)

        print = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]/div/a')
        print.click()
        time.sleep(5)

        imprimer = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-mains')
        imprimer.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
