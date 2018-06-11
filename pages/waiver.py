from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds



class WaiverAddPage(BasePage):

    url = 'https://dev.godo.io/waiver.aspx'
    add_waiver_button = Find(by=By.XPATH, value="//button[text()='New Waiver']")
    ok_confirm_button = Find(by=By.XPATH, value="//button[text()='Ok']")
    logo_checkbox = Find(by=By.XPATH, value="//input[@name='chkCompanyLogo']")
    waiver_title = Find(by=By.XPATH, value="//input[@id='waivername']")
    waiver_header = Find(by=By.XPATH, value="//div[@class='fr-element fr-view']")
    next_button = Find(by=By.XPATH, value="//button[text()='Next >']")
    field_add = Find(by=By.XPATH, value="//select[@id='defFields']")
    insert_button = Find(by=By.XPATH, value="//button[text()=' Insert']")
    refer_field = Find(by=By.XPATH, value="//input[@id='txtCustomerWording']")
    next1_button = Find(by=By.XPATH, value="//button[@ng-click='vm.showParticipants()']")
    save_button = Find(by=By.XPATH, value="//button[@id='btnSaveWaiver']")
    entries_per_page = Find(by=By.XPATH, value="//select[@name='dtWaivers_length']")
    waiver_names = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    waiver_entries = Finds(by=By.XPATH, value="//tr[@ng-repeat='waiver in vm.companyWaivers']")
    count_value = Finds(by=By.XPATH, value="//span[@ng-bind='waiver.activityCount']")
    waiver_name = Finds(by=By.XPATH, value="//*[@id='dtWaivers']/tbody/tr/td[2]/span")