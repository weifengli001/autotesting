# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HoldApproveTogather(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://institution.happymangocredit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_hold_approve_togather(self):
        driver = self.driver
        driver.get(self.base_url + "/auth/login")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("99zhadmin")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("liweifeng.liwf@gmail.com")
        driver.find_element_by_css_selector("input[type=\"checkbox\"]").click()
        driver.find_element_by_css_selector("input.btn.btn-happymango").click()
        driver.find_element_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr/td[13]/button").click()
        driver.find_element_by_link_text("Yes").click()
        driver.find_element_by_id("checkfail").click()
        driver.find_element_by_xpath("(//button[@type='button'])[10]").click()
        driver.find_element_by_css_selector("#HoldInfoModal > div.modal-dialog.ui-draggable > div.modal-content > div.modal-footer > button.btn.btn-confirm").click()
        time.sleep(10)
        driver.find_element_by_link_text("Applications").click()
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "New"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("New", driver.find_element_by_link_text("New").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertEqual("New", driver.find_element_by_link_text("New").text)
        driver.find_element_by_link_text("New").click()
        driver.find_element_by_xpath("//table[@id='DataTables_Table_0']/tbody/tr/td[13]/button").click()
        driver.find_element_by_link_text("Yes").click()
        driver.find_element_by_id("checkpass").click()
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_id("historycheck").click()
        driver.find_element_by_id("historycheck").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_id("historycheck").click()
        driver.find_element_by_id("historycheck").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_xpath("(//input[@name='historycheck'])[2]").click()
        driver.find_element_by_id("gotocashflow").click()
        driver.find_element_by_id("btn-ApproveModal").click()
        driver.find_element_by_id("btn_recommendation_approve").click()
        driver.find_element_by_css_selector("#ApproveInfoModal > div.modal-dialog.ui-draggable > div.modal-content > div.modal-footer > button.btn.btn-confirm").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
