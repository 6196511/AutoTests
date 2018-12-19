ffrom webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from event_calendar import EventCalendarPage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from admin_booking import AdminBookingPage
from guide_side import GuidePage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password, guide_flat_login, guide_flat_password

ActivityName= 'Tickets Minimum Enforce'
GuideName = 'Holly Flat'
EventHeaderDateTimeList =[]

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO981(BaseTest):
    def test_981(self):
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
        select = Select(page.first_guide)
        if page.switcher_minimum_enforce.get_attribute(
                "outerHTML") != switcher_OFF and page.ticket_minimum.get_attribute('value') == '5' and select.first_selected_option.text == GuideName:
            page.cancel_button.click()
        else:
            if page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF:
                page.switcher_minimum_enforce.click()
                time.sleep(2)
                assert page.switcher_minimum_enforce.get_attribute(
                    "outerHTML") != switcher_OFF  # Tickets Minimum Enforce
            if page.ticket_minimum.get_attribute('value') != '5':
                page.ticket_minimum.clear()
                page.ticket_minimum.send_keys('5')
            if select.first_selected_option.text != GuideName:
                select.select_by_visible_text(GuideName)
            page.save_button.click()
        page = EventCalendarPage()
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
                page.add_booking_button.click()
            break
        time.sleep(5)
        page = AdminBookingPage()
        time.sleep(5)
        page.first_tickets_type.send_keys('3')
        time.sleep(5)
        assert page.final_alert.get_attribute(
            "textContent") == 'Minimum number of tickets (5 tickets) for the event has not been met yet. Do you want to continue?'
        page.final_alert_ok_button.click()  # STEP4
        time.sleep(5)
        page.enter_customer_information_button.click()
        time.sleep(5)
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName)
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
        select = Select(page.payment_type_list)
        PaymentType = "Cash"
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        time.sleep(5)
        page.submit_booking_button.click()
        time.sleep(5)
        assert page.final_alert.get_attribute("textContent") == 'Booking Successful!'
        page.final_alert_ok_button.click()
        page = EventCalendarPage()#STEP1
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)#STEP2
        select.select_by_visible_text(ActivityName)
        time.sleep(5)
        page.hide_events.click()
        time.sleep(5)
        page.event_tickets[0].click()
        time.sleep(5)
        for i in range(0, len(page.event_tickets)):#STEP3
            if EventHeaderDateTimeList[0] != page.date_time_title.get_attribute('textContent'):
                page.close_button.click()
                time.sleep(5)
                page.event_tickets[i + 1].click()
                time.sleep(5)
                continue
            else:
                time.sleep(5)
                assert 'Tickets Sold: 3' in page.manifest_title.get_attribute("innerText")
                assert page.event_status.get_attribute('textContent') == 'Pending'
            break
        time.sleep(5)
        select = Select(page.guide_list)#STEP4
        select.select_by_visible_text(GuideName)
        page.save_guide.click()
        assert page.info_pop_up.get_attribute('textContent') == "Information was saved successfully."
        page.OK_info_pop_up.click()#STEP5
        page = loginpage()
        page.open()
        page.login_field.send_keys(guide_flat_login)#STEP6
        page.password_field.send_keys(guide_flat_password)
        page.button.click()
        page = GuidePage()
        time.sleep(5)
        page.search_field.send_keys(ActivityName)
        time.sleep(5)
        page.event_tickets[0].click()
        for i in range(0, len(page.event_tickets)):#STEP7
            if '(3)' in page.customer_tickets.get_attribute("innerText") and page.date_time_title.get_attribute('textContent') == EventHeaderDateTimeList[0]:
                time.sleep(5)
                page.add_booking.click()
            else:
                get_driver().back()
                time.sleep(5)
                page.event_tickets[i + 1].click()
                time.sleep(5)
                continue
        time.sleep(5)
        page.add_booking.click()#STEP8
        page = AdminBookingPage()
        page.second_tickets_type.send_keys('1')#STEP9
        time.sleep(5)
        assert page.final_alert.get_attribute(
            "textContent") == 'Minimum number of tickets (5 tickets) for the event has not been met yet. Do you want to continue?'
        page.alert_cancel_button.click()#STEP10
        time.sleep(5)
        assert page.is_element_present('enter_customer_information_button') == False
