from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from channel_page import ChannelPage

ChannelName = 'test 0305'
Amount = '10.01'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO781(BaseTest):
    def test_781(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        page.table_channel_editbutton.click()
        select = Select(page.comission_type_list)
        if select.first_selected_option.text == 'Percentage':
            pass
        else:
            select.select_by_visible_text('Percentage')
        if page.comission_amount.get_attribute('value') == Amount:
            pass
        else:
            page.comission_amount.clear()
            page.comission_amount.send_keys(Amount)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        page.table_channel_editbutton.click()
        select = Select(page.comission_type_list)
        NewComissionType = 'Dollar Amount'
        select.select_by_visible_text(NewComissionType)
        page.save_button.click()
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        assert page.table_channel_comission.get_attribute('textContent') == '$' + ''.join(Amount)
        page.table_channel_editbutton.click()
        time.sleep(2)
        select = Select(page.comission_type_list)
        assert select.first_selected_option.text == 'Dollar Amount'
        select.select_by_visible_text('Percentage')
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        assert page.table_channel_comission.get_attribute('textContent') == Amount+'%'
