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

class Test_GODO790(BaseTest):
    def test_790(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        time.sleep(2)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        page.table_channel_editbutton.click()
        time.sleep(5)
        select = Select(page.country_list)
        if select.first_selected_option.text == 'United States':
            pass
        else:
            select.select_by_visible_text('United States')
        select = Select(page.state_list)
        if select.first_selected_option.text == 'California':
            pass
        else:
            select.select_by_visible_text('California')
        if page.zip_code.get_attribute('value') == '45355':
            pass
        else:
            page.zip_code.clear()
            page.zip_code.send_keys('45355')
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