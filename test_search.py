import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class search(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(r'C:\Users\sumuk\Downloads\chromedriver_win32 (1)\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://enigmatic-retreat-90606.herokuapp.com/')
        time.sleep(3)
    @classmethod
    def tearDownClass(self):
        time.sleep(3)
        self.driver.close()

    def test_searchsuccess(self):
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[1]/span').click()
        time.sleep(3)
        self.driver.find_element_by_name('search').send_keys('Adidas')
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,200)")
    def test_searchfail(self):
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[1]/span').click()
        time.sleep(3)
        self.driver.find_element_by_name('search').send_keys('gucci')
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()

