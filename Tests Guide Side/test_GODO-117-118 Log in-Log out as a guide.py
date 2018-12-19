from webium.driver import get_driver
from Login import loginpage
from webium.driver import close_driver
from creds import guide1_login, guide1_password
from guide_side import GuidePage
import time
from selenium.webdriver.support.wait import WebDriverWait

class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO117_118(BaseTest):
    def test_117(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(guide1_login)
        page.password_field.send_keys(guide1_password)
        page.button.click()
        time.sleep(5)
        page=GuidePage()
        assert page.url == get_driver().current_url

    def test_118(self):
        get_driver().maximize_window()
        page = GuidePage()
        page.profile_dropdown.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('logout_button'))
        page.logout_button.click()
        page = loginpage()
        assert page.url == get_driver().current_url