from webium.driver import get_driver
from Login import loginpage
from webium.driver import close_driver


class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test1(BaseTest):
    def test_1(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys('login')
        page.password_field.send_keys('password')
        page.button.click()
        get_driver().quit()
