from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

ActivityNameList = []

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO82_83_84(BaseTest):
    def test_82(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.add_activity_button.click()
        page=AddEditActivityPage()
        time.sleep(5)
        for i in range(1, len(page.switchers1)):
            page.switchers1[i].click()
        for i in range(0, len(page.switchers2)):
            page.switchers2[i].click()
        page.switcher_minimum_enforce.click()
        time.sleep(10)
        NewActivityName = ("AutoTest_"+''.join(choice(digits) for i in range(4)))
        ActivityNameList.append(NewActivityName)
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.send_keys(NewActivityURL)
        select = Select(page.activity_status)
        NewActivityStatus = "Active"
        select.select_by_visible_text(NewActivityStatus )
        select = Select(page.branch)
        NewActivityBranch = "AlexeyBranch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Hotel California"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Pacific"
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
        select = Select(page.first_ticket_viator)
        NewActivityFirstViatorType = "Adult"
        select.select_by_visible_text(NewActivityFirstViatorType)
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
        time.sleep(5)
        page.activity_actions.click()
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
        assert page.sales_tax.get_attribute('value') == NewActivitySalesTax+' %'
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
        assert select.first_selected_option.text == NewActivityStopbookingSold+' '
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
        for i in range(1, len(page.switchers2)):
             assert page.switchers2[i].get_attribute("outerHTML") != switcher_OFF
        assert page.switchers1[0].get_attribute("outerHTML") == switcher_OFF
        assert page.switchers1[1].get_attribute("outerHTML") != switcher_OFF
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") != switcher_OFF
        select = Select(page.first_ticket_viator)
        assert select.first_selected_option.text == NewActivityFirstViatorType

    def test_83(self):
        page=ActivityHubPage()
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(ActivityNameList[0])
        time.sleep(5)
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('activity_actions'))
        page.activity_actions.click()
        page.edit_activity.click()
        page=AddEditActivityPage()
        time.sleep(15)
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
        NewActivityName = ("TestEdit"+''.join(choice(digits) for i in range(4)))
        ActivityNameList.append(NewActivityName)
        page.activity_name.clear()
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.clear()
        page.activity_url.send_keys(NewActivityURL)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
        select.select_by_visible_text(NewActivityStatus )
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
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(ActivityNameList[1])
        time.sleep(5)
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
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

    def test_84(self):
        page = ActivityHubPage()
        page.open()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(ActivityNameList[1])
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page=AddEditActivityPage()
        time.sleep(15)
        OldActivityName = page.activity_name.get_attribute('value')
        OldActivityURL = page.activity_url.get_attribute('value')
        select = Select(page.activity_status)
        OldActivityStatus = select.first_selected_option.text
        select = Select(page.time_zone)
        OldActivityTimezone = select.first_selected_option.text
        select = Select(page.branch)
        OldActivityBranch = select.first_selected_option.text
        select = Select(page.starting_location)
        OldActivityLocation = select.first_selected_option.text
        OldActivityDesription = page.activity_description.get_attribute('value')
        OldActivityCancellationPolicy = page.cancellation_policy.get_attribute('value')
        OldActivitySalesTax = page.sales_tax.get_attribute('value')
        OldActivityDurationDays = page.activity_duration_days.get_attribute('value')
        OldActivityDurationHours = page.activity_duration_hours.get_attribute('value')
        OldActivityDurationMinutes = page.activity_duration_minutes.get_attribute('value')
        select = Select(page.activity_color)
        OldActivityColor = select.first_selected_option.text
        OldActivityMaxTickets = page.ticket_maximum.get_attribute('value')
        select = Select(page.sell_out_alert)
        OldActivitySellOut = select.first_selected_option.text
        select = Select(page.alert_guide_upon_sellout)
        OldActivityGuideUponSellout = select.first_selected_option.text
        select = Select(page.stop_booking_sold)
        OldActivityStopbookingSold = select.first_selected_option.text
        OldActivityMinTickets = page.ticket_minimum.get_attribute('value')
        OldActivityNotmetAlert = page.minimum_not_met_alert.get_attribute('value')
        OldActivityStopbookingNoSales = page.stop_no_sales.get_attribute('value')
        OldActivityFirstTicketType = page.first_ticket_type.get_attribute('value')
        OldActivityFirstTicketPrice = page.first_ticket_price.get_attribute('value')
        select = Select(page.first_guide)
        OldActivityFirstGuide = select.first_selected_option.text
        select = Select(page.first_linked_activity)
        OldActivityLinked = select.first_selected_option.text
        OldActivityWhatIncluded = page.what_included.get_attribute('value')
        OldActivityWhatKnow = page.what_know.get_attribute('value')
        OldActivityWhatBring = page.what_bring.get_attribute('value')
        select = Select(page.review_redirect)
        OldActivityStarsReview = select.first_selected_option.text
        OldReviewURL = page.review_website.get_attribute('value')
        select = Select(page.first_ticket_viator)
        OldActivityFirstViatorType = select.first_selected_option.text
        OldActivityName = page.activity_name.get_attribute('value')
        for i in range(0, len(page.switchers1)):
            if page.switchers1[i].get_attribute("outerHTML") == switcher_OFF:
                page.switchers1[i].click()
            else:
                continue
        for i in range(0, len(page.switchers2)):
            if page.switchers2[i].get_attribute("outerHTML") == switcher_OFF:
                page.switchers2[i].click()
            else:
                continue
        if page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF:
            page.switcher_minimum_enforce.click()
        NewActivityName = ("NoEdit"+''.join(choice(digits) for i in range(4)))
        page.activity_name.clear()
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.clear()
        page.activity_url.send_keys(NewActivityURL)
        select = Select(page.activity_status)
        NewActivityStatus = "Private Party"
        select.select_by_visible_text(NewActivityStatus )
        select = Select(page.time_zone)
        NewActivityTimezone = "Alaska"
        select.select_by_visible_text(NewActivityTimezone)
        select = Select(page.branch)
        NewActivityBranch = "Nealon Branch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Bud Rip's"
        select.select_by_visible_text(NewActivityLocation)
        NewActivityDesription = 'This activity has been edited CANCEL'
        page.activity_description.clear()
        page.activity_description.send_keys(NewActivityDesription)
        NewActivityCancellationPolicy = 'We can not cancel event CANCEL'
        page.cancellation_policy.clear()
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivitySalesTax = '84'
        page.sales_tax.clear()
        page.sales_tax.send_keys(NewActivitySalesTax)
        NewActivityDurationDays = '2'
        page.activity_duration_days.clear()
        page.activity_duration_days.send_keys(NewActivityDurationDays)
        NewActivityDurationHours = '16'
        page.activity_duration_hours.clear()
        page.activity_duration_hours.send_keys(NewActivityDurationHours)
        NewActivityDurationMinutes = '45'
        page.activity_duration_minutes.clear()
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        select = Select(page.activity_color)
        NewActivityColor = "Topaz"
        select.select_by_visible_text(NewActivityColor)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '343'
        page.ticket_maximum.send_keys(NewActivityMaxTickets)
        select = Select(page.sell_out_alert)
        NewActivitySellOut = "60%"
        select.select_by_visible_text(NewActivitySellOut)
        select = Select(page.alert_guide_upon_sellout)
        NewActivityGuideUponSellout = "No"
        select.select_by_visible_text(NewActivityGuideUponSellout)
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "10h 30 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        NewActivityMinTickets = '23'
        page.ticket_minimum.clear()
        page.ticket_minimum.send_keys(NewActivityMinTickets)
        NewActivityNotmetAlert = '5'
        page.minimum_not_met_alert.clear()
        page.minimum_not_met_alert.send_keys(NewActivityNotmetAlert)
        NewActivityFirstTicketType = "Senior"
        page.first_ticket_type.clear()
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '111.11'
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        select = Select(page.first_ticket_viator)
        NewActivityFirstViatorType = "Infant"
        select.select_by_visible_text(NewActivityFirstViatorType)
        select = Select(page.first_guide)
        NewActivityFirstGuide = "Peter Petrov"
        select.select_by_visible_text(NewActivityFirstGuide)
        select = Select(page.first_linked_activity)
        NewActivityLinked = "Test MT"
        select.select_by_visible_text(NewActivityLinked)
        NewActivityWhatIncluded = 'All INCLUDED.'
        page.what_included.clear()
        page.what_included.send_keys(NewActivityWhatIncluded)
        NewActivityWhatKnow = 'CANCEL BUTTON CHECK'
        page.what_know.clear()
        page.what_know.send_keys(NewActivityWhatKnow)
        NewActivityWhatBring = 'NOTHING'
        page.what_bring.clear()
        page.what_bring.send_keys(NewActivityWhatBring)
        select = Select(page.review_redirect)
        NewActivityStarsReview = "3 Stars"
        select.select_by_visible_text(NewActivityStarsReview)
        NewReviewURL = 'http://tut.by'
        page.review_website.clear()
        page.review_website.send_keys(NewReviewURL)
        page.cancel_button.click()
        page = ActivityHubPage()
        page.show_inactive.click()
        page.search_activity_field.send_keys(NewActivityName)
        time.sleep(5)
        assert page.is_element_present('activity_actions') == False
        get_driver().refresh()
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(OldActivityName)
        time.sleep(5)
        page.activity_actions.click()
        text = page.activity_title.get_attribute("textContent")
        assert text == OldActivityName
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_name.get_attribute('value') == OldActivityName
        assert page.activity_url.get_attribute('value')== OldActivityURL
        select = Select(page.activity_status)
        assert select.first_selected_option.text == OldActivityStatus
        select = Select(page.branch)
        assert select.first_selected_option.text == OldActivityBranch
        select = Select(page.starting_location)
        assert select.first_selected_option.text == OldActivityLocation
        select = Select(page.time_zone)
        assert select.first_selected_option.text == OldActivityTimezone
        assert page.activity_description.get_attribute('value') == OldActivityDesription
        assert page.cancellation_policy.get_attribute('value') == OldActivityCancellationPolicy
        assert page.sales_tax.get_attribute('value') == OldActivitySalesTax
        assert page.activity_duration_days.get_attribute('value') == OldActivityDurationDays
        assert page.activity_duration_hours.get_attribute('value') == OldActivityDurationHours
        assert page.activity_duration_minutes.get_attribute('value') == OldActivityDurationMinutes
        select = Select(page.activity_color)
        assert select.first_selected_option.text == OldActivityColor
        assert page.ticket_maximum.get_attribute('value') == OldActivityMaxTickets
        select = Select(page.sell_out_alert)
        assert select.first_selected_option.text == OldActivitySellOut
        select = Select(page.alert_guide_upon_sellout)
        assert select.first_selected_option.text == OldActivityGuideUponSellout
        select = Select(page.stop_booking_sold)
        assert select.first_selected_option.text == OldActivityStopbookingSold
        assert page.ticket_minimum.get_attribute('value') == OldActivityMinTickets
        assert page.minimum_not_met_alert.get_attribute('value') == OldActivityNotmetAlert
        assert page.stop_no_sales.get_attribute('value') == OldActivityStopbookingNoSales
        assert page.first_ticket_type.get_attribute('value') == OldActivityFirstTicketType
        assert page.first_ticket_price.get_attribute('value') == OldActivityFirstTicketPrice
        select = Select(page.first_guide)
        assert select.first_selected_option.text == OldActivityFirstGuide
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == OldActivityLinked
        assert page.what_included.get_attribute('value') == OldActivityWhatIncluded
        assert page.what_know.get_attribute('value') == OldActivityWhatKnow
        assert page.what_bring.get_attribute('value') == OldActivityWhatBring
        select = Select(page.review_redirect)
        assert select.first_selected_option.text == OldActivityStarsReview
        assert page.review_website.get_attribute('value') == OldReviewURL
        for i in range(0, len(page.switchers1)):
             assert page.switchers1[i].get_attribute("outerHTML") == switcher_OFF
        for i in range(0, len(page.switchers2)):
             assert page.switchers2[i].get_attribute("outerHTML") == switcher_OFF
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF
        select = Select(page.first_ticket_viator)
        assert select.first_selected_option.text == OldActivityFirstViatorType
