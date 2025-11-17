import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='/path/to/geckodriver')
        self.driver = webdriver.Firefox(service=service)
    def test_search_python_unittest(self):
        driver = self.driver
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python unittest" + Keys.RETURN)
        self.assertIn("Python", driver.title)

    def tearDown(self):
        self.driver.quit()