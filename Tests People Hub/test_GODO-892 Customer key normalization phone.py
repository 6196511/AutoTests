from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from customer_list import CustomerListPage
from selenium.webdriver.support.ui import Select
import time
import random
from admin_booking import AdminBookingPage
from navigation_bar import NavigationBar
from dateutil.relativedelta import relativedelta
from event_calendar import EventCalendarPage
from datetime import date, datetime
from random import choice
from creds import admin_login, admin_password, server, database, username, password
from pytz import timezone
import string
import re
import pyodbc


ActivityName = "_AutoTest200918"
ActivityTimezone = 'AT'
AdultTickets = '1'
AdultTicketPrice = '$0.90'
AT = timezone('America/Glace_Bay')


class BaseTest(object):
    def teardown_class(self):
        close_driver()


class Test_GODO892(BaseTest):
    def test_892(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click() #STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)#STEP2
        page.first_tickets_type.send_keys(AdultTickets) #STEP3
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 28)) #STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 11))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone) #STEP5
        time.sleep(5)
        page.enter_customer_information_button.click() #STEP6
        first_names = (
        'Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James', 'Bob', 'Ivan', 'Tim', 'Chris', 'Jim',
        'Pahom', 'Vlad', 'Paul')
        NewFirstName = random.choice(first_names)
        page.first_name.send_keys(NewFirstName) #STEP7
        last_names = (
        'Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff', 'Green', 'Clinton', 'Jameson',
        'Last', 'Sergeff', 'Madison')
        NewLastName = random.choice(last_names)
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        # NewPhone = (''.join(choice(string.ascii_letters+string.digits+string.punctuation) for i in range(15)))
        NewPhone = (''.join(choice(string.ascii_letters) for i in range(2))+''.join(choice(string.punctuation) for i in range(3))+''.join(choice(string.digits) for i in range(3))+''.join(choice(string.punctuation) for i in range(3))+''.join(choice(string.digits) for i in range(4))+''.join(choice(string.punctuation) for i in range(2))+''.join(choice(string.digits) for i in range(2)))
        page.phone_number.send_keys(NewPhone)
        page.complete_booking_button.click()
        time.sleep(7)
        select = Select(page.payment_type_list)
        PaymentType = "Cash"  # STEP8
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage() #STEP10
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        page.date_picker.click()
        time.sleep(2)
        page.date_picker_next.click()
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(EventDate):
                page.days_date_picker[i].click()
            else:
                continue
            break
        page.day_button.click()
        time.sleep(6)
        EventTime = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday))
        assert str(NewFullDate) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots: #STEP11
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                else:
                    continue
            break
        time.sleep(6)
        assert page.customer_name_link.get_attribute('textContent') == NewFullName
        assert page.phone_link.get_attribute('textContent') == ' '+NewPhone+' '
        page.customer_name_link.click()  # STEP12
        page = CustomerListPage()
        assert page.customer_name_info.get_attribute('textContent')==NewFullName+"'s"
        assert page.phone_info.get_attribute('innerText')==NewPhone
        assert page.email_info.get_attribute('innerText') == 'Not Saved'
        assert page.zip_info.get_attribute('innerText')== 'Not Saved'
        assert page.state_info.get_attribute('innerText')=='Not Saved'
        assert page.address_info.get_attribute('innerText') == 'Not Saved'
        assert page.timeline_tickets_title.get_attribute('textContent') == 'Purchased Tickets for the '+''.join(ActivityName)
        assert EventTimeWithZone and NewFullDate in page.timeline_event.get_attribute('textContent')
        assert page.timeline_tickets.get_attribute('textContent') == AdultTickets+' Tickets | ' +''.join(AdultTicketPrice)+' '
        page.activities_tab_link.click()
        time.sleep(5)
        assert page.activities_tab_title.get_attribute('innerText') == ActivityName
        assert page.activities_tickets.get_attribute('innerText') == AdultTickets + ' tickets | ' + ''.join(AdultTicketPrice)
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password) #STEP 14
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = cursor.fetchone()
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[10] == NewPhone
        assert row[17] == re.sub("\D", "", NewPhone)  #CustomerKey





