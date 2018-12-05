from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
import time
from creds import admin_login, admin_password
from random import choice
from string import digits

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO600(BaseTest):

    def test_600(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage() #STEP1
        page.open()
        page.add_activity_button.click() #STEP2
        page=AddEditActivityPage()
        time.sleep(5)
        assert page.switchers1[0].get_attribute("outerHTML") == switcher_OFF
        page.stop_no_sales.send_keys('-1')#STEP3
        page.minimum_not_met_alert.click()
        assert page.stop_no_sales.get_attribute('value')=='0'
        page.stop_no_sales.send_keys('10000001')#STEP4
        page.minimum_not_met_alert.click()
        assert page.stop_no_sales.get_attribute('value')=='100'
        page.stop_no_sales.clear()#STEP5
        page.stop_no_sales.send_keys('1')
        page.minimum_not_met_alert.click()
        assert page.stop_no_sales.get_attribute('value')=='1'
        NewActivityName = ("AutoTest600_" + ''.join(choice(digits) for i in range(4)))
        page.activity_name.send_keys(NewActivityName)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
        select.select_by_visible_text(NewActivityStatus)
        select = Select(page.branch)
        NewActivityBranch = "AlexeyBranch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Hotel California"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Pacific"
        select.select_by_visible_text(NewActivityTimezone)
        NewActivityCancellationPolicy = 'We can cancel an event any time we want.'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '100'
        page.ticket_maximum.send_keys(NewActivityMaxTickets)
        NewActivityFirstTicketType = "Adult"
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '9.99'
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "15 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        page.search_activity_field.send_keys(NewActivityName)  # STEP6
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.switchers1[0].get_attribute("outerHTML") == switcher_OFF
        assert page.stop_no_sales.get_attribute('value') == '1'
        page.switchers1[0].click()#STEP8
        assert page.switchers1[0].get_attribute("outerHTML") != switcher_OFF
        assert page.stop_no_sales.get_attribute('value') == ''
        assert page.stop_no_sales.is_enabled()==False
        page.save_button.click()#STEP9
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        page.search_activity_field.send_keys(NewActivityName)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.switchers1[0].get_attribute("outerHTML") != switcher_OFF
        assert page.stop_no_sales.is_enabled() == False