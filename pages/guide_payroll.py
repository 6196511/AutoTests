from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class GuidePayrollPage(BasePage):
    url = 'https://dev.godo.io/guide_payroll.aspx'
    guide_list = Find(by=By.XPATH, value="//select[@id='selectGuides']")
    event_due = Finds(by=By.XPATH, value ="//*[contains(@id,'guidePayroll')]/tbody/tr[1]/td[6]")
    activity_timedate = Finds(by=By.XPATH, value ="//a[contains(@ng-click,'vm.openManifest')]")
    direct_deposit = Finds(by=By.XPATH, value ="//input[@value='directdeposit']")
    cash = Finds(by=By.XPATH, value="//input[@value='cash']")
    check = Finds(by=By.XPATH, value="//input[@value='check']")
    check_number = Finds(by=By.XPATH, value="//input[@type='text']")
    pay_button = Finds(by=By.XPATH, value="//button[@id='submitpayment']")
    OK_button = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")
    show_entries = Find(by=By.XPATH, value="//select[@name='guidePayrollAll_length']")
    payment_entry = Finds(by=By.XPATH, value="//tr[@class='row']|//tr[@class='odd']|//tr[@class='even']")
    next_button = Find(by=By.XPATH, value="//*[@id='guidePayrollAll_paginate']/ul/li[3]/a")
