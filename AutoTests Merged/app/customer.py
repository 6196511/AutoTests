from selenium import webdriver
import webium.settings

from actions.customer_booking import CustomerActions
from actions.customer_certificate import CustomerCertActions


class Customer:

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
        self.booking = CustomerActions(self)
        self.certificate = CustomerCertActions(self)

    def destroy(self):
        self.driver.quit()
