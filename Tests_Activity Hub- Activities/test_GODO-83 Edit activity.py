from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO83(BaseTest):
    def test_83(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys('AutoTest_')
        page.activity_actions.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('activity_actions'))
        page.edit_activity.click()
        page=AddEditActivityPage()
        for i in range(1, len(page.switchers)):
            if page.switchers[i].get_attribute("outerHTML") != switcher_OFF:
                page.switchers[i].click()
            else:
                continue
            break
        time.sleep(15)
        NewActivityName = ("TestEdit"+''.join(choice(digits) for i in range(4)))
        page.activity_name.clear()
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.clear()
        page.activity_url.send_keys(NewActivityURL)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
        select.select_by_visible_text(NewActivityStatus )
        select = Select(page.branch)
        NewActivityBranch = "Belarus Branch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Chris Falvey's Place"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Atlantic"
        select.select_by_visible_text(NewActivityTimezone)
        NewActivityDesription = 'This activity has been edited'
        page.activity_description.clear()
        page.activity_description.send_keys(NewActivityDesription)
        NewActivityCancellationPolicy = 'We can not cancel event'
        page.cancellation_policy.clear()
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivitySalesTax = '15'
        page.sales_tax.clear()
        page.sales_tax.send_keys(NewActivitySalesTax)
        NewActivityDurationDays = '1'
        page.activity_duration_days.clear()
        page.activity_duration_days.send_keys(NewActivityDurationDays)
        NewActivityDurationHours = '3'
        page.activity_duration_hours.clear()
        page.activity_duration_hours.send_keys(NewActivityDurationHours)
        NewActivityDurationMinutes = '45'
        page.activity_duration_minutes.clear()
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        select = Select(page.activity_color)
        NewActivityColor = "Water"
        select.select_by_visible_text(NewActivityColor)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '99'
        page.ticket_maximum.send_keys(NewActivityMaxTickets )
        page.sell_out_alert.click()
        select = Select(page.sell_out_alert)
        NewActivitySellOut = "90%"
        select.select_by_visible_text(NewActivitySellOut)
        page.alert_guide_upon_sellout.click()
        select = Select(page.alert_guide_upon_sellout)
        NewActivityGuideUponSellout = "Yes"
        select.select_by_visible_text(NewActivityGuideUponSellout)
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "2 h 00 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        NewActivityMinTickets = '2'
        page.ticket_minimum.clear()
        page.ticket_minimum.send_keys(NewActivityMinTickets)
        NewActivityNotmetAlert = '1'
        page.minimum_not_met_alert.clear()
        page.minimum_not_met_alert.send_keys(NewActivityNotmetAlert)
        NewActivityStopbookingNoSales = '2'
        page.stop_no_sales.clear()
        page.stop_no_sales.send_keys(NewActivityStopbookingNoSales)
        NewActivityFirstTicketType = "Child"
        page.first_ticket_type.clear()
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '12.59'
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        select = Select(page.first_guide)
        NewActivityFirstGuide = "Joseph Super"
        select.select_by_visible_text(NewActivityFirstGuide)
        select = Select(page.first_linked_activity)
        NewActivityLinked = "Test AT"
        select.select_by_visible_text(NewActivityLinked)
        NewActivityWhatIncluded = 'Nothing.'
        page.what_included.clear()
        page.what_included.send_keys(NewActivityWhatIncluded)
        NewActivityWhatKnow = 'You should know all'
        page.what_know.clear()
        page.what_know.send_keys(NewActivityWhatKnow)
        NewActivityWhatBring = 'Drink and eat'
        page.what_bring.clear()
        page.what_bring.send_keys(NewActivityWhatBring )
        select = Select(page.review_redirect)
        NewActivityStarsReview = "4 Stars"
        select.select_by_visible_text(NewActivityStarsReview)
        page.review_website.clear()
        page.review_website.send_keys(NewActivityURL)
        page.save_button.click()
        page = ActivityHubPage()
        page.show_inactive.click()
        page.search_activity_field.send_keys(NewActivityName)
        page.activity_actions.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('activity_actions'))
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_name.get_attribute('value') == NewActivityName
        assert page.activity_url.get_attribute('value')== NewActivityURL
        select = Select(page.activity_status)
        assert select.first_selected_option.text == NewActivityStatus
        select = Select(page.branch)
        assert select.first_selected_option.text == NewActivityBranch
        select = Select(page.starting_location)
        assert select.first_selected_option.text == NewActivityLocation
        select = Select(page.time_zone)
        assert select.first_selected_option.text == NewActivityTimezone
        assert page.activity_description.get_attribute('value') == NewActivityDesription
        assert page.cancellation_policy.get_attribute('value') == NewActivityCancellationPolicy
        assert page.sales_tax.get_attribute('value') == NewActivitySalesTax
        assert page.activity_duration_days.get_attribute('value') == NewActivityDurationDays
        assert page.activity_duration_hours.get_attribute('value') == NewActivityDurationHours
        assert page.activity_duration_minutes.get_attribute('value') == NewActivityDurationMinutes
        select = Select(page.activity_color)
        assert select.first_selected_option.text == NewActivityColor
        assert page.ticket_maximum.get_attribute('value') == NewActivityMaxTickets
        select = Select(page.sell_out_alert)
        assert select.first_selected_option.text == NewActivitySellOut
        select = Select(page.alert_guide_upon_sellout)
        assert select.first_selected_option.text == NewActivityGuideUponSellout
        select = Select(page.stop_booking_sold)
        assert select.first_selected_option.text == NewActivityStopbookingSold
        assert page.ticket_minimum.get_attribute('value') == NewActivityMinTickets
        assert page.minimum_not_met_alert.get_attribute('value') == NewActivityNotmetAlert
        assert page.stop_no_sales.get_attribute('value') == NewActivityStopbookingNoSales
        assert page.first_ticket_type.get_attribute('value') == NewActivityFirstTicketType
        assert page.first_ticket_price.get_attribute('value') == NewActivityFirstTicketPrice
        select = Select(page.first_guide)
        assert select.first_selected_option.text == NewActivityFirstGuide
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == NewActivityLinked
        assert page.what_included.get_attribute('value') == NewActivityWhatIncluded
        assert page.what_know.get_attribute('value') == NewActivityWhatKnow
        assert page.what_bring.get_attribute('value') == NewActivityWhatBring
        select = Select(page.review_redirect)
        assert select.first_selected_option.text == NewActivityStarsReview
        assert page.review_website.get_attribute('value') == NewActivityURL
        for i in range(0, len(page.switchers)):  #FAILED because of bug 2270
             assert page.switchers[i].get_attribute("outerHTML") == switcher_OFF
