from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from channel_page import ChannelPage

ChannelName = 'test 070518'
Amount1 = '5.5'
Amount2 = '10.5'

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
        time.sleep(2)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        page.table_channel_editbutton.click()
        time.sleep(5)
        select = Select(page.comission_type_list)
        if select.first_selected_option.text == 'Dollar Amount':
            pass
        else:
            select.select_by_visible_text('Dollar Amount')
        if page.comission_amount.get_attribute('value') == Amount1:
            pass
        else:
            page.comission_amount.clear()
            page.comission_amount.send_keys(Amount1)
        page.save_button.click()
        time.sleep(2)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        page.table_channel_editbutton.click()
        time.sleep(5)
        page.comission_amount.clear()
        page.comission_amount.send_keys(Amount2)
        page.save_button.click()
        time.sleep(2)
        page.search_field.send_keys(ChannelName)
        time.sleep(2)
        assert page.table_channel_comission.get_attribute('textContent') == '$' + ''.join(Amount2)
        page.table_channel_editbutton.click()
        time.sleep(2)
        assert page.comission_amount.get_attribute('value') == Amount2
