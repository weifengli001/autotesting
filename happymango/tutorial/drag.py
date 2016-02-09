import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class ActionChainsTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_action_chains_drag(self):
        driver = self.driver
        driver.get('https://jqueryui.com/draggable')
        frame=driver.find_element_by_tag_name('iframe')
        driver.switch_to_frame(frame)
        draggable_element = driver.find_element_by_xpath("//div[@id='draggable']")
        location1 = draggable_element.location
        print "Before Drag Position: ", location1
        x1 = location1.get('x')
        print x1
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(draggable_element, 100, 0)
        actions.perform()
        time.sleep(5)
        location2 = draggable_element.location
        print "After Drag Postion: ", location2
        x2 = location2.get('x')
        print x2
        self.assertTrue(x2 - x1 == 100)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

