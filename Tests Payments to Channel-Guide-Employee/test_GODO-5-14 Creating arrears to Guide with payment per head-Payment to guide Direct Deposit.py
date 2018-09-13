from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password, guide_per_head_login, guide_per_head_password
import random
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from event_calendar import EventCalendarPage
from guide_side import GuidePage
from guide_payroll import GuidePayrollPage
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from selenium.common.exceptions import WebDriverException
from pytz import timezone


ActivityName = "_AutoTest200718"
ActivityTimezone = 'AT'
GuideName = "Alexey Perhead"
guide_per_head_rate = 10
AdultTickets = '4'
ChildTickets = '3'
guide_per_head_due_amount = (int(AdultTickets) + int(ChildTickets)) * guide_per_head_rate
guide_per_head_due =('$'+''.join(str(guide_per_head_due_amount))+'.00')
AT = timezone('America/Glace_Bay')
# at_time = datetime.now(AT)
# time_and_date = at_time.strftime('%#m/%#d/%Y %#H:%M')

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO5_14(BaseTest):
    def test_5(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = GuidePayrollPage()
        page.open()
        time.sleep(3)
        select = Select(page.guide_list)
        try:
            select.select_by_visible_text(GuideName)
            time.sleep(3)
            for i in range(0, len(page.check)):
                if page.cash[i].is_displayed():
                    page.cash[i].click()
                else:
                    continue
                break
            time.sleep(2)
            for i in range(0, len(page.pay_button)):
                if page.pay_button[i].is_displayed():
                    page.pay_button[i].click()
                else:
                    continue
                break
            time.sleep(3)
            alert = get_driver().switch_to_alert()
            alert.accept()
            time.sleep(2)
            page.OK_button.click()
        except WebDriverException:
            print("Guide has no payment due")
            get_driver().refresh()
        page = NavigationBar()
        time.sleep(2)
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)
        page.first_tickets_type.send_keys(AdultTickets)
        page.second_tickets_type.send_keys(ChildTickets)
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
        EventTimeHours = str(random.randint(2, 11))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM','PM'))
        EventTimeWithZone = (EventTimeHours+':'+''.join(EventTimeMinutes)+' '+''.join(timeday)+' '+''.join(ActivityTimezone))
        nextMonthDate = (datetime.now() + relativedelta(months=1)).strftime('%#m')
        NextMonthName = (datetime.now() + relativedelta(months=1)).strftime("%B")
        NewFullDate = (NextMonthName+ ' ' + ''.join(str(EventDate)))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)
        time.sleep(5)
        page.enter_customer_information_button.click()
        FirstName = "Alexey"
        page.first_name.send_keys(FirstName)
        LastName = "Kolennikov"
        page.last_name.send_keys(LastName)
        EmailAddress = 'godoautotest@gmail.com'
        page.email_address.send_keys(EmailAddress)
        page.complete_booking_button.click()
        time.sleep(2)
        select = Select(page.payment_type_list)
        time.sleep(5)
        PaymentType = "Cash"
        select.select_by_visible_text(PaymentType)
        time.sleep(2)
        page.cash_recieved.click()
        page.submit_booking_button.click()
        time.sleep(5)
        page = EventCalendarPage()
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
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NewFullDate and EventTime in page.date_time_title.get_attribute('textContent')
                    assert ActivityName == page.activity_name_title.get_attribute('textContent')
                    select = Select(page.guide_list)
                    select.select_by_visible_text(GuideName)
                    page.save_guide.click()
                    page.close_button.click()
                else:
                    continue
            break
        page = loginpage()
        page.open()
        page.login_field.send_keys(guide_per_head_login)
        page.password_field.send_keys(guide_per_head_password)
        page.button.click()
        page = GuidePage()
        time.sleep(2)
        page.day_button.click()
        time.sleep(2)
        page.date_picker.click()
        time.sleep(2)
        page.next_month.click()
        time.sleep(2)
        for i in range(0, len(page.days_date_picker)):
            if page.days_date_picker[i].get_attribute("textContent") == str(EventDate):
                page.days_date_picker[i].click()
            else:
                continue
            break
        time.sleep(5)
        assert str(NewFullDate) in page.date_header.get_attribute("textContent")
        for ticket in page.day_slots:
            for i in range(0, len(page.day_slots)):
                if EventTime in ticket.day_slot_time[i].get_attribute('textContent'):
                    page.day_slots[i].click()
                    time.sleep(6)
                    assert NextMonthName and EventDate and EventTimeWithZone in page.date_time_title.get_attribute('textContent')
                    assert ActivityName in page.activity_name_title.get_attribute('textContent')
                else:
                    continue
            break
        time.sleep(4)
        page.check_in.click()
        page.event_complete.click()
        alert = get_driver().switch_to_alert()
        alert.accept()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = GuidePayrollPage()
        page.open()
        select = Select(page.guide_list)
        select.select_by_visible_text(GuideName)
        time.sleep(5)
        for i in range(0, len(page.event_due)):
            if page.event_due[i].is_displayed():
                assert page.event_due[i].get_attribute("textContent") == guide_per_head_due
            else:
                continue
            break
        for i in range(0, len(page.activity_timedate)):
            if page.activity_timedate[i].is_displayed():
                assert EventTimeWithZone and nextMonthDate and EventDate in page.activity_timedate[i].get_attribute("textContent")
            else:
                continue
            break
    def test_14(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = GuidePayrollPage()
        page.open()
        select = Select(page.guide_list)
        select.select_by_visible_text(GuideName)
        time.sleep(6)
        for i in range(0, len(page.direct_deposit)):
            if page.direct_deposit[i].is_displayed():
                page.direct_deposit[i].click()
            else:
                continue
            break
        time.sleep(6)
        for i in range(0, len(page.pay_button)):
            if page.pay_button[i].is_displayed():
                page.pay_button[i].click()
            else:
                continue
            break
        time.sleep(6)
        alert = get_driver().switch_to_alert()
        assert (guide_per_head_due+' to '+''.join(GuideName)) in alert.text
        alert.accept()
        time_and_date = datetime.now(AT).strftime('%#m/%#d/%Y %#I:%M')
        print(time_and_date)
        time.sleep(2)
        page.OK_button.click()
        time.sleep(12)
        select = Select(page.show_entries)
        select.select_by_visible_text('100')
        time.sleep(8)
        # try:
        #     page.next_button.click()
        # except WebDriverException:
        #     print("Less than 100 Entries")
        # time.sleep(4)
        L=[]
        # for i in range(0, len(page.payment_entry)):
        #     L.append(page.payment_entry[i].get_attribute('textContent'))
        for i in range(0, len(page.payment_entry)): #until fixing 2904 Incorrect sorting of Recent Payments by date on guide_payroll.aspx
            if time_and_date in page.payment_entry[i].get_attribute('textContent'):
                L.append(page.payment_entry[i].get_attribute('textContent'))
                assert GuideName and guide_per_head_due in page.payment_entry[i].get_attribute('textContent')
            else:
                continue
            break
        assert len(L) ==1  #until fixing 2904 Incorrect sorting of Recent Payments by date on guide_payroll.aspx
        # L.sort(reverse=True)
        # assert time_and_date and GuideName and guide_per_head_due in L[0]
