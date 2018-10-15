from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from employees import EmployeePage
from activity_hub_page import ActivityHubPage
from event_calendar import EventCalendarPage
from navigation_bar import NavigationBar
from channel_page import ChannelPage
from waiver import WaiverAddPage
from marketing_hub_page import DiscountPage
from groupon_page import GrouponPage
from admin_certificate import CertificatePage
from invoice import InvoicePage, InvoicePageV2
from people_hub_page import PeopleHubPage
from guide_payroll import GuidePayrollPage
from channel_payroll import ChannelPayrollPage
from guide_bulkassignment import GuideBulAssignmentPage
from starting_location import AddStartingLocationPage
from company_page import EditCompanyPage
from analytics_dashboard import AnalyticsDashboardPage
from taxes_report import TaxesReportPage
from self_profile_page import SelfProfilePage
from customer_list import CustomerListPage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from random import choice
from string import digits
from selenium.webdriver.common.by import By
from webium import BasePage, Find

email_list = []
fullname_list = []
username_list = []
pwd_list = []
permission_1 = 'View Invoice'
permission_2 = 'Edit Guides Information'
no_permission_msg = 'ERROR: You do not have permission to view this page. Please log in under a user that has proper permission.'

class NoPermission(BasePage):
    no_permission_alert = Find(by=By.XPATH, value="//div[@class='col-sm-10']")

class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO245_246(BaseTest):
    def test_245(self):
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
        NewUserName = ("autotest245_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        username_list.append(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.password_field.send_keys(NewUserPassword)
        pwd_list.append(NewUserPassword)
        NewFirstName = "AutoTest"
        page.first_name_field.send_keys(NewFirstName)
        NewLastName = '245'
        page.last_name_field.send_keys(NewLastName)
        NewFullName = NewFirstName+' '+ ''.join(NewLastName)
        fullname_list.append(NewFullName)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10)) + '@mailinator.com')
        page.email_field.send_keys(NewEmail)
        email_list.append(NewEmail)
        select = Select(page.role_list)
        NewRole = "Lead Guide"
        select.select_by_visible_text(NewRole)
        select = Select(page.payroll_type_list)
        NewPayrollType = "weekly"
        select.select_by_visible_text(NewPayrollType)
        NewSalaryAmount = '100'
        page.amount_field.send_keys(NewSalaryAmount)
        page.status_checkbox.click()
        time.sleep(5)
        select = Select(page.branch_list)
        NewBranch = "AlexeyBranch"
        select.select_by_visible_text(NewBranch)
        time.sleep(5)
        for i in range(0, len(page.permission_entries)):
            if permission_1 in page.permission_entries[i].get_attribute('outerText'):
                page.permission_checkbox[i].click()
            elif  permission_2 in page.permission_entries[i].get_attribute('outerText'):
                page.permission_checkbox[i].click()
            else:
                continue
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
        assert page.email_field.get_attribute('value') == NewEmail
        select = Select(page.role_list)
        assert select.first_selected_option.text == NewRole
        select = Select(page.payroll_type_list)
        assert select.first_selected_option.text == NewPayrollType
        assert page.amount_field.get_attribute('value') == NewSalaryAmount
        assert page.status_checkbox.get_attribute('checked') == 'true'
        select = Select(page.branch_list)
        assert select.first_selected_option.text == NewBranch
        L1 = []
        for i in range(0, len(page.permission_entries)):
            if page.permission_checkbox[i].get_attribute('checked') == 'true':
                L1.append(page.permission_entries[i].get_attribute('outerText'))
            else:
                continue
        assert L ==L1
        print(username_list)
        print(pwd_list)
    def test_246(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(username_list[0])#STEP1
        page.password_field.send_keys(pwd_list[0])
        page.button.click()
        time.sleep(5)
        page = EmployeePage() #STEP2
        page.open()
        time.sleep(2)
        assert page.is_element_present('add_new_user') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = ActivityHubPage() #STEP3
        page.open()
        time.sleep(2)
        assert page.is_element_present('add_activity_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = NavigationBar() #STEP 4
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = ChannelPage() #STEP 5
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = WaiverAddPage() #STEP 6
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = DiscountPage() #STEP 7
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = GrouponPage() #STEP 8
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = CertificatePage() #STEP 9
        page.open()
        time.sleep(2)
        assert page.is_element_present('add_new_certificate_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = InvoicePage() #STEP 10
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = InvoicePageV2() #STEP 11 BLOCKED
        page.open() 
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = PeopleHubPage() #STEP 12
        page.open()
        time.sleep(2)
        assert page.is_element_present('add_guide_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = PeopleHubPage()  # STEP 12.1
        page.add_guide_button.click()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = PeopleHubPage()  # STEP 12.2
        page.open()
        time.sleep(2)
        page.edit_guide_button.click()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = GuidePayrollPage() #STEP 13
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = ChannelPayrollPage() #STEP 14
        page.open()
        time.sleep(2)
        assert page.is_element_present('channel_payment_due') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = EventCalendarPage()#STEP 15
        page.open()
        assert page.is_element_present('date_picker') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = GuideBulAssignmentPage() #STEP 16
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = AddStartingLocationPage()#STEP 17
        page.open()
        assert page.is_element_present('location_name') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = TaxesReportPage() #STEP 18
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = AnalyticsDashboardPage() #STEP 19
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = EditCompanyPage()#STEP 20
        page.open()
        assert page.is_element_present('company_name_field') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = SelfProfilePage()#STEP 21
        page.open()
        assert page.is_element_present('first_name_field') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = CustomerListPage()#STEP 22
        page.open()
        assert page.is_element_present('add_customer_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False