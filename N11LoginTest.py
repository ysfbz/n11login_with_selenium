import unittest
from selenium import webdriver
import time 

class LoginN11(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.n11.com")
        self.driver.get_cookies()


    def test_n11_login(self):
        self.driver.find_element_by_class_name("btnHolder").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("btnSignIn").click()
        time.sleep(0)
        self.driver.find_element_by_name("email").send_keys("sendyour@email.com")
        self.driver.find_element_by_name("password").send_keys("yourpassword")
        time.sleep(1)
        self.driver.find_element_by_id("loginButton").click()
        time.sleep(60)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
