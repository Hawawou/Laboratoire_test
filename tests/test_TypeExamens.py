import unittest
import time 
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

        button = driver.find_element(By.LINK_TEXT, 'Type examens')
        button.click()
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
