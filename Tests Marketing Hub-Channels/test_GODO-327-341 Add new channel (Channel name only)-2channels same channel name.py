from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
from random import choice
from string import digits
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from channel_page import ChannelPage



ActivityName = "AlertTest"
ActivityTimezone = 'AT'
ChannelNameList =[]

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO327_341(BaseTest):
    def test_327(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        page.add_channel_button.click()
        time.sleep(5)
        NewChannelName = ("AutoTestNameOnly_" + ''.join(choice(digits) for i in range(3)))
        page.channel_name.send_keys(NewChannelName)
        ChannelNameList.append(NewChannelName)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewChannelName)
        time.sleep(2)
        assert page.table_channel_name.get_attribute('textContent') == '  ('+''.join(NewChannelName)+')'
        assert page.table_channel_comission.get_attribute('textContent') == '' #FAILED FOR PERCENTAGE - Bug 3110
        assert page.table_channel_phonenumber.get_attribute('textContent') == ''
        assert page.table_channel_email.get_attribute('textContent') == ''
        page.table_channel_editbutton.click()
        time.sleep(5)
        assert page.channel_name.get_attribute('value') == NewChannelName
        assert page.status_checkbox.is_selected() == True
        page.cancel_button.click()
        time.sleep(7)
        page = NavigationBar()
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)
        page.first_tickets_type.send_keys('1')
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 30))
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 10))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)
        time.sleep(5)
        page.enter_customer_information_button.click()
        FirstName = "Alexey"
        page.first_name.send_keys(FirstName)
        LastName = "Kolennikov"
        page.last_name.send_keys(LastName)
        EmailAddress = '6196511@mailinator.com'
        page.email_address.send_keys(EmailAddress)
        page.complete_booking_button.click()
        time.sleep(2)
        select = Select(page.channel_list)
        time.sleep(5)
        select.select_by_visible_text(NewChannelName)
        assert select.first_selected_option.text == NewChannelName

    def test_341(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        time.sleep(2)
        entries1 = page.table_entries_qty.get_attribute('textContent')
        page.add_channel_button.click()
        time.sleep(5)
        page.channel_name.send_keys(ChannelNameList[0])
        page.save_button.click()
        time.sleep(5)
        assert page.channel_exist_alert.get_attribute('textContent') == 'Channel name ('+''.join(ChannelNameList)+') already exists, please choose another.'
        page.OK_alert.click()
        time.sleep(5)
        entries2 = page.table_entries_qty.get_attribute('textContent')
        assert entries1 == entries2 #FAILED BUG 3351