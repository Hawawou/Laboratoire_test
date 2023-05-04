import unittest
import time 
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

        examen = driver.find_element(By.LINK_TEXT, 'Examens')
        examen.click()
        time.sleep(3)

        ajouter = driver.find_element(By.CSS_SELECTOR, 'button.btn-link-green')
        ajouter.click()
        time.sleep(3)

        type = Select(driver.find_element(By.NAME, 'matriculefam'))
        type.select_by_visible_text("SANG")
        time.sleep(1)

        nom_examen = driver.find_element(By.NAME, 'nom')
        typing(nom_examen, 'typhoid')
        time.sleep(1)

        prix = driver.find_element(By.NAME, 'prix')
        typing(prix, '5000')
        time.sleep(1)

        tube = Select(driver.find_element(By.NAME, 'verre'))
        tube.select_by_visible_text('Tube Standard')
        time.sleep(1)
        
        add = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        add.click()
        time.sleep(3)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
