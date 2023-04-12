import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('–headless')
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")


def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)
class LaboratoireTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)

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

        time.sleep(30)

    # def test_Patients(self):
    #     driver = self.driver
    #     button_patient = driver.find_element(By.NAME, "Patients")
    #     button_patient.click

    # def test_addUser(self):
    #     driver = self.driver
    #     employees = driver.find_element(By.XPATH, "//div[@id='root']/div[@class='kt-quick-panel--right kt-demo-panel--right kt-offcanvas-panel--right kt-header--fixed kt-header-mobile--fixed kt-subheader--enabled kt-subheader--transparent kt-aside--enabled kt-aside--fixed kt-page--loading']/div[@class='page-wrapper']/div[@class='sidebar-container']/div[@class='sidebar open']/section[@class='nav-links nav-links-mobile']/a[@class='nav-link'][1]/div[@class='link-text']")
    #     employees.click()
        
    #     fname = driver.find_element(By.NAME, "nom")
    #     typing(fname, "John")
    #     time.sleep(1)

    #     lname = driver.find_element(By.NAME, "prenom")
    #     typing(lname, "Doe")
    #     time.sleep(1)

    #     email = driver.find_element(By.NAME, "email")
    #     typing(email, "johndoe2@gmail.com")
    #     time.sleep()

    #     phone = driver.find_element(By.NAME, "telephone")
    #     typing(phone, "672345892")
    #     time.sleep()

      
        driver.close()
    

if __name__ == "__main__":
    unittest.main()
    print("All tests passed")

