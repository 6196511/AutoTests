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

class Test_GODO314(BaseTest):
    def test_314(self):
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
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys('-100')
        assert page.first_ticket_price.get_attribute('value')=='100'
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys('abc')
        assert page.first_ticket_price.get_attribute('value')==''
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys('0.01')
        assert page.first_ticket_price.get_attribute('value')=='0.01'
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
        assert page.first_ticket_price.get_attribute('value') == '0.01'
        page.first_ticket_price.clear()
        page.first_ticket_price.send_keys('0.9')
        assert page.first_ticket_price.get_attribute('value') == '0.9'
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
        assert page.first_ticket_price.get_attribute('value') == '0.9'