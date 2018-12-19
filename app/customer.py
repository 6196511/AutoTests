from selenium import webdriver
import webium.settings

from actions.customer_booking import CustomerActions
from actions.customer_certificate import CustomerCertActions


class Customer:

    def __init__(self, browser, domain):
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
        self.booking = CustomerActions(self, domain)
        self.certificate = CustomerCertActions(self, domain)

    def destroy(self):
        self.driver.quit()
