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
from invoice import InvoicePageV2
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
from fakemailgenerator_page import FakeMailGeneratorPage


CompanyName = 'GoDo Manual Testing Company'
email_list = []
email_local_list=[]
fullname_list = []
username_list = []
pwd_list = []
permission_1 = 'Edit Users'
permission_2 = 'Edit Activities'
no_permission_msg = 'ERROR: You do not have permission to view this page. Please log in under a user that has proper permission.'

class NoPermission(BasePage):
    no_permission_alert = Find(by=By.XPATH, value="//div[@class='col-sm-10']")

class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO243_244_495(BaseTest):
    def test_243(self):
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
        NewUserName = ("autotest243_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        username_list.append(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.password_field.send_keys(NewUserPassword)
        pwd_list.append(NewUserPassword)
        NewFirstName = "AutoTest"
        page.first_name_field.send_keys(NewFirstName)
        NewLastName = '243'
        page.last_name_field.send_keys(NewLastName)
        NewFullName = NewFirstName+' '+ ''.join(NewLastName)
        fullname_list.append(NewFullName)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewEmailILocal = '' + ''.join(choice(digits) for i in range(10))
        email_local_list.append(NewEmailILocal)
        NewEmailDomain = '@cuvox.de'
        NewEmail = (NewEmailILocal + NewEmailDomain)
        page.email_field.send_keys(NewEmail)
        email_list.append(NewEmail)
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

    def test_495(self):
        get_driver().maximize_window()
        page = FakeMailGeneratorPage()
        page.open()
        page.inbox_field.clear()
        page.inbox_field.send_keys(email_local_list[0])
        page.domain_list.click()
        time.sleep(2)
        page.cuvox_domain.click()
        time.sleep(10)
        assert page.from_field.get_attribute('textContent') == '"GoDo" <email_admin@email.godo.io>'
        assert page.to_field.get_attribute('textContent') == email_list[0]
        assert page.subject_field.get_attribute('textContent') == 'You have been added as an admin for '+''.join(CompanyName)
        get_driver().switch_to_frame('emailFrame')
        assert page.body_field.get_attribute('innerText') == ''.join(fullname_list[0])+',\nWelcome to GoDo. You have been added as an admin for '+''.join(CompanyName)+'.\n\nTo log in, go to:\nhttps://dev.godo.io/ \n\nAnd use this information:\n\nLOGIN: '+''.join(username_list[0])+'\nPASSWORD: '+''.join(pwd_list[0])+'\n\n\n\n\xa0\nThank you, \nThe '+''.join(CompanyName)+' Team \xa0 \n\xa0 \n\xa0 \n\xa0 \n'

    def test_244(self):
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
        page = NoPermission()
        assert page.no_permission_alert.get_attribute('outerText')== no_permission_msg
        page = ActivityHubPage() #STEP3.1
        page.open()
        time.sleep(8)
        page.activity_actions.click()
        page.get_widget.click()
        time.sleep(2)
        assert "customer_flow.aspx" in get_driver().current_url
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = ActivityHubPage() #STEP3.2
        page.open()
        time.sleep(8)
        page.activity_actions.click()
        page.view_calendar.click()
        time.sleep(2)
        assert "event_calendar.aspx" in get_driver().current_url
        page = EventCalendarPage()
        assert page.is_element_present('date_picker') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = ActivityHubPage()  # STEP3.3
        page.open()
        time.sleep(5)
        page.activity_actions.click()
        page.add_events.click()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = ActivityHubPage()  # STEP3.4
        page.open()
        time.sleep(8)
        page.activity_actions.click()
        page.edit_activity.click()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==True
        assert page.no_permission_alert.get_attribute('outerText') == no_permission_msg
        page = ActivityHubPage()  # STEP3.4
        page.open()
        time.sleep(8)
        page.activity_actions.click()
        time.sleep(2)
        page.edit_activity.click()
        time.sleep(2)
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
        page = InvoicePageV2() #STEP 10
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = PeopleHubPage() #STEP 11
        page.open()
        time.sleep(2)
        assert page.is_element_present('add_guide_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = GuidePayrollPage() #STEP 12
        page.open()
        time.sleep(2)
        assert page.is_element_present('guide_list') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = ChannelPayrollPage() #STEP 13
        page.open()
        time.sleep(2)
        assert page.is_element_present('channel_payment_due') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = EventCalendarPage()#STEP 14
        page.open()
        assert page.is_element_present('date_picker') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = GuideBulAssignmentPage() #STEP 15
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = AddStartingLocationPage()#STEP 16
        page.open()
        assert page.is_element_present('location_name') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = TaxesReportPage() #STEP 17
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = AnalyticsDashboardPage() #STEP 18
        page.open()
        time.sleep(2)
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') == False
        page = EditCompanyPage()#STEP 19
        page.open()
        assert page.is_element_present('company_name_field') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = SelfProfilePage()#STEP 20
        page.open()
        assert page.is_element_present('first_name_field') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False
        page = CustomerListPage()#STEP 21
        page.open()
        assert page.is_element_present('add_customer_button') == True
        page = NoPermission()
        assert page.is_element_present('no_permission_alert') ==False