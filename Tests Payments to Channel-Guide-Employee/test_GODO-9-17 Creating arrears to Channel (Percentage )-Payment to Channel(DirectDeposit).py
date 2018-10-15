from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password, guide_login, guide_password
import random
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from event_calendar import EventCalendarPage
from guide_side import GuidePage
from channel_payroll import ChannelPayrollPage
from dateutil.relativedelta import relativedelta
from datetime import date, datetime
import re
from pytz import timezone


ActivityName = "_AutoTest200918"
ActivityTimezone = 'AT'
GuideName = "Ivan Petrov"
guide_per_head_rate = 72
AdultTickets = '3'
CheckNumber = '134124124'
channel = "DollarAmount1"
channel_name = 'qwer asdf'
dollar_amount= 15
comission_amount = "$ " +''.join(str(dollar_amount))
comission_amount_alert = "$" +''.join(str(('{:.2f}'.format(round(dollar_amount, 2)))))
AT = timezone('America/Glace_Bay')
at_time = datetime.now(AT)
time_and_date = at_time.strftime('%#m/%#d/%Y %#H:%M')
from selenium.common.exceptions import WebDriverException

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO8_18(BaseTest):
    def test_8(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPayrollPage()
        page.open()
        page.channel_payment_due.click()
        time.sleep(3)
        try:
            for i in range(0, len(page.channel_entries)):
                if channel in page.channel_entries[i].get_attribute('textContent'):
                    page.channel_detail[i].click()
                else:
                    continue
                break
            time.sleep(3)
            for i in range(0, len(page.cash)):
                if page.cash[i].is_displayed():
                    page.cash[i].click()
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
            alert.accept()
            time.sleep(2)
            page.OK_button.click()
            time.sleep(2)
        except WebDriverException:
            print("Channel has no payment due")
        page = NavigationBar()
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)
        page.first_tickets_type.send_keys(AdultTickets)
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
        select = Select(page.channel_list)
        time.sleep(5)
        select.select_by_visible_text(channel)
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
        page.login_field.send_keys(guide_login)
        page.password_field.send_keys(guide_password)
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
        time.sleep(2)
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
        page = ChannelPayrollPage()
        page.open()
        page.channel_payment_due.click()
        time.sleep(5)
        L=[]
        for i in range(0, len(page.channel_entries)):
            if channel in page.channel_entries[i].get_attribute('textContent'):
                assert comission_amount in page.channel_entries[i].get_attribute('textContent')
                L.append(page.channel_entries[i].get_attribute('textContent'))
            else:
                continue
            break
        assert len(L)==1
    def test_18(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPayrollPage()
        page.open()
        page.channel_paid.click()
        time.sleep(3)
        L = []
        for i in range(0, len(page.channel_paid_entries)):
            if channel_name in page.channel_paid_entries[i].get_attribute('textContent'):
                L.append(page.channel_paid_amounts[i].get_attribute('textContent'))
            else:
                continue
            break
        assert len(L) == 1
        paid_amount = L[0]
        paid_amount_number = re.findall('\d+\.\d*', paid_amount)[0]
        time.sleep(3)
        page.channel_paid.click()
        time.sleep(3)
        page.channel_payment_due.click()
        time.sleep(3)
        for i in range(0, len(page.channel_entries)):
            if channel in page.channel_entries[i].get_attribute('textContent'):
                page.channel_detail[i].click()
            else:
                continue
            break
        time.sleep(3)
        for i in range(0, len(page.cash)):
            if page.cash[i].is_displayed():
                page.cash[i].click()
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
        assert (comission_amount_alert + ' to ' + ''.join(channel_name)) in alert.text
        alert.accept()
        time.sleep(2)
        page.OK_button.click()
        time.sleep(12)
        page.channel_paid.click()
        L1 = []
        for i in range(0, len(page.channel_paid_entries)):
            if channel_name in page.channel_paid_entries[i].get_attribute('textContent'):
                L1.append(page.channel_paid_amounts[i].get_attribute('textContent'))
            else:
                continue
            break
        assert len(L1) == 1
        paid_amount_new = L1[0]
        paid_amount_number_new = re.findall('\d+\.\d*', paid_amount_new)[0]
        assert float(paid_amount_number_new) == float(paid_amount_number)+float(dollar_amount)
