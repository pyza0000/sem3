import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def add_numbers(a,b):
    return a+b

class TestSimpleAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_numbers(2,3),5)

class TestGoogleSearch(unittest.TestCase):
    def test_google_search(self):
        driver=webdriver.Chrome()
        driver.get("https://www.google.com")
        time.sleep(3)
        try:
            driver.find_element(By.TAG_NAME,"body").click()
        except:
            pass
        time.sleep(1)
        search=driver.find_element(By.NAME,"q")
        search.send_keys("Python unittest")
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertIn("python",driver.title.lower())
        driver.quit()

class TestURLChange(unittest.TestCase):
    def test_url_change(self):
        driver=webdriver.Chrome()
        driver.get("https://www.python.org")
        time.sleep(2)
        try:
            link=driver.find_element(By.LINK_TEXT,"Downloads")
            link.click()
        except:
            pass
        time.sleep(3)
        self.assertIn("downloads",driver.current_url.lower())
        driver.quit()

if __name__=="__main__":
    unittest.main()
