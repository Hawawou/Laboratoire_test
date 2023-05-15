import time
import utills

from selenium import webdriver
from selenium.webdriver.common.by import By


typing = utills.typing()


def setUp(self):
    self.driver = webdriver.Chrome()


def test_patient(driver):
    driver.get("http://51.38.42.38:3017/")
    driver.maximize_window()

    connect = driver.find_element(By.LINK_TEXT, "Connectez-vous")
    connect.click()
    time.sleep(3)

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
    time.sleep(15)



