from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from event_calendar import EventCalendarPage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from admin_booking import AdminBookingPage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

ActivityName= 'Spring Flowers Tour'
EventHeaderDateTimeList = []
CC_Number = '4242424242424242'
ExpDate = '1020'
CVC = '303'
CCZip ='12345'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO597(BaseTest):
    def test_597(self):
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
        if page.ticket_maximum.get_attribute("value") == '10':
            page.cancel_button.click()
        else:
            page.ticket_maximum.clear()
            page.ticket_maximum.send_keys('10')
            page.save_button.click()
        time.sleep(5)
        page = EventCalendarPage()  # STEP1
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        time.sleep(5)
        page.hide_events.click()
        time.sleep(5)
        page.event_tickets[0].click()
        time.sleep(5)
        for i in range(0, len(page.event_tickets)):
            if 'Ticket Sold: 0' not in page.manifest_title.get_attribute("innerText"):
                page.close_button.click()
                time.sleep(5)
                page.event_tickets[i + 1].click()
                time.sleep(5)
                continue
            else:
                time.sleep(5)
                EventHeaderDateTimeList.append(page.date_time_title.get_attribute('textContent'))
                page.add_booking_button.click()  # STEP2
            break
        time.sleep(5)
        page = AdminBookingPage()
        time.sleep(5)
        page.first_tickets_type.send_keys('5')  # STEP3
        time.sleep(5)
        page.second_tickets_type.send_keys('5')
        page.enter_customer_information_button.click()  # STEP6
        time.sleep(5)
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName)  # STEP7
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        time.sleep(10)
        page.complete_booking_button.click()
        time.sleep(5)
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('payment_type_list'))
        select = Select(page.payment_type_list)  # STEP8
        PaymentType = "Cash"
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        assert page.final_alert.get_attribute("textContent") == 'Booking Successful!'
        page.final_alert_ok_button.click()  # STEP9
        page = EventCalendarPage()  # STEP10
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        time.sleep(5)
        page.hide_events.click()
        time.sleep(5)
        page.event_tickets[0].click()
        time.sleep(5)
        for i in range(0, len(page.event_tickets)): # STEP11
            if EventHeaderDateTimeList[0] != page.date_time_title.get_attribute('textContent'):
                page.close_button.click()
                time.sleep(5)
                page.event_tickets[i + 1].click()
                time.sleep(5)
                continue
            else:
                time.sleep(5)
                assert 'Tickets Sold: 10' in page.manifest_title.get_attribute("innerText")
                assert 'Ticket Available: 0' in page.manifest_title.get_attribute("innerText")
                assert '5 Adult' in page.manifest_tickets.get_attribute("innerText")
                assert '5 Child' in page.manifest_tickets.get_attribute("innerText")
                page.add_booking_button.click()  # STEP12
            break
        time.sleep(5)
        page = AdminBookingPage()
        time.sleep(5)
        page.first_tickets_type.send_keys('1')  # STEP13
        time.sleep(5)
        assert page.final_alert.get_attribute(
            "textContent") == 'Booking 1 tickets will overbook this event.  Do you want to continue?'
        page.final_alert_ok_button.click()
        page.second_tickets_type.send_keys('1')
        time.sleep(5)
        assert page.final_alert.get_attribute(
            "textContent") == 'Booking 2 tickets will overbook this event.  Do you want to continue?'
        page.final_alert_ok_button.click() # STEP14
        time.sleep(5)
        time.sleep(5)
        assert page.is_element_present('enter_customer_information_button') == True
        page.enter_customer_information_button.click()  # STEP15
        time.sleep(5)
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName)  # STEP16
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        time.sleep(10)
        page.complete_booking_button.click()
        time.sleep(5)
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('payment_type_list'))
        select = Select(page.payment_type_list)  # STEP17
        PaymentType = "Cash"
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        assert page.final_alert.get_attribute("textContent") == 'Booking Successful!'
        page.final_alert_ok_button.click()  # STEP18
        page = EventCalendarPage()  # STEP19
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        time.sleep(5)
        page.event_tickets[0].click()
        time.sleep(5)
        for i in range(0, len(page.event_tickets)):  # STEP11
            if EventHeaderDateTimeList[0] != page.date_time_title.get_attribute('textContent'):
                page.close_button.click()
                time.sleep(5)
                page.event_tickets[i + 1].click()
                time.sleep(5)
                continue
            else:
                time.sleep(5)
            break
        assert 'Tickets Sold: 12' in page.manifest_title.get_attribute("innerText")
        assert 'Ticket Available: -2' in page.manifest_title.get_attribute("innerText")
        assert '6 Adult' in page.manifest_tickets.get_attribute("innerText")
        assert '6 Child' in page.manifest_tickets.get_attribute("innerText")
