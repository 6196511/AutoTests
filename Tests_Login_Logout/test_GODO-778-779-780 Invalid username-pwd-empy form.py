from webium.driver import get_driver
from Login import loginpage
from webium.driver import close_driver
from creds import admin_login, admin_password
from string import digits
import time
from random import choice


class BaseTest(object):
    def teardown_class(self):
        pass
        close_driver()


class Test_GODO778_779_780(BaseTest):
    def test_778(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        invalid_pwd = (''.join(choice(digits) for i in range(7)))
        page.password_field.send_keys(invalid_pwd)
        page.button.click()
        time.sleep(5)
        assert get_driver().current_url == page.url
        assert page.error_login.is_displayed()
        assert page.error_login.get_attribute('textContent')== "ERROR: Your login was incorrect"

    def test_779(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        invalid_username = ('test779_' + ''.join(choice(digits) for i in range(7)))
        page.login_field.send_keys(invalid_username)
        page.password_field.send_keys(admin_password)
        page.button.click()
        time.sleep(5)
        assert get_driver().current_url == page.url
        assert page.error_login.is_displayed()
        assert page.error_login.get_attribute('textContent')== "ERROR: Your login was incorrect"

    def test_780(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.button.click()
        time.sleep(5)
        assert get_driver().current_url == page.url
        assert page.error_login.is_displayed()
        assert page.error_login.get_attribute('textContent')== "ERROR: Your login was incorrect"
