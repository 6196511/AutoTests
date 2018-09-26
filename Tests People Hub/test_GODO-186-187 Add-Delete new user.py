from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from employees import EmployeePage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
from random import choice
from string import digits
import datetime

email_list = []
fullname_list = []

class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO186_187(BaseTest):
    def test_186(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        time.sleep(5)
        page = EmployeePage()
        page.open()
        page.add_new_user.click()
        NewUserName = ("autotest_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.password_field.send_keys(NewUserPassword)
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James')
        NewFirstName = random.choice(first_names)
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff')
        NewLastName = random.choice(last_names)
        page.last_name_field.send_keys(NewLastName)
        NewFullName = NewFirstName+' '+ ''.join(NewLastName)
        fullname_list.append(NewFullName)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewPhone2 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone2_field.send_keys(NewPhone2)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10)) + '@mailinator.com')
        page.email_field.send_keys(NewEmail)
        email_list.append(NewEmail)
        select = Select(page.role_list)
        NewRole = "Office Staff"
        select.select_by_visible_text(NewRole)
        select = Select(page.payroll_type_list)
        NewPayrollType = "weekly"
        select.select_by_visible_text(NewPayrollType)
        NewSalaryAmount = '100'
        page.amount_field.send_keys(NewSalaryAmount)
        page.status_checkbox.click()
        NewHireDate = '09/25/2018'
        page.hire_date_field.send_keys(NewHireDate)
        NewEndDate = '09/25/2020'
        page.end_date_field.send_keys(NewEndDate)
        time.sleep(5)
        NewUserHouseNumber = '' + ''.join(choice(digits) for i in range(2))
        page.house_number_field.send_keys(NewUserHouseNumber)
        NewUserStreet = 'Main Street'
        page.street_field.send_keys( NewUserStreet )
        NewUserCity = 'Boston'
        page.city_field.send_keys(NewUserCity)
        NewUserCountry = "United States"
        select = Select(page.country_list)
        select.select_by_visible_text(NewUserCountry)
        NewUserState = 'Florida'
        select = Select(page.state_list)
        time.sleep(3)
        select.select_by_visible_text(NewUserState)
        NewUserZip = '54321'
        page.user_zip.send_keys('54321')
        select = Select(page.branch_list)
        NewBranch = "AlexeyBranch"
        select.select_by_visible_text(NewBranch)
        NewAccountOwnerName = 'TestAccountOwner'
        page.name_account_owner_field.send_keys(NewAccountOwnerName)
        NewBankName = 'BSB Bank'
        page.bank_name_field.send_keys(NewBankName)
        time.sleep(5)
        NewRoutingNumber = '' + ''.join(choice(digits) for i in range(8))
        page.routing_number_field.send_keys(NewRoutingNumber)
        NewAccountNumber = '' + ''.join(choice(digits) for i in range(8))
        page.account_number_field.send_keys(NewAccountNumber)
        NewEmergencyContact = '' + ''.join(choice(digits) for i in range(8))
        page.em_contact_field.send_keys(NewEmergencyContact)
        NewEmergencyPhone = '' + ''.join(choice(digits) for i in range(8))
        page.em_phone_field.send_keys(NewEmergencyPhone)
        L=[]
        for i in range(0, len(page.permission_entries)):
            if page.permission_checkbox[i].get_attribute('checked') == 'true':
                L.append(page.permission_entries[i].get_attribute('outerText'))
            else:
                continue
        page.save_button.click()
        time.sleep(6)
        page.search_field.clear()
        page.search_field.send_keys(NewEmail)
        time.sleep(6)
        page.edit_user_button.click()
        time.sleep(2)
        assert page.username_readonly_field.get_attribute('value') == NewUserName
        assert page.first_name_field.get_attribute('value') == NewFirstName
        assert page.last_name_field.get_attribute('value') == NewLastName
        assert page.phone1_field.get_attribute('value') == NewPhone1
        assert page.phone2_field.get_attribute('value') == NewPhone2
        assert page.email_field.get_attribute('value') == NewEmail
        select = Select(page.role_list)
        assert select.first_selected_option.text == NewRole
        select = Select(page.payroll_type_list)
        assert select.first_selected_option.text == NewPayrollType
        assert page.amount_field.get_attribute('value') == NewSalaryAmount
        assert page.status_checkbox.get_attribute('checked') == 'true'
        assert page.hire_date_field.get_attribute('value') == NewHireDate
        assert page.end_date_field.get_attribute('value') == NewEndDate
        assert page.house_number_field.get_attribute('value') == NewUserHouseNumber
        assert page.street_field.get_attribute('value') == NewUserStreet
        assert page.city_field.get_attribute('value') == NewUserCity
        select = Select(page.country_list)
        assert select.first_selected_option.text == NewUserCountry
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewUserState
        assert page.user_zip.get_attribute('value') == NewUserZip
        select = Select(page.branch_list)
        assert select.first_selected_option.text == NewBranch
        assert page.name_account_owner_field.get_attribute('value') == NewAccountOwnerName
        assert page.bank_name_field.get_attribute('value') == NewBankName
        assert page.routing_number_field.get_attribute('value') == NewRoutingNumber
        assert page.account_number_field.get_attribute('value') == NewAccountNumber
        L1 = []
        for i in range(0, len(page.permission_entries)):
            if page.permission_checkbox[i].get_attribute('checked') == 'true':
                L1.append(page.permission_entries[i].get_attribute('outerText'))
            else:
                continue
        assert L ==L1
    def test_187(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        time.sleep(5)
        page = EmployeePage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(email_list[0])
        time.sleep(5)
        page.delete_user_button.click()
        time.sleep(5)
        alert = get_driver().switch_to_alert()
        assert (fullname_list[0]) in alert.text
        alert.accept()
        time.sleep(2)
        page.search_field.send_keys(email_list[0])
        time.sleep(2)
        assert page.is_element_present('no_such_entry_msg')
        assert page.no_such_entry_msg.get_attribute('textContent') == "No matching records found"
