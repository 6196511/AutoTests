from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from navigation_bar import NavigationBar
from event_calendar import EventCalendarPage
from activity_hub_page import ActivityHubPage
from customer_charge import CustomerChargePage
from activity_page import AddEditActivityPage
from admin_booking import AdminBookingPage
import random
from datetime import date, datetime
from selenium.webdriver.support.ui import Select
from dateutil.relativedelta import relativedelta
import pyodbc
import time
from creds import admin_login, admin_password, database, server, username, password

ActivityName= 'Dresden Tour'
EventHeaderDateTimeList = []
ActivityTimezone = 'PT'
CC_Number = '4242424242424242'
ExpDate = '1020'
CVC = '303'
CCZip ='12345'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO567(BaseTest):
    def test_567(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ActivityHubPage()
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(ActivityName)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.sales_tax.get_attribute("value") == '0 %':
            page.cancel_button.click()
        else:
            page.sales_tax.clear()
            page.sales_tax.send_keys('0')
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()  # STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)  # STEP2
        page.first_tickets_type.send_keys('1')# STEP3
        page.second_tickets_type.send_keys('1')
        time.sleep(5)
        assert page.ticket_total.get_attribute("innerText")=='$150.00'
        assert page.discount.get_attribute("innerText") == '- $0.00'
        assert page.giftcertificate.get_attribute("innerText") == '- $0.00'
        assert page.taxes.get_attribute("innerText") == '$0.00'
        assert page.booking_fee.get_attribute("innerText") == '$0.00'
        assert page.grand_total.get_attribute("innerText") == '$150.00'
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 27))  # STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(8, 11))
        minutes_values = '00'
        EventTimeMinutes = minutes_values
        timeday = 'AM'
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)  # STEP5
        time.sleep(5)
        page.enter_customer_information_button.click()  # STEP6
        time.sleep(5)
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName)  # STEP5
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        time.sleep(10)
        page.complete_booking_button.click()
        time.sleep(7)
        select = Select(page.payment_type_list)
        PaymentType = "Credit Card"  # STEP8
        select.select_by_visible_text(PaymentType)
        select = Select(page.credit_card_list)
        time.sleep(5)
        select.select_by_visible_text('New Card')
        time.sleep(5)
        get_driver().switch_to.frame(page.stripe)
        page.card_number_input.send_keys(CC_Number)
        page.card_date_input.send_keys(ExpDate)
        page.card_cvc_input.send_keys(CVC)
        page.card_zip_input.send_keys(CCZip)
        get_driver().switch_to.default_content()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage()  # STEP10
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
        for ticket in page.day_slots:  # STEP11
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                else:
                    continue
            break
        time.sleep(6)
        assert page.customer_name_link.get_attribute('textContent') == NewFullName
        assert page.email_link.get_attribute('innerText') == NewEmail
        assert '1 Adult' in page.manifest_tickets.get_attribute("innerText")
        assert '1 Child' in page.manifest_tickets.get_attribute("innerText")
        assert page.paid_link.get_attribute("innerText") == 'Paid in Full : $150.00 '
        page.paid_link.click() #STEP12
        page = CustomerChargePage()
        time.sleep(5)
        assert page.ticket_total.get_attribute('textContent') == '$150.00'
        assert page.boooking_fee.get_attribute('textContent') == '$0.00'
        assert page.taxes.get_attribute('textContent') == '$0.00'
        assert page.grand_total.get_attribute('textContent') == '$150.00'
        assert page.total_charges.get_attribute('textContent') == '$150.00'
        assert page.total_due.get_attribute('textContent') == '$0.00'
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)  # STEP 13
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM charge ORDER BY charge_id DESC")
        row = cursor.fetchone()
        assert row[12] == 0 # charge_amount_tax
        assert row[13] == 150  # charge_amount_total
        assert row[9] == 'creditcard'  # charge_type
        assert 'OK|CHARGED|' in row[14] #charge_resulttext
        cursor.execute("SELECT TOP 1 * FROM q_charge_ex ORDER BY charge_id DESC")  # STEP14
        row = cursor.fetchone()
        assert row[12] == 0 # charge_amount_tax
        assert row[13] == 150  # charge_amount_total
        assert row[9] == 'creditcard'  # charge_type
        assert 'OK|CHARGED|' in row[14] #charge_resulttext