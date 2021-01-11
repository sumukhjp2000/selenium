import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


class signup(unittest.TestCase):
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

    def test_signup(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[3]/div').click()
        fh = open("signupdata.txt")
        for line in fh:
            count = 0
            if line.startswith("Id: "):
                pos = line.find(" ")
                valI = line[pos + 1:]
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/form/input[1]').send_keys(valI)

            else:
                posi = line.find(" ")
                valP = line[posi + 1:]
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/form/input[2]').send_keys(valP)
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/form/input[3]').send_keys(valP)
                time.sleep(3)
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div/button').click()
                time.sleep(3)
                try:
                    time.sleep(2)
                    self.driver.switch_to_alert().accept()
                    self.driver.refresh()
                    continue
                except:
                    print(".")
                # signout
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[3]/div/span').click()
                time.sleep(3)
                # signin
                self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div[3]/div/span').click()
                time.sleep(3)
                handle = open('registered.txt','a+')
                print("\n")
                print("\n")
                handle.write("Id: "+ valI)
                handle.write("password: "+valP)
        print("\n")
if __name__ == "__main__":
    unittest.main()
