from webium.driver import get_driver
from Login import loginpage
from webium.driver import close_driver
from creds import admin_login, admin_password


class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO1(BaseTest):
    def test_1(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        get_driver().quit()