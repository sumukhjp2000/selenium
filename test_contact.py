import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class contact(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(r'C:\Users\sumuk\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://enigmatic-retreat-90606.herokuapp.com/')
        time.sleep(3)

    def test_contactsuccess(self):
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[2]/span').click()
        time.sleep(3)
        self.driver.find_element_by_name("name").send_keys('John')
        self.driver.find_element_by_name("email").send_keys('john@yahoo.com')
        self.driver.find_element_by_name("subject").send_keys('Product enquiry')
        self.driver.find_element_by_name("message").send_keys('Are the size 9 adidas shoes available?')
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,400)")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/form/div/div[5]/button').click()


    def test_contactmissing(self):
        time.sleep(4)
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[2]/span').click()
        time.sleep(3)
        self.driver.find_element_by_name("name").send_keys('John')
        self.driver.find_element_by_name("email").send_keys('asjdnkadj')
        self.driver.find_element_by_name("subject").send_keys('Product enquiry')
        self.driver.find_element_by_name("message").send_keys('Are the size 9 adidas shoes available?')
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,400)")
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/form/div/div[5]/button').click()
        time.sleep(3)


    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()