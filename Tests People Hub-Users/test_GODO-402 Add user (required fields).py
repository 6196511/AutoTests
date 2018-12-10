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

class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO402(BaseTest):
    def test_402(self):
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
        NewUserName = ("autotest402_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.password_field.send_keys(NewUserPassword)
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James')
        NewFirstName = random.choice(first_names)
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff')
        NewLastName = random.choice(last_names)
        page.last_name_field.send_keys(NewLastName)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10)) + '@mailinator.com')
        page.email_field.send_keys(NewEmail)
        select = Select(page.role_list)
        NewRole = "Office Staff"
        select.select_by_visible_text(NewRole)
        select = Select(page.payroll_type_list)
        NewPayrollType = "weekly"
        select.select_by_visible_text(NewPayrollType)
        NewSalaryAmount = '100'
        page.amount_field.send_keys(NewSalaryAmount)
        page.status_checkbox.click()
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
        assert page.email_field.get_attribute('value') == NewEmail
        select = Select(page.role_list)
        assert select.first_selected_option.text == NewRole
        select = Select(page.payroll_type_list)
        assert select.first_selected_option.text == NewPayrollType
        assert page.amount_field.get_attribute('value') == NewSalaryAmount
        assert page.status_checkbox.get_attribute('checked') == 'true'
