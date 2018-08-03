from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class EmployeePayrollPage(BasePage):
    url = 'https://dev.godo.io/employee_payroll.aspx'
    employee_payment_due_hourly = Find(by=By.XPATH, value="//a[@id='hourlypayrolldetailplus_']")
    employee_paid_hourly = Find(by=By.XPATH, value="//a[@ng-click='vm.showHourlyAdminPaid()']")
    hourly_payment_due_enties = Finds(by=By.XPATH, value="//tbody[@ng-if='vm.hourlyPayAdminPayments.length > 0']")
    hourly_employee_payment_due_amounts = Finds(by=By.XPATH, value="//*[@id='employeehourlypayrolldetail_']/table/tbody/tr/td[6]")
    hourly_paid_entries = Finds(by=By.XPATH, value="//*[@id='EmployeePayroll']/div[5]/table/tbody")
    employee_hourly_paid_names = Finds(by=By.XPATH,value="//*[@id='EmployeePayroll']/div[5]/table/tbody/tr/td[3]")
    employee_hourly_paid_amounts = Finds(by=By.XPATH, value="//*[@id='EmployeePayroll']/div[5]/table/tbody/tr/td[5]")
    detail_links_hourly = Finds(by=By.XPATH, value="//a[@ng-click='vm.showHourlyPayDetails(key)']")
    direct_deposit = Finds(by=By.XPATH, value="//input[@value='directdeposit']")
    cash = Finds(by=By.XPATH, value="//input[@value='cash']")
    check = Finds(by=By.XPATH, value="//input[@value='check']")
    check_number = Finds(by=By.XPATH, value="//input[@type='text']")
    pay_button_hourly = Finds(by=By.XPATH, value="//button[@ng-click='vm.commitEmployeePayments(payments)']")
    OK_button = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")

    employee_payment_due_weekly = Find(by=By.XPATH, value="//a[@id='payrolldetailplus_']")
    employee_paid_weekly = Find(by=By.XPATH, value="//a[@id='paymentPaidEmployee']")
    weekly_payment_due_enties = Finds(by=By.XPATH, value="//tbody[@ng-if='vm.weeklyPayAdminPayments.length > 0']")
    weekly_employee_payment_due_amounts = Finds(by=By.XPATH, value="//*[@id='employeepayrolldetail_']/table/tbody/tr/td[4]")
    detail_links_weekly = Finds(by=By.XPATH, value="//a[@ng-click='vm.showWeeklyPayDetails(payment.adminId)']")
    pay_button_weekly = Finds(by=By.XPATH, value="//button[@ng-click='vm.commitEmployeePayment(payment)']")
    weekly_employee_payment_due_amounts_total = Finds(by=By.XPATH, value="//*[@id='employeepayrolldetail_']/table/tbody/tr/td[6]")
    weekly_paid_entries = Finds(by=By.XPATH, value="//*[@id='dtEmpPaid']/tbody/tr")
    weekly_paid_amounts = Finds(by=By.XPATH, value="//*[@id='dtEmpPaid']/tbody/tr/td[4]")
    show_entries_list = Find(by=By.XPATH, value="//select[@name='dtEmpPaid_length']")