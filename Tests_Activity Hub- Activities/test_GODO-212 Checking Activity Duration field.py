from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO212(BaseTest):
    def test_212(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=AddEditActivityPage() #STEP1
        page.open()
        time.sleep(5)
        for i in range(0, len(page.switchers1)):
            if page.switchers1[i].get_attribute("outerHTML") != switcher_OFF:
                page.switchers1[i].click()
            else:
                continue
        for i in range(0, len(page.switchers2)):
            if page.switchers2[i].get_attribute("outerHTML") != switcher_OFF:
                page.switchers2[i].click()
            else:
                continue
        if page.switcher_minimum_enforce.get_attribute("outerHTML") != switcher_OFF:
            page.switcher_minimum_enforce.click()
        NewActivityName = ("AutoTestDuration" + ''.join(choice(digits) for i in range(4)))
        page.activity_name.clear()
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://" + NewActivityName + '.com')
        page.activity_url.clear()
        page.activity_url.send_keys(NewActivityURL)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
        select.select_by_visible_text(NewActivityStatus)
        select = Select(page.branch)
        NewActivityBranch = "HA Branch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Chris Falvey's Place"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Hawaii"
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
        select = Select(page.activity_color)
        NewActivityColor = "Water"
        select.select_by_visible_text(NewActivityColor)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '99'
        page.ticket_maximum.send_keys(NewActivityMaxTickets)
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
        page.what_bring.send_keys(NewActivityWhatBring)
        select = Select(page.review_redirect)
        NewActivityStarsReview = "4 Stars"
        select.select_by_visible_text(NewActivityStarsReview)
        page.review_website.clear()
        page.review_website.send_keys(NewActivityURL)
        page.save_button.click() #STEP 3
        time.sleep(10)
        assert page.is_element_present('duration_alert') == True
        assert page.duration_alert.get_attribute('outerText') == 'Activity Duration should be greater than 0.'
        page.activity_duration_days.clear()#STEP 4
        page.activity_duration_days.send_keys('-1')
        page.activity_duration_hours.clear()
        page.activity_duration_hours.send_keys('-1')
        page.activity_duration_minutes.clear()
        page.activity_duration_minutes.send_keys('-1')
        assert page.activity_duration_days.get_attribute('value') == '1'
        assert page.activity_duration_hours.get_attribute('value') == '1'
        assert page.activity_duration_minutes.get_attribute('value') == '1'
        page.activity_duration_days.clear()#STEP 5
        page.activity_duration_days.send_keys('1')
        page.activity_duration_hours.clear()
        page.activity_duration_minutes.clear()
        assert page.activity_duration_days.get_attribute('value') == '1'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName) #STEP6
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        for i in range(0, len(page.switchers1)):
             assert page.switchers1[i].get_attribute("outerHTML") == switcher_OFF
        for i in range(0, len(page.switchers2)):
             assert page.switchers2[i].get_attribute("outerHTML") == switcher_OFF
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF
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
        assert page.sales_tax.get_attribute('value') == NewActivitySalesTax+' %'
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
        assert page.activity_duration_days.get_attribute('value') == '1'
        assert page.activity_duration_hours.get_attribute('value') == '0'
        assert page.activity_duration_minutes.get_attribute('value') == '0'
        page.activity_duration_days.clear()#STEP7
        page.activity_duration_hours.send_keys('1')
        assert page.activity_duration_hours.get_attribute('value') == '1'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName) #STEP8
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_duration_days.get_attribute('value') == '0'
        assert page.activity_duration_hours.get_attribute('value') == '1'
        assert page.activity_duration_minutes.get_attribute('value') == '0'
        page.activity_duration_hours.clear()#STEP9
        page.activity_duration_minutes.send_keys('1')
        assert page.activity_duration_minutes.get_attribute('value') == '1'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        get_driver().refresh()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName) #STEP10
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_duration_days.get_attribute('value') == '0'
        assert page.activity_duration_hours.get_attribute('value') == '0'
        assert page.activity_duration_minutes.get_attribute('value') == '1'
        page.activity_duration_days.clear()#Step11
        page.activity_duration_days.send_keys('14')
        page.activity_duration_hours.clear()
        page.activity_duration_hours.send_keys('23')
        page.activity_duration_minutes.clear()
        page.activity_duration_minutes.send_keys('59')
        assert page.activity_duration_days.get_attribute('value') == '14'
        assert page.activity_duration_hours.get_attribute('value') == '23'
        assert page.activity_duration_minutes.get_attribute('value') == '59'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName) #STEP12
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_duration_days.get_attribute('value') == '14'
        assert page.activity_duration_hours.get_attribute('value') == '23'
        assert page.activity_duration_minutes.get_attribute('value') == '59'
        page.activity_duration_days.clear()#Step13
        page.activity_duration_days.send_keys('15')
        page.activity_duration_hours.clear()
        page.activity_duration_hours.send_keys('24')
        page.activity_duration_minutes.clear()
        page.activity_duration_minutes.send_keys('60')
        assert page.activity_duration_days.get_attribute('value') == '15'
        assert page.activity_duration_hours.get_attribute('value') == '24'
        assert page.activity_duration_minutes.get_attribute('value') == '60'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName) #STEP14
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_duration_days.get_attribute('value') == '16'
        assert page.activity_duration_hours.get_attribute('value') == '1'
        assert page.activity_duration_minutes.get_attribute('value') == '0'
