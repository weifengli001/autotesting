import unittest
import time
from selenium import webdriver

class SwitchToWindowTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
    def test_switch_to_window(self):
        driver = self.driver
        driver.get('http://robotframework.org')
        library_link = driver.find_element_by_xpath("//a[@href='#test-libraries']")
        library_link.click()
        builtin_link = driver.find_element_by_link_text("Builtin")
        builtin_link.click()
        time.sleep(15)
        windows = driver.window_handles
        number_of_windows = len(windows)
        print 'Number of Windows: ', number_of_windows
        driver.switch_to_window(windows[number_of_windows - 1])
        expected_text = driver.find_element_by_xpath("//table/tbody//td[contains(text(),'BuiltIn')]")
        self.assertTrue(expected_text.is_displayed())
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()