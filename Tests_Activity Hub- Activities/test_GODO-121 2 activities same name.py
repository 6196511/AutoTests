from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
from selenium.webdriver.support.wait import WebDriverWait
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO121(BaseTest):
    def test_121(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.show_inactive.click()
        page.search_activity_field.send_keys('TestEdit')
        ExistedActivityName = page.activity_title.get_attribute("textContent")
        page.add_activity_button.click()
        time.sleep(10)
        page = AddEditActivityPage()
        page.activity_name.send_keys(ExistedActivityName)
        page.activity_url.click()
        time.sleep(5)
        assert page.is_element_present('alert_message') == True
        select = Select(page.activity_status)
        NewActivityStatus = "Active"
        select.select_by_visible_text(NewActivityStatus )
        select = Select(page.branch)
        NewActivityBranch = "First branch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Hotel California"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Central"
        select.select_by_visible_text(NewActivityTimezone)
        NewActivityCancellationPolicy = 'We can cancel an event any time we want.'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivityDurationDays = '0'
        page.activity_duration_days.send_keys(NewActivityDurationDays)
        NewActivityDurationHours = '2'
        page.activity_duration_hours.send_keys(NewActivityDurationHours)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "1h 30 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        NewActivityFirstTicketType = "Adult"
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '9.99'
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        page.save_button.click()
        time.sleep(5)
        assert page.is_element_present('alert_message') == True #failed - bug 2432
        assert get_driver().current_url == page.url #failed - bug 2432












