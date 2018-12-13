from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from string import digits
from selenium.webdriver.support.ui import Select
import random
from event_calendar import EventCalendarPage
from random import choice
from datetime import date, datetime
import time
from selenium.webdriver import ActionChains
from creds import admin_login, admin_password,server, database, username, password
from dateutil.relativedelta import relativedelta
from pytz import timezone

ActivityNameList = []
ActivityIDList =[]
Activity1 = 'Linked Activity A'
Activity2 = 'Linked Activity B'
Activity3 = 'Linked Activity C'
Activity4 = 'Linked Activity D'
ActivityTimezone = 'PT'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO510_511_512_513_519_520(BaseTest):
    def test_510(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys(Activity1)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
        time.sleep(7)
        select = Select(page.first_linked_activity)
        time.sleep(5)
        select.select_by_visible_text(Activity2)
        page.save_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity1)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        page.cancel_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity2)
        time.sleep(5)
        text = page.activity_title.get_attribute("textContent")
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1

    def test_511(self):
        page = NavigationBar()
        page.open()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click() #STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(Activity1)#STEP2
        page.first_tickets_type.send_keys('1') #STEP3
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 27)) #STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = '9'
        EventTimeMinutes = '00'
        timeday = 'PM'
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone) #STEP5
        time.sleep(5)
        page.enter_customer_information_button.click() #STEP6
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName) #STEP7
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        page.complete_booking_button.click()
        time.sleep(12)
        select = Select(page.payment_type_list)
        PaymentType = "Cash" #STEP8
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage() #STEP10
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(Activity2)
        page.hide_events.click()
        time.sleep(2)
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
        assert page.event_status.get_attribute('textContent')=='Closed'

    def test_512(self):
        page=ActivityHubPage()
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity3)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
            page.save_button.click()
        page=ActivityHubPage()
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity4)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
            page.save_button.click()
        page=ActivityHubPage()#STEP1
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity3)#STEP2
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        time.sleep(5)
        select.select_by_visible_text(Activity4)#STEP3
        page.save_button.click()
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity1)#STEP4
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.second_linked_activity)# STEP5
        time.sleep(5)
        select.select_by_visible_text(Activity4)
        actions = ActionChains(get_driver())
        actions.move_to_element(page.tooltip_linked_activity).perform()
        time.sleep(3)
        assert page.tooltip_linked_activity_msg.get_attribute('textContent') ==\
               "Activity '"+''.join(Activity4)+"' is linked with 1 other activity. After saving changes your activity will be linked to all activities already linked with '"+''.join(Activity4)+"'."
        page.save_button.click()# STEP6
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity1)# STEP7
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity3
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP8
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity2)# STEP9
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity3
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP10
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity3)# STEP11
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP12
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity4)# STEP13
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity3

    def test_513(self):
        page = NavigationBar()
        page.open()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click() #STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(Activity4)#STEP2
        page.first_tickets_type.send_keys('1') #STEP3
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 27)) #STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = '10'
        EventTimeMinutes = '00'
        timeday = 'PM'
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone) #STEP5
        time.sleep(5)
        page.enter_customer_information_button.click() #STEP6
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName) #STEP7
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        page.complete_booking_button.click()
        time.sleep(12)
        select = Select(page.payment_type_list)
        PaymentType = "Cash" #STEP8
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage() #STEP10
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(Activity1)
        page.hide_events.click()
        time.sleep(2)
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
        assert page.event_status.get_attribute('textContent')=='Closed'
        page.close_button.click()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(Activity2)
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
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
        assert page.event_status.get_attribute('textContent') == 'Closed'
        page.close_button.click()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(Activity3)
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
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
        assert page.event_status.get_attribute('textContent') == 'Closed'

    def test_519(self):
        page=ActivityHubPage()#STEP1
        page.open()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity3)#STEP2
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        page.remove_third_linked_activity.click()#STEP3
        page.remove_second_linked_activity.click()
        page.remove_first_linked_activity.click()
        assert page.is_element_present('third_linked_activity')==False
        assert page.is_element_present('second_linked_activity') == False
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == '-- Select Activity --'
        page.save_button.click()#STEP4
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity1)  # STEP5
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity4
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == '-- Select Activity --'
        page.cancel_button.click()  # STEP6
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity2)  # STEP7
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity4
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == '-- Select Activity --'
        page.cancel_button.click()  # STEP8
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity3)  # STEP9
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == '-- Select Activity --'
        assert page.is_element_present('second_linked_activity')==False
        assert page.is_element_present('third_linked_activity') == False
        page.cancel_button.click()  # STEP10
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(Activity4)  # STEP7
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == '-- Select Activity --'

    def test_520(self):
        page = NavigationBar()
        page.open()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click() #STEP1
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(Activity3)#STEP2
        page.first_tickets_type.send_keys('1') #STEP3
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 27)) #STEP4
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = '11'
        EventTimeMinutes = '00'
        timeday = 'PM'
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone) #STEP5
        time.sleep(5)
        page.enter_customer_information_button.click() #STEP6
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName) #STEP7
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        page.complete_booking_button.click()
        time.sleep(12)
        select = Select(page.payment_type_list)
        PaymentType = "Cash" #STEP8
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()#STEP9
        time.sleep(5)
        page = ActivityHubPage()#STEP11
        page.open()
        page.search_activity_field.send_keys(Activity3)#STEP12
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        time.sleep(5)
        select.select_by_visible_text(Activity4)#STEP13
        page.save_button.click()
        time.sleep(5)
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()  # STEP14
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(Activity4)  # STEP15
        page.first_tickets_type.send_keys('1')  # STEP16
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        for i in range(0, len(page.dates)): #STEP17
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = '11'
        EventTimeMinutes = '00'
        timeday = 'PM'
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName + ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)  # STEP18
        time.sleep(5)
        page.enter_customer_information_button.click()  # STEP19
        NewFirstName = 'James'
        page.first_name.send_keys(NewFirstName)  # STEP20
        NewLastName = 'James'
        NewFullName = NewFirstName + ' ' + ''.join(NewLastName)
        page.last_name.send_keys(NewLastName)
        NewEmail = ('James@mailinator.com')
        page.email_address.send_keys(NewEmail)
        page.complete_booking_button.click()
        time.sleep(12)
        select = Select(page.payment_type_list)
        PaymentType = "Cash"  # STEP21
        select.select_by_visible_text(PaymentType)
        page.cash_recieved.click()
        page.submit_booking_button.click()  # STEP22
        page = EventCalendarPage() #STEP24
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(Activity3)#STEP25
        page.hide_events.click()
        time.sleep(2)
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
        for ticket in page.day_slots: #STEP26
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                else:
                    continue
            break
        time.sleep(6)
        assert page.event_status.get_attribute('textContent')=='Pending'
