# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoantestPy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.happymangocredit.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_loantest_py(self):
        driver = self.driver
        driver.get(self.base_url + "/#login")
        for i in range(60):
            try:
                if self.is_element_present(By.NAME, "email"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("liweifeng.liwf@gmail.com")
        for i in range(60):
            try:
                if self.is_element_present(By.NAME, "password"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("alms1234")
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "button.btn.btn-happymango"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.btn.btn-happymango").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.navs > ul > li.short.first > a"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("div.navs > ul > li.short.first > a").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "h3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("h3").click()
        driver.find_element_by_id("loan-amount").clear()
        driver.find_element_by_id("loan-amount").send_keys("$ 200")
        driver.find_element_by_id("loan-peroid").clear()
        driver.find_element_by_id("loan-peroid").send_keys("3")
        driver.find_element_by_id("loan-company").clear()
        driver.find_element_by_id("loan-company").send_keys("City Bank")
        Select(driver.find_element_by_name("hireYear")).select_by_visible_text("2012")
        Select(driver.find_element_by_name("hireMonth")).select_by_visible_text("February")
        driver.find_element_by_name("occupation").clear()
        driver.find_element_by_name("occupation").send_keys("Manager")
        driver.find_element_by_name("monthlyIncome").clear()
        driver.find_element_by_name("monthlyIncome").send_keys("$ 10,000")
        driver.find_element_by_xpath("(//input[@name='purpose'])[2]").click()
        driver.find_element_by_id("next-button").click()
        driver.find_element_by_id("next-button").click()
    
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
