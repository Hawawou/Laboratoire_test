import unittest
import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)

class TestAgence(unittest.TestCase):
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

        agence = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/section/a[3]')
        agence.click()
        time.sleep(5)

# add agency
        add_agence = driver.find_element(By.CLASS_NAME, 'add-agency-item')
        add_agence.click
        time.sleep(10)

        nom_agence = driver.find_element(By.NAME, 'nom')
        typing(nom_agence, 'Agency3')
        time.sleep(1)

        telephone = driver.find_element(By.NAME, 'telephone')
        typing(telephone, '+237690234589')
        time.sleep(1)

        email = driver.find_element(By.NAME, 'email')
        typing(email, 'agency3@gmail.com')
        time.sleep(1)

        pays = Select(driver.find_element(By.NAME, 'pays'))
        pays.select_by_visible_text("Cameroun")
        time.sleep(1)
        
        ville = driver.find_element(By.NAME, 'ville')
        typing(ville, 'Yaounde')
        time.sleep(1)

        region = driver.find_element(By.NAME, 'region')
        typing(region, 'Yaounde')
        time.sleep(1)

        create = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-main')
        create.click(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
