from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
import random
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO116(BaseTest):
    def test_116(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        activity_partnames = ('AutoTest', 'test1', '3110', '25102017', 'TESTEDIT', 'REGRESSION', 'Regr')
        activity_partname = random.choice(activity_partnames)
        page.search_activity_field.send_keys(activity_partname)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        ActivityName = page.activity_name.get_attribute('value')
        page.ticket_maximum.clear()
        page.ticket_maximum.send_keys('50')
        page.ticket_minimum.clear()
        page.ticket_minimum.send_keys('51')
        page.ticket_maximum.click()
        assert page.ticket_maximum.get_attribute('value') == '50'
        assert page.ticket_minimum.get_attribute('value') == '51'
        time.sleep(5)
        assert page.is_element_present('ticket_maximum_alert') == True
        assert page.ticket_maximum_alert.is_displayed()
        page.save_button.click()
        time.sleep(5)
        assert page.ticket_maximum_alert.is_displayed()
        page.ticket_maximum.clear()
        page.ticket_maximum.send_keys('10')
        page.ticket_minimum.clear()
        page.ticket_minimum.send_keys('9')
        assert page.ticket_maximum.get_attribute('value') == '10'
        assert page.ticket_minimum.get_attribute('value') == '9'
        time.sleep(5)
        assert page.is_element_present('ticket_maximum_alert') == False
        page.save_button.click()
        page.save_button.click()
        time.sleep(5)
        page = ActivityHubPage()
        get_driver().refresh()
        page.search_activity_field.send_keys(ActivityName)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.ticket_maximum.get_attribute('value') == '10'
        assert page.ticket_minimum.get_attribute('value') == '9'
        assert page.is_element_present('ticket_maximum_alert') == False
