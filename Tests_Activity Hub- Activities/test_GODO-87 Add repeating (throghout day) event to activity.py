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
from random import choice
import datetime
from dateutil.relativedelta import relativedelta

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO87(BaseTest):
    def test_87(self):
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
        select.select_by_visible_text('Repeating Event (Throughout Day)')
        page.rep_mult_begin_field.click()
        page.next_button_calendar_begin.click()
        NewDateBegin = random.randint(1, 25)
        nextMonthDate = datetime.date.today() + relativedelta(months=1)
        NewFullDateBegin = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateBegin)))
        NewFullDateNextBegin = (nextMonthDate.strftime("%B") + ' ' + ''.join(str(NewDateBegin+1)))


        print(NewDateBegin)
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
        print(NewFullDateBegin)
        print(NewFullDateNextBegin)
        print(NewFullDatePrevEnd)
        print(NewFullDateEnd)

        page.rep_mult_end_field.click()
        time.sleep(5)
        page.next_button_calendar_enddate_repmult.click()
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
        NewTimeHoursBegin = str(random.randint(1, 10))
        select = Select(page.rep_mult_hours_begin)
        select.select_by_visible_text(NewTimeHoursBegin)
        minutes_values = ('00','05','10','15','20','25','30','35','40','45','50','55')
        NewTimeMinutesBegin = random.choice(minutes_values)
        select = Select(page.rep_mult_min_begin)
        select.select_by_visible_text(NewTimeMinutesBegin)
        NewTimeAMPM = 'PM'
        select = Select(page.rep_mult_appm_begin)
        select.select_by_visible_text(NewTimeAMPM)
        NewTimeHoursEnd = str(int(NewTimeHoursBegin)+2)
        select = Select(page.rep_mult_hours_end)
        select.select_by_visible_text(NewTimeHoursEnd)
        NewTimeMinutesEnd = NewTimeMinutesBegin
        select = Select(page.rep_mult_min_end)
        select.select_by_visible_text(NewTimeMinutesEnd)
        NewTimeAMPM = 'PM'
        select = Select(page.rep_mult_appm_end)
        select.select_by_visible_text(NewTimeAMPM)
        time.sleep(6)
        EveryMinutesRuns = '60'
        page.rep_every_min.send_keys(EveryMinutesRuns)
        page.rep_add_mult.click()
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
        time.sleep(5)
        page.day_button.click()
        time.sleep(5)
        timeEventBegin = (NewTimeHoursBegin+':' + ''.join(NewTimeMinutesBegin)+' '+''.join(NewTimeAMPM))
        print(timeEventBegin)
        timeEventEnd = (NewTimeHoursEnd + ':' + ''.join(NewTimeMinutesEnd) + ' ' + ''.join(NewTimeAMPM))
        assert str(NewDateBegin) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEventBegin in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventBegin in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
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
                if timeEventBegin in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateNextBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventBegin in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateEnd - 1):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateEnd - 1) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEventBegin in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDatePrevEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventBegin in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
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
                if timeEventBegin in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventBegin in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        print(timeEventEnd)
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateBegin):
                page.days_date_picker[i].click()
        time.sleep(5)
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateBegin) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEventEnd in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventEnd in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
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
                if timeEventEnd in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateNextBegin in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventEnd  in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(NewDateEnd - 1):
                page.days_date_picker[i].click()
        page.day_button.click()
        time.sleep(5)
        assert str(NewDateEnd - 1) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if timeEventEnd in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDatePrevEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventEnd  in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break
        time.sleep(2)
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
                if timeEventEnd in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDateEnd in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    assert timeEventEnd  in page.date_time_title.get_attribute('textContent')
                    page.close_button.click()
                else:
                    continue
            break

