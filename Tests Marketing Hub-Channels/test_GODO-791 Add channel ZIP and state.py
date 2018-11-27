from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from channel_page import ChannelPage

ChannelName = 'Test Channel 250718'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO791(BaseTest):
    def test_791(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        time.sleep(2)
        page.add_channel_button.click()
        time.sleep(5)
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        select = Select(page.state_list)
        time.sleep(3)
        select.select_by_visible_text('Florida')
        page.zip_code.send_keys('54321')
        State = select.first_selected_option.text
        Zip = page.zip_code.get_attribute('value')
        select = Select(page.country_list)
        select.select_by_visible_text('Canada')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State #Bug2952
        assert page.zip_code.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('Mexico')
        time.sleep(3)
        assert page.zip_code.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.zip_code.get_attribute('value') == Zip