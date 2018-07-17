import webium.settings
from selenium import webdriver

from actions.admin_booking import AdminBooking
from actions.certificate import CertificateActions
from actions.activity_hub import ActivityHub
from actions.people_hub import PeopleHub
from actions.groupons import Groupons
from actions.addons import Addons
from app.session import SessionHelper
from actions.customer_booking import CustomerActions


class Application:

    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        webium.settings.wait_timeout = 5
        self.session = SessionHelper(self)
        self.customer_booking = CustomerActions(self)
        self.booking = AdminBooking(self)
        self.certificate = CertificateActions(self)
        self.activity_hub = ActivityHub(self)
        self.people_hub = PeopleHub(self)
        self.groupons = Groupons(self)
        self.addons = Addons(self)

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
