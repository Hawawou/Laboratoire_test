import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1280x800")
# options.add_argument("–disable-dev-shm-usage")
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--no-sandbox")
# options.binary_location("/usr/bin/google-chrome")


delay = 10 #sec

def typing(element, text):
    for i in text:
        element.send_keys(i)
        time.sleep(0.3)
class LaboratoireTest(unittest.TestCase):
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

        print("Test completed")

    # def test_Patients(self):
    #     driver = self.driver
    #     button_patient = driver.find_elements(By.CLASS_NAME, ".header-link-link")
    #     if len(button_patient) > 0:
    #         button_patient[0].click()      

    # def test_addEmployee(self):


    #     driver = self.driver
    #     employees = driver.find_element(By.CSS_SELECTOR, "Employés")
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

      
    #     driver.close()
    

if __name__ == "__main__":
    unittest.main()
    print("All tests passed")

