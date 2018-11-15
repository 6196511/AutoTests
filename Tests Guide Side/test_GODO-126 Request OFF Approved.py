from webium.driver import get_driver
from webium.driver import close_driver
from selenium.webdriver.support.ui import Select
import time
from fakemailgenerator_page import FakeMailGeneratorPage
from guide_side import GuidePage, GuideRequestOffPage
from request_off import RequestOFFPage
from Login import loginpage
from creds import guide1_login, guide1_password, admin_login, admin_password, guide1_email_login
import datetime


today = datetime.date.today()
start = today
end = today + datetime.timedelta(days=7)
day_start = start.strftime("%#d")
day_end = end.strftime("%#d")
month_start = start.strftime("%#m")
month_end = end.strftime("%#m")
start_date = start.strftime("%#m/%#d/%Y")
end_date = end.strftime("%#m/%#d/%Y")
CompanyName = 'GoDo Manual Testing Company'
GuideName = 'Alexey Autotest'
reason_text = 'AutoTest126'

class BaseTest(object):
    def teardown_class(self):
        pass
        close_driver()


class Test_126(BaseTest):
    def test_126(self):
        page = loginpage()
        page.open()
        page.login_field.send_keys(guide1_login)
        page.password_field.send_keys(guide1_password)
        page.button.click()
        page = GuideRequestOffPage()
        page.open()
        select = Select(page.company_drop_down)
        select.select_by_visible_text(CompanyName)
        page.start_date.click()
        time.sleep(2)
        for i in range(0, len(page.dates_calendar_start)):
            if page.dates_calendar_start[i].get_attribute('textContent') == day_start:
                page.dates_calendar_start[i].click()
            else:
                continue
            break
        time.sleep(5)
        page.end_date.click()
        time.sleep(2)
        for i in range(0, len(page.calendar_next_month )):
            if page.calendar_next_month[i].is_displayed():
                if (int(month_start)-int(month_end))>0:
                    page.calendar_next_month[i].click()
            else:
                continue
            break
        time.sleep(2)
        for i in range(0, len(page.dates_calendar_end)):
            if page.dates_calendar_end[i].get_attribute('textContent') == day_end:
                page.dates_calendar_end[i].click()
            else:
                continue
            break
        time.sleep(5)
        page.reason_field.send_keys(reason_text)
        page.I_aknowledge_checkbox.click()
        page.submit_request_button.click()
        time.sleep(3)
        assert page.pop_up_notification.get_attribute('textContent') == 'Your time off request has been received.'
        time.sleep(3)
        page.pop_up_OK.click()
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = RequestOFFPage()
        page.open()
        for i in range(0, len(page.request_off_entry)):
            if GuideName and reason_text in page.request_off_entry[i].get_attribute('textContent'):
                assert start_date and end_date in page.request_off_entry[i].get_attribute('textContent')
            else:
                continue
        Requests1_list = len(page.request_off_entry)
        for i in range(0, len(page.request_off_entry)):
            if GuideName and start_date and end_date and reason_text in page.request_off_entry[i].get_attribute('textContent'):
                select = Select(page.approval_dropdown[i])
                select.select_by_visible_text('Request Off Approved')
            else:
                continue
        time.sleep(5)
        Requests2_list = len(page.request_off_entry)
        assert Requests1_list - Requests2_list == 1
        for i in range (0, len(page.request_off_entry)):
            assert GuideName and start_date and end_date and reason_text not in page.request_off_entry[i].get_attribute('textContent')
            continue
        page.approved_button.click()
        time.sleep(3)
        assert GuideName and start_date and end_date and reason_text not in page.tables[0].get_attribute('textContent')
        assert GuideName and start_date and end_date and reason_text in page.tables[1].get_attribute('textContent')
        page = loginpage()
        page.open()
        page.login_field.send_keys(guide1_login)
        page.password_field.send_keys(guide1_password)
        page.button.click()
        page = GuideRequestOffPage()
        page.open()
        time.sleep(2)
        L=[]
        for i in range (0, len(page.request_entry)):
            if start_date and end_date in page.request_entry[i].get_attribute('textContent'):
                assert CompanyName and 'Approved' in page.request_entry[i].get_attribute('textContent')
                # assert 'Not Approved' not in page.request_entry[i].get_attribute('outerText')
                L.append(page.request_entry[i].get_attribute('textContent'))
            else:
                continue
        assert len(L)>0
