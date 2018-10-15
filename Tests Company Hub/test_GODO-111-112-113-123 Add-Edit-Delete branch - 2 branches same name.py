from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from branch_page import BranchPage, CustomerBranchPage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from random import choice
from string import digits


BranchNewNameList = []
BranchEditedNameList =[]

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO111_112_113_123(BaseTest):
    def test_111(self): #ADD BRANCH
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=BranchPage()
        page.open()
        page.add_branch_button.click()
        BranchName = 'AutoTest'+''.join(choice(digits) for i in range(4))
        page.branch_name_field.send_keys(BranchName)
        BranchNewNameList.append(BranchName)
        select = Select(page.timezone_list)
        NewBranchTimeZone = "Atlantic"
        select.select_by_visible_text(NewBranchTimeZone)
        NewBranchAddress1 = "test012"
        page.branch_address1.send_keys(NewBranchAddress1)
        NewBranchAddress2 = "test012"
        page.branch_address2.send_keys(NewBranchAddress2)
        select = Select(page.country_list)
        NewBranchCountry = "United States"
        select.select_by_visible_text(NewBranchCountry)
        time.sleep(6)
        select = Select(page.state_list)
        NewBranchState = "Washington"
        select.select_by_visible_text(NewBranchState)
        NewBranchCity = "Seattle"
        page.branch_city.send_keys(NewBranchCity)
        NewBranchZip = "12341"
        page.branch_zip.send_keys(NewBranchZip)
        NewBranchEmail = "6196511@mailinator.com"
        page.branch_email.send_keys(NewBranchEmail)
        NewBranchPhone1 = "(206)624-3287"
        page.branch_phone1.send_keys(NewBranchPhone1)
        NewBranchPhone2 = "(206)624-3287"
        page.branch_phone2.send_keys(NewBranchPhone2)
        page.save_button.click()
        time.sleep(3)
        for i in range (0, len(page.branch_names)):
            if page.branch_names[i].get_attribute('textContent') == BranchName:
                page.branch_edit_buttons[i].click()
            else:
                continue
            break
        time.sleep(3)
        assert page.branch_name_field.get_attribute('value') == BranchName
        select = Select(page.timezone_list)
        assert select.first_selected_option.text == NewBranchTimeZone
        assert page.branch_address1.get_attribute('value') == NewBranchAddress1
        assert page.branch_address2.get_attribute('value') == NewBranchAddress2
        select = Select(page.country_list)
        assert select.first_selected_option.text == NewBranchCountry
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewBranchState
        assert page.branch_city.get_attribute('value') == NewBranchCity
        assert page.branch_zip.get_attribute('value') == NewBranchZip
        assert page.branch_email.get_attribute('value') == NewBranchEmail
        assert page.branch_phone1.get_attribute('value') == NewBranchPhone1
        assert page.branch_phone2.get_attribute('value') == NewBranchPhone2
    def test_112(self):#EDIT BRANCH
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=BranchPage()
        page.open()
        for i in range(0, len(page.branch_names)):
            if page.branch_names[i].get_attribute('textContent') == BranchNewNameList[0]:
                page.branch_edit_buttons[i].click()
            else:
                continue
            break
        time.sleep(3)
        BranchName = 'AutoTestEdited'+''.join(choice(digits) for i in range(4))
        BranchEditedNameList.append(BranchName)
        page.branch_name_field.clear()
        page.branch_name_field.send_keys(BranchName)
        BranchNewNameList.append(BranchName)
        select = Select(page.timezone_list)
        NewBranchTimeZone = "Eastern"
        select.select_by_visible_text(NewBranchTimeZone)
        NewBranchAddress1 = "Main Street"
        page.branch_address1.clear()
        page.branch_address1.send_keys(NewBranchAddress1)
        NewBranchAddress2 = "123-123"
        page.branch_address2.clear()
        page.branch_address2.send_keys(NewBranchAddress2)
        select = Select(page.country_list)
        NewBranchCountry = "Canada"
        select.select_by_visible_text(NewBranchCountry)
        time.sleep(6)
        select = Select(page.state_list)
        NewBranchState = "Alberta"
        select.select_by_visible_text(NewBranchState)
        NewBranchCity = "Toronto"
        page.branch_city.clear()
        page.branch_city.send_keys(NewBranchCity)
        time.sleep(4)
        NewBranchZip = "A1A 1A1"
        page.branch_zip.clear()
        page.branch_zip.send_keys(NewBranchZip)
        NewBranchEmail = "3242342342@mailinator.com"
        page.branch_email.clear()
        page.branch_email.send_keys(NewBranchEmail)
        NewBranchPhone1 = "(017)327-3730"
        page.branch_phone1.clear()
        page.branch_phone1.send_keys(NewBranchPhone1)
        NewBranchPhone2 = "(017)271-3420"
        page.branch_phone2.clear()
        page.branch_phone2.send_keys(NewBranchPhone2)
        page.save_button.click()
        time.sleep(3)
        for i in range(0, len(page.branch_names)):
            if page.branch_names[i].get_attribute('textContent') == BranchName:
                page.branch_edit_buttons[i].click()
            else:
                continue
            break
        time.sleep(3)
        assert page.branch_name_field.get_attribute('value') == BranchName
        select = Select(page.timezone_list)
        assert select.first_selected_option.text == NewBranchTimeZone
        assert page.branch_address1.get_attribute('value') == NewBranchAddress1
        assert page.branch_address2.get_attribute('value') == NewBranchAddress2
        select = Select(page.country_list)
        assert select.first_selected_option.text == NewBranchCountry
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewBranchState
        assert page.branch_city.get_attribute('value') == NewBranchCity
        assert page.branch_zip.get_attribute('value') == NewBranchZip #FAILED BUG 2833
        assert page.branch_email.get_attribute('value') == NewBranchEmail
        assert page.branch_phone1.get_attribute('value') == NewBranchPhone1
        assert page.branch_phone2.get_attribute('value') == NewBranchPhone2
    def test_113(self):#DELETE BRANCH
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=BranchPage()
        page.open()
        for i in range(0, len(page.branch_names)):
            if page.branch_names[i].get_attribute('textContent') == BranchEditedNameList[0]:
                page.delete_buttons[i-1].click()
            else:
                continue
            break
        time.sleep(3)
        branch_list = []
        for i in range(0, len(page.branch_names)):
            branch_list.append(page.branch_names[i].get_attribute('textContent'))
        assert BranchEditedNameList[0] not in branch_list
        page = CustomerBranchPage()
        page.open()
        customer_branch_list = []
        for i in range(0, len(page.branch_tickets)):
            customer_branch_list.append(page.branch_tickets[i].get_attribute('textContent'))
        assert BranchEditedNameList[0] not in customer_branch_list

    def test_123(self):#2 BRANCHES WITH THE SAME NAME
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=BranchPage()
        page.open()
        branch_list = []
        for i in range(0, len(page.branch_names)):
            branch_list.append(page.branch_names[i].get_attribute('textContent'))
        time.sleep(3)
        page.add_branch_button.click()
        BranchName = branch_list[-1]
        page.branch_name_field.send_keys(BranchName)
        BranchNewNameList.append(BranchName)
        select = Select(page.timezone_list)
        NewBranchTimeZone = "Atlantic"
        select.select_by_visible_text(NewBranchTimeZone)
        NewBranchAddress1 = "test012"
        page.branch_address1.send_keys(NewBranchAddress1)
        NewBranchAddress2 = "test012"
        page.branch_address2.send_keys(NewBranchAddress2)
        select = Select(page.country_list)
        NewBranchCountry = "United States"
        select.select_by_visible_text(NewBranchCountry)
        time.sleep(6)
        select = Select(page.state_list)
        NewBranchState = "Washington"
        select.select_by_visible_text(NewBranchState)
        NewBranchCity = "Seattle"
        page.branch_city.send_keys(NewBranchCity)
        NewBranchZip = "12341"
        page.branch_zip.send_keys(NewBranchZip)
        NewBranchEmail = "6196511@mailinator.com"
        page.branch_email.send_keys(NewBranchEmail)
        NewBranchPhone1 = "(206)624-3287"
        page.branch_phone1.send_keys(NewBranchPhone1)
        NewBranchPhone2 = "(206)624-3287"
        page.branch_phone2.send_keys(NewBranchPhone2)
        page.save_button.click()
        time.sleep(3)
        assert page.is_element_present('alert_message') == True
        branch_list1 = []
        for i in range(0, len(page.branch_names)):
            branch_list1.append(page.branch_names[i].get_attribute('textContent'))
        assert len(branch_list1 ) == len(branch_list)
