# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Approve(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://institution.happymangocredit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_approve(self):
        driver = self.driver
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//button[@applicationid='474']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//button[@applicationid='474']").click()
        driver.find_element_by_link_text("Yes").click()
        driver.find_element_by_id("checkpass").click()
        driver.find_element_by_id("notes").clear()
        driver.find_element_by_id("notes").send_keys("test")
        driver.find_element_by_xpath("(//button[@type='button'])[11]").click()
        driver.find_element_by_id("historycheck").click()
        driver.find_element_by_id("creditnotes").clear()
        driver.find_element_by_id("creditnotes").send_keys("test")
        driver.find_element_by_id("gotocashflow").click()
        for i in range(60):
            try:
                if self.is_element_present(By.ID, "btn-ApproveModal"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
