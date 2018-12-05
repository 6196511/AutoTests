from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password, server, database, username, password
import pyodbc

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO599(BaseTest):
    def test_599(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage() #STEP1
        page.open()
        page.add_activity_button.click()#STEP2
        page=AddEditActivityPage()
        time.sleep(15)
        for i in range(0, len(page.switchers1)):#STEP3
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
        NewActivityName = ("AutoTestMinAlert" + ''.join(choice(digits) for i in range(4)))
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://" + NewActivityName + '.com')
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
        page.activity_description.send_keys(NewActivityDesription)
        NewActivityCancellationPolicy = 'We can not cancel event'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivitySalesTax = '15'
        page.sales_tax.send_keys(NewActivitySalesTax)
        NewActivityDurationDays = '0'
        page.activity_duration_days.send_keys(NewActivityDurationDays)
        NewActivityDurationHours = '2'
        page.activity_duration_hours.send_keys(NewActivityDurationHours)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        select = Select(page.activity_color)
        NewActivityColor = "Water"
        select.select_by_visible_text(NewActivityColor)
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
        page.ticket_minimum.send_keys(NewActivityMinTickets)
        NewActivityStopbookingNoSales = '2'
        page.stop_no_sales.send_keys(NewActivityStopbookingNoSales)
        NewActivityFirstTicketType = "Child"
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '12.59'
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        select = Select(page.first_guide)
        NewActivityFirstGuide = "Joseph Super"
        select.select_by_visible_text(NewActivityFirstGuide)
        select = Select(page.first_linked_activity)
        NewActivityLinked = "Test AT"
        select.select_by_visible_text(NewActivityLinked)
        NewActivityWhatIncluded = 'Nothing.'
        page.what_included.send_keys(NewActivityWhatIncluded)
        NewActivityWhatKnow = 'You should know all'
        page.what_know.send_keys(NewActivityWhatKnow)
        NewActivityWhatBring = 'Drink and eat'
        page.what_bring.send_keys(NewActivityWhatBring)
        select = Select(page.review_redirect)
        NewActivityStarsReview = "4 Stars"
        select.select_by_visible_text(NewActivityStarsReview)
        page.review_website.send_keys(NewActivityURL)
        page.minimum_not_met_alert.send_keys('-1')#STEP4
        page.ticket_minimum.click()
        assert page.minimum_not_met_alert.get_attribute('value')=='0'
        page.minimum_not_met_alert.clear()#STEP5
        page.minimum_not_met_alert.send_keys('10000001')
        page.ticket_minimum.click()
        assert page.minimum_not_met_alert.get_attribute('value')=='100'
        page.minimum_not_met_alert.clear()#STEP6
        page.minimum_not_met_alert.send_keys('1')
        page.ticket_minimum.click()
        assert page.minimum_not_met_alert.get_attribute('value')=='1'
        page.save_button.click()
        page = ActivityHubPage()#STEP7
        time.sleep(5)
        page.show_inactive.click()
        time.sleep(10)
        page.search_activity_field.send_keys(NewActivityName)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        time.sleep(5)
        page = AddEditActivityPage()
        assert page.minimum_not_met_alert.get_attribute('value') == '1'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)#STEP8
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 activity_alert_minimumnotmet_hours FROM activity ORDER BY activity_id DESC")
        row = cursor.fetchone()
        assert row[0] == 1
