import webium.settings
from selenium import webdriver

from actions.admin_booking import AdminBooking
from actions.calendar import Calendar
from actions.certificate import CertificateActions
from actions.waiting import Waiting
from app.session import SessionHelper


class CallCenter:

    def __init__(self, browser, domain, credentials):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_script_timeout(30)
        self.driver.set_page_load_timeout(60)
        webium.settings.wait_timeout = 15
        self.session = SessionHelper(self, domain=domain, credentials=credentials)
        self.booking = AdminBooking(self)
        self.certificate = CertificateActions(self)
        self.calendar = Calendar(self)
        self.waiting = Waiting(self)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            return True
        except:
            return False

    def current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        button = self.session.navigation_bar.main_actions_drop_down
        self.driver.refresh()
        self.waiting.for_staleness(element=button, timeout=5)
