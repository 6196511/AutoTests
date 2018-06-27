from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from event_schelduler import EventScheldulerPage
from event_calendar import EventCalendarPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
import datetime
from dateutil.relativedelta import relativedelta

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO85(BaseTest):
    def test_85(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys('AutoTest_')
        time.sleep(5)
        page.activity_actions.click()
        ActivityName = page.activity_title.get_attribute("textContent")
        page.add_events.click()
        page = EventScheldulerPage()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('scheldule_type'))
        select = Select(page.scheldule_type)
        select.select_by_visible_text('One-Time Event')
        page.onetime_field.click()
        page.next_button_calendar_begin.click()
        NewDate = random.randint(8, 30)
        nextMonthDate = datetime.date.today() + relativedelta(months=1)
        NewFullDate = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDate)))
        for i in range(0, len(page.date_calendar)):
            if i+1==NewDate:
                page.date_calendar[i].click()
            else:
                continue
            break
        NewTimeHours = str(random.randint(1, 12))
        select = Select(page.onetime_hour)
        select.select_by_visible_text(NewTimeHours)
        NewTimeMinutes = '30'
        select = Select(page.onetime_minute)
        select.select_by_visible_text(NewTimeMinutes)
        NewTimeAMPM = 'PM'
        select = Select(page.onetime_ampm)
        select.select_by_visible_text(NewTimeAMPM)
        page.onetime_add.click()
        time.sleep(5)
        assert page.is_element_present('popup_OK') == True
        page.popup_OK.click()
        page = EventCalendarPage()
        page.open()
        time.sleep(2)
        select = Select(page.activity_name)
        select.select_by_visible_text(ActivityName)
        time.sleep(2)
        page.hide_events.click()
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
        page.date_picker_next.click()
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDate):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(2)
        timeEvent = (NewTimeHours+':' + ''.join(NewTimeMinutes)+' '+''.join(NewTimeAMPM))
        assert str(NewFullDate) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEvent in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDate in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEvent in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                    page = EventCalendarPage()
                else:
                    continue
            break

