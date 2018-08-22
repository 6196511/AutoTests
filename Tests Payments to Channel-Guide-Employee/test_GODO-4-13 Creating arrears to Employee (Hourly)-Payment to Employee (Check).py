from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
import time
from creds import admin_hourly_login, admin_hourly_password, admin_login, admin_password
from navigation_bar import NavigationBar
from employee_payroll import EmployeePayrollPage
import re

admin_hourly_name = "Alexey Kolennikov"
rate_per_hour = 15
tracked_time_seconds = 60
amount_tracked = 0.3 #change after fix 2430
CheckNumber=123455

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO4_13(BaseTest):
    def test_4(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_hourly_login)
        page.password_field.send_keys(admin_hourly_password)
        page.button.click()
        page = NavigationBar()
        time.sleep(6)
        page.time_tracker.click()
        time.sleep(tracked_time_seconds)
        page.time_tracker_checked.click()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = EmployeePayrollPage()
        page.open()
        time.sleep(3)
        page.employee_payment_due_hourly.click()
        L=[]
        for i in range (0, len(page.hourly_payment_due_enties)):
            if admin_hourly_name in page.hourly_payment_due_enties[i].get_attribute("textContent"):
                L.append(page.hourly_employee_payment_due_amounts[i].get_attribute("textContent"))
            else:
                continue
            break
        time.sleep(3)
        assert len(L)==1
        payment_due_amount_number=float("{0:.1f}".format(float(re.sub("[^\d\.]", "", L[0]))))
        assert payment_due_amount_number == amount_tracked
    def test_13(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = EmployeePayrollPage()
        page.open()
        page.employee_paid_hourly.click()
        time.sleep(3)
        L=[]
        for i in range (0, len(page.hourly_paid_entries)):
            if admin_hourly_name in page.hourly_paid_entries[i].get_attribute("textContent"):
                L.append(page.employee_hourly_paid_amounts[i].get_attribute("textContent"))
            else:
                continue
            break
        paid_amount_number = re.sub("[^\d\.]", "", L[0])
        page.employee_payment_due_hourly.click()
        L=[]
        for i in range (0, len(page.hourly_payment_due_enties)):
            if admin_hourly_name in page.hourly_payment_due_enties[i].get_attribute("textContent"):
                L.append(page.hourly_employee_payment_due_amounts[i].get_attribute("textContent"))
                page.detail_links_hourly[i].click()
            else:
                continue
            break
        assert len(L)==1
        payment_due_amount_alert=L[0]
        payment_due_amount_number = re.sub("[^\d\.]", "", L[0])
        time.sleep(6)
        for i in range(0, len(page.check)):
            if page.check[i].is_displayed():
                page.check[i].click()
            else:
                continue
            break
        time.sleep(6)
        for i in range(0, len(page.check_number)):
            if page.check_number[i].is_displayed():
                page.check_number[i].send_keys(CheckNumber)
            else:
                continue
            break
        time.sleep(6)
        for i in range(0, len(page.pay_button_hourly)):
            if page.pay_button_hourly[i].is_displayed():
                page.pay_button_hourly[i].click()
            else:
                continue
            break
        time.sleep(6)
        alert = get_driver().switch_to_alert()
        assert (payment_due_amount_alert + ' to ' + ''.join(admin_hourly_name)) in alert.text
        alert.accept()
        page.OK_button.click()
        page.employee_paid_hourly.click()
        time.sleep(3)
        L = []
        for i in range(0, len(page.hourly_paid_entries)):
            if admin_hourly_name in page.hourly_paid_entries[i].get_attribute("textContent"):
                L.append(page.employee_hourly_paid_amounts[i].get_attribute("textContent"))
            else:
                continue
            break
        new_paid_amount_number = re.sub("[^\d\.]", "", L[0])
        assert float(new_paid_amount_number)==float(payment_due_amount_number)+float(paid_amount_number)


