from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from employees import EmployeePage
from employee_payroll import EmployeePayrollPage
import random
from random import choice
import re
from string import digits
import datetime



today = datetime.date.today()
lastMonth = today - datetime.timedelta(days=30)
nextMonth = today + datetime.timedelta(days=30)
day_begin = lastMonth.strftime("%#d")
day_end = nextMonth.strftime("%#d")



class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO12(BaseTest):
    def test_12(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = EmployeePage()
        page.open()
        page.add_new_user.click()
        NewUserName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8))+'qwer')
        page.password_field.send_keys(NewUserPassword)
        first_names = ('Ivan','Peter','John','Bill','Michael','Sidor','Alex','James')
        NewFirstName = random.choice(first_names )
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith','Baker','Petroff','Smirnoff','Black','White','Broun','Ivanoff')
        NewLastName = random.choice(last_names)
        page.last_name_field.send_keys(NewLastName)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewPhone2 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone2_field.send_keys(NewPhone2)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10))+'@mailinator.com')
        page.email_field.send_keys(NewEmail)
        select = Select(page.role_list)
        NewRole = "Office Staff"
        select.select_by_visible_text(NewRole)
        select = Select(page.payroll_type_list)
        NewPayrollType = "weekly"
        select.select_by_visible_text(NewPayrollType)
        NewSalaryAmount = '100'
        NewTotalAmount = str(int(NewSalaryAmount)*4)
        page.amount_field.send_keys(NewSalaryAmount)
        page.status_checkbox.click()
        page.hire_date_field.click()
        time.sleep(5)
        for i in range(0, len(page.calendar_begin_prev)):
            if page.calendar_begin_prev[i].is_displayed():
                page.calendar_begin_prev[i].click()
            else:
                continue
            break
        time.sleep(2)
        for i in range(0, len(page.dates_calendar_begin)):
            if page.dates_calendar_begin[i].get_attribute('textContent') == day_begin:
                page.dates_calendar_begin[i].click()
            else:
                continue
            break
        time.sleep(5)
        page.end_date_field.click()
        time.sleep(5)
        for i in range(0, len(page.calendar_end_next)):
            if page.calendar_end_next[i].is_displayed():
                page.calendar_end_next[i].click()
            else:
                continue
            break
        time.sleep(2)
        for i in range(0, len(page.dates_calendar_end)):
            if page.dates_calendar_end[i].get_attribute('textContent') == day_end:
                page.dates_calendar_end[i].click()
            else:
                continue
            break
        time.sleep(5)
        page.save_button.click()

        page = EmployeePayrollPage()
        page.open()
        page.employee_payment_due_weekly.click()
        time.sleep(3)
        L = []
        L1=[]
        for i in range(0, len(page.weekly_payment_due_enties)):
            if (''.join(NewFirstName)+' '+''.join(NewLastName)) in page.weekly_payment_due_enties[i].get_attribute("textContent"):
                L.append(page.weekly_employee_payment_due_amounts[i].get_attribute("textContent"))
                L1.append(page.weekly_employee_payment_due_amounts_total[i].get_attribute("textContent"))
                page.detail_links_weekly[i].click()
            else:
                continue
            break
        assert len(L) == 1
        assert len(L1) == 1
        payment_due_amount_alert=L1[0]
        payment_due_amount_number_weekly = re.sub("[^\d\.]", "", L[0])
        assert NewSalaryAmount == payment_due_amount_number_weekly
        payment_due_amount_number_weekly_total = re.sub("[^\d\.]", "", L1[0])
        assert float(NewTotalAmount) == float(payment_due_amount_number_weekly_total)
        time.sleep(6)
        for i in range(0, len(page.cash)):
            if page.cash[i].is_displayed():
                page.cash[i].click()
            else:
                continue
            break
        time.sleep(6)
        for i in range(0, len(page.pay_button_weekly)):
            if page.pay_button_weekly[i].is_displayed():
                page.pay_button_weekly[i].click()
            else:
                continue
            break
        time.sleep(6)
        alert = get_driver().switch_to_alert()
        assert (payment_due_amount_alert + ' to ' + ''.join(NewFirstName)+' '+''.join(NewLastName)) in alert.text
        alert.accept()
        page.OK_button.click()
        page.employee_paid_weekly.click()
        select = Select(page.show_entries_list)
        select.select_by_visible_text('100')
        time.sleep(3)
        L = []
        for i in range(0, len(page.weekly_paid_entries)):
            if (''.join(NewFirstName)+' '+''.join(NewLastName)) in page.weekly_paid_entries[i].get_attribute("textContent"):
                L.append(page.weekly_paid_amounts[i].get_attribute("textContent"))
            else:
                continue
            break
        new_paid_amount_number = re.sub("[^\d\.]", "", L[0])
        assert float(NewTotalAmount) == float(new_paid_amount_number)