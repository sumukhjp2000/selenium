import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class Addtocart(unittest.TestCase):
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

    def test_emptycart(self):
        self.driver.get('https://enigmatic-retreat-90606.herokuapp.com/')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[4]/a/div/span').click()
        time.sleep(2)

    def test_addtocart(self):
        item1 = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/img')
        item2 = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[3]/div[2]/div[5]/div[1]/img')
        self.driver.execute_script("arguments[0].scrollIntoView();",item1)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[3]/div[1]/div[2]/div[2]/button/span').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,2000)")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[3]/div[2]/div[5]/div[2]/button/span').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(3000,0)")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[4]/a/div/span').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(4)
if __name__=="__main__":
    unittest.main()
