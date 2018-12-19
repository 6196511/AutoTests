from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
import time
from creds import admin_login, admin_password, server, database, username, password
from random import choice
from string import digits
import pyodbc

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO594(BaseTest):

    def test_594(self):
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
        NewActivityName = ("AutoTest594_"+''.join(choice(digits) for i in range(4)))#STEP3
        page.activity_name.send_keys(NewActivityName)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
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
        page.ticket_minimum.send_keys('-1') #STEP4
        page.ticket_maximum.click()
        assert page.ticket_minimum.get_attribute('value')=='0'
        page.ticket_minimum.send_keys('10000001') #STEP5
        page.ticket_maximum.click()
        assert page.ticket_minimum.get_attribute('value')=='10000000'
        page.ticket_minimum.clear()#STEP6
        page.ticket_minimum.send_keys('1')
        page.ticket_maximum.click()
        assert page.ticket_minimum.get_attribute('value')=='1'
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        time.sleep(5)
        page.show_inactive.click()
        page.search_activity_field.send_keys(NewActivityName) #STEP7
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.ticket_minimum.get_attribute('value') == '1'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password) #STEP8
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 activity_mintickets, activity_name FROM activity ORDER BY activity_id DESC")
        row = cursor.fetchone()
        assert row[0]==1
        assert row[1] == NewActivityName
