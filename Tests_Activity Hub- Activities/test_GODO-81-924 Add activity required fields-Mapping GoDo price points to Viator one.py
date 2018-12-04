from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
import random
import time
from creds import admin_login, admin_password
from random import choice
from string import digits

NewFirstViatorType = "Adult"
NewSecondViatorType = "Child"
NewThirdViatorType = "Youth"
NewFourthViatorType = "Senior"
ActivityNameList =[]

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO81_924(BaseTest):

    def test_81(self):
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
        NewActivityName = ("AutoTest81_"+''.join(choice(digits) for i in range(4)))
        ActivityNameList.append(NewActivityName)
        page.activity_name.send_keys(NewActivityName)
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
        NewActivityCancellationPolicy = 'We can cancel an event any time we want.'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '100'
        page.ticket_maximum.send_keys(NewActivityMaxTickets )
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
        page.search_activity_field.send_keys(NewActivityName)
        time.sleep(5)
        page.activity_actions.click()
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_name.get_attribute('value') == NewActivityName
        select = Select(page.activity_status)
        assert select.first_selected_option.text == NewActivityStatus
        select = Select(page.branch)
        assert select.first_selected_option.text == NewActivityBranch
        select = Select(page.starting_location)
        assert select.first_selected_option.text == NewActivityLocation
        select = Select(page.time_zone)
        assert select.first_selected_option.text == NewActivityTimezone
        assert page.cancellation_policy.get_attribute('value') == NewActivityCancellationPolicy
        assert page.activity_duration_minutes.get_attribute('value') == NewActivityDurationMinutes
        assert page.ticket_maximum.get_attribute('value') == NewActivityMaxTickets
        assert page.first_ticket_type.get_attribute('value') == NewActivityFirstTicketType
        assert page.first_ticket_price.get_attribute('value') == NewActivityFirstTicketPrice
        for i in range(0, len(page.switchers1)):
            assert page.switchers1[i].get_attribute("outerHTML") == switcher_OFF
        for i in range(0, len(page.switchers2)):
            assert page.switchers2[i].get_attribute("outerHTML") == switcher_OFF
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF
        select = Select(page.stop_booking_sold)
        assert select.first_selected_option.text == NewActivityStopbookingSold

    def test_924(self):
        page=ActivityHubPage() #STEP1
        page.open()
        page.search_activity_field.send_keys(ActivityNameList[0])  #STEP2
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        L=[]
        if page.is_element_present('second_ticket_type') == False and page.is_element_present('second_ticket_price') == False:  #STEP3
            page.add_ticket_type.click()
            time.sleep(5)
            NewActivitySecondTicketType = "Child"
            page.second_ticket_type.send_keys( NewActivitySecondTicketType)
            NewActivitySecondTicketPrice = '9.99'
            page.second_ticket_price.send_keys(NewActivitySecondTicketPrice)
        if page.switchers1[1].get_attribute("outerHTML") == switcher_OFF: #STEP4
            page.switchers1[1].click()
        time.sleep(5)
        assert page.first_ticket_type.is_displayed() and page.first_ticket_price.is_displayed() and page.first_ticket_viator.is_displayed()
        L.append(page.first_ticket_type.get_attribute('value'))
        assert page.second_ticket_type.is_displayed() and page.second_ticket_price.is_displayed() and page.second_ticket_viator.is_displayed()
        L.append(page.second_ticket_type.get_attribute('value'))
        if page.is_element_present('third_ticket_type') == True and page.is_element_present('third_ticket_price') == True:
            L.append(page.third_ticket_type.get_attribute('value'))
            assert page.third_ticket_type.is_displayed() and page.third_ticket_price.is_displayed() and page.third_ticket_viator.is_displayed()
        if page.is_element_present('fourth_ticket_type') == True and page.is_element_present('fourth_ticket_price') == True:
            L.append(page.fourth_ticket_type.get_attribute('value'))
            assert page.fourth_ticket_type.is_displayed() and page.fourth_ticket_price.is_displayed() and page.fourth_ticket_viator.is_displayed()
        select = Select(page.first_ticket_viator)#STEP5
        select.select_by_visible_text(NewFirstViatorType)
        page.save_button.click()#STEP6
        assert page.is_element_present('viator1_alert') == False
        assert page.is_element_present('viator2_alert') == True
        if len(L)>2:
            assert page.is_element_present('viator3_alert') == True
            assert page.viator3_alert.is_displayed()
        else:
            assert page.is_element_present('viator3_alert') == False
        if len(L)>3:
            assert page.is_element_present('viator4_alert') == True
        else:
            assert page.is_element_present('viator4_alert') == False
        select = Select(page.second_ticket_viator)  # STEP7
        select.select_by_visible_text(NewSecondViatorType)
        if len(L) > 2:
            select = Select(page.third_ticket_viator)
            select.select_by_visible_text(NewThirdViatorType)
        if len(L) > 3:
            select = Select(page.fourth_ticket_viator)
            select.select_by_visible_text(NewFourthViatorType)
        time.sleep(5)
        page.second_ticket_type.click()
        time.sleep(5)
        assert page.is_element_present('viator1_alert') == False
        assert page.is_element_present('viator2_alert') == False
        assert page.is_element_present('viator3_alert') == False
        assert page.is_element_present('viator4_alert') == False
        time.sleep(5)
        page.save_button.click()# STEP8
        page = ActivityHubPage()
        page.search_activity_field.send_keys(ActivityNameList[0])# STEP9
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.switchers1[1].get_attribute("outerHTML") != switcher_OFF# STEP10
        select = Select(page.first_ticket_viator)
        assert select.first_selected_option.text == NewFirstViatorType
        select = Select(page.second_ticket_viator)
        assert select.first_selected_option.text == NewSecondViatorType
        if len(L) > 2:
            select = Select(page.third_ticket_viator)
            assert select.first_selected_option.text == NewThirdViatorType
        if len(L) > 3:
            select = Select(page.fourth_ticket_viator)
            assert select.first_selected_option.text == NewFourthViatorType
        select = Select(page.first_ticket_viator)#STEP11
        select.select_by_visible_text('----Choose Viator Ticket Type-----')
        time.sleep(3)
        assert select.first_selected_option.text == NewFirstViatorType
        page.switchers1[1].click()#STEP12
        time.sleep(3)
        assert page.switchers1[1].get_attribute("outerHTML") == switcher_OFF
        assert page.is_element_present('first_ticket_viator') == False
        assert page.is_element_present('second_ticket_viator') == False
        assert page.is_element_present('third_ticket_viator') == False
        assert page.is_element_present('fourth_ticket_viator') == False
        page.save_button.click()  # STEP13
        page = ActivityHubPage()
        page.search_activity_field.send_keys(ActivityNameList[0])  # STEP14
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.switchers1[1].get_attribute("outerHTML") == switcher_OFF # STEP15
        assert page.is_element_present('first_ticket_viator') == False
        assert page.is_element_present('second_ticket_viator') == False
        assert page.is_element_present('third_ticket_viator') == False
        assert page.is_element_present('fourth_ticket_viator') == False