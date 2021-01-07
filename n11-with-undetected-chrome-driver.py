import undetected_chromedriver as uc
uc.install()
import unittest
import time 


from selenium.webdriver import Chrome
driver = Chrome()
driver.get('http://www.n11.com')
driver.find_element_by_class_name("btnHolder").click()
time.sleep(1)
driver.find_element_by_class_name("btnSignIn").click()
time.sleep(0)
driver.find_element_by_name("email").send_keys("yusufbuzrul@gmail.com")
driver.find_element_by_name("password").send_keys("milan1905")
time.sleep(1)
driver.find_element_by_id("loginButton").click()
time.sleep(60)
