from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO82(BaseTest):
    def test_82(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys('login')
        page.password_field.send_keys('password')
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.add_activity_button.click()
        page=AddEditActivityPage()
        time.sleep(15)
        NewActivityName = ("AutoTest"+''.join(choice(digits) for i in range(4)))
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.send_keys(NewActivityURL)
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
        NewActivityDesription = 'The activity is created automatically.'
        page.activity_description.send_keys(NewActivityDesription)
        NewActivityCancellationPolicy = 'We can cancel an event any time we want.'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivitySalesTax = '5'
        page.sales_tax.send_keys(NewActivitySalesTax)
        NewActivityDurationDays = '0'
        page.activity_duration_days.send_keys(NewActivityDurationDays)
        NewActivityDurationHours = '2'
        page.activity_duration_hours.send_keys(NewActivityDurationHours)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        select = Select(page.activity_color)
        NewActivityColor = "Alabaster"
        select.select_by_visible_text(NewActivityColor)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '100'
        page.ticket_maximum.send_keys(NewActivityMaxTickets )
        page.sell_out_alert.click()
        select = Select(page.sell_out_alert)
        NewActivitySellOut = "80%"
        select.select_by_visible_text(NewActivitySellOut)
        page.alert_guide_upon_sellout.click()
        select = Select(page.alert_guide_upon_sellout)
        NewActivityGuideUponSellout = "No"
        select.select_by_visible_text(NewActivityGuideUponSellout)
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "1h 30 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        NewActivityMinTickets = '20'
        page.ticket_minimum.send_keys(NewActivityMinTickets)
        NewActivityNotmetAlert = '10'
        page.minimum_not_met_alert.send_keys(NewActivityNotmetAlert)
        NewActivityStopbookingNoSales = '10'
        page.stop_no_sales.send_keys(NewActivityStopbookingNoSales)
        NewActivityFirstTicketType = "Adult"
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '9.99'
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        select = Select(page.first_guide)
        NewActivityFirstGuide = "Holly Flat"
        select.select_by_visible_text(NewActivityFirstGuide)
        select = Select(page.first_linked_activity)
        NewActivityLinked = "AlertTest1"
        select.select_by_visible_text(NewActivityLinked)
        NewActivityWhatIncluded = 'Good mood.'
        page.what_included.send_keys(NewActivityWhatIncluded)
        NewActivityWhatKnow = 'Everything will be fine.'
        page.what_know.send_keys(NewActivityWhatKnow)
        NewActivityWhatBring = 'Just bring a lot of money.'
        page.what_bring.send_keys(NewActivityWhatBring )
        select = Select(page.review_redirect)
        NewActivityStarsReview = "5 Stars"
        select.select_by_visible_text(NewActivityStarsReview)
        page.review_website.send_keys(NewActivityURL)
        page.save_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(NewActivityName)
        page.activity_actions.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('activity_actions'))
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
        page.edit_activity.click()
        # assert page.is_element_present('activity_actions')
        # page.activity_actions.click()
        # wait = WebDriverWait(get_driver(), 15)
        # wait.until(lambda driver: page.is_element_present('edit_activity'))
        # page.edit_activity.click()
