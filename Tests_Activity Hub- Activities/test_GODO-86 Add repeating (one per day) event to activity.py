from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from event_schelduler import EventScheldulerPage
from event_calendar import EventCalendarPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
from event_manifest import EventManifestPage
import datetime
from dateutil.relativedelta import relativedelta

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO86(BaseTest):
    def test_86(self):
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
        select.select_by_visible_text('Repeating Event (Once Per Day)')
        page.rep_begin_field.click()
        page.next_button_calendar_begin.click()
        NewDateBegin = random.randint(8, 25)
        nextMonthDate = datetime.date.today() + relativedelta(months=1)
        NewFullDateBegin = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateBegin)))
        NewFullDateNextBegin = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateBegin+1)))
        for i in range(0, len(page.date_calendar)):
            if i+1==NewDateBegin:
                page.date_calendar[i].click()
            else:
                continue
            break
        time.sleep(5)
        NewDateEnd = NewDateBegin+3
        NewFullDateEnd = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateEnd)))
        NewFullDatePrevEnd = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateEnd-1)))
        page.rep_end_field.click()
        page.next_button_calendar_enddate_rep.click()
        time.sleep(5)
        end_date_list = []
        for i in range(0, len(page.date_calendar_end)):
            if page.date_calendar_end[i].is_displayed():
                end_date_list.append(page.date_calendar_end[i])
        for i in range(0, len(end_date_list)):
            if i+1==NewDateEnd:
                end_date_list[i].click()
            else:
                continue
            break
        NewTimeHours = str(random.randint(1, 12))
        select = Select(page.rep_hour)
        select.select_by_visible_text(NewTimeHours)
        minutes_values = ('00','05','10','15','20','25','30','35','40','45','50','55')
        NewTimeMinutes = random.choice(minutes_values)
        select = Select(page.rep_minute)
        select.select_by_visible_text(NewTimeMinutes)
        NewTimeAMPM = 'AM'
        select = Select(page.rep_ampm)
        select.select_by_visible_text(NewTimeAMPM)
        page.rep_add.click()
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
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateBegin):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        timeEvent = (NewTimeHours+':' + ''.join(NewTimeMinutes)+' '+''.join(NewTimeAMPM))
        assert str(NewDateBegin) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEvent in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    page = EventManifestPage()
                    assert NewFullDateBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEvent in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
        page = EventCalendarPage()
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateBegin+1):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateBegin+1) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEvent in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    page = EventManifestPage()
                    assert NewFullDateNextBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEvent in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
        page = EventCalendarPage()
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateEnd-1):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateEnd-1) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEvent in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    page = EventManifestPage()
                    assert NewFullDatePrevEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEvent in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
        page = EventCalendarPage()
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateEnd):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateEnd) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEvent in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    page = EventManifestPage()
                    assert NewFullDateEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEvent in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break