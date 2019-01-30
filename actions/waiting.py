import webium
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webium.wait import wait


class Waiting:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver

    def for_staleness(self, element, timeout=webium.settings.wait_timeout):
        WebDriverWait(self.driver, timeout).until(staleness_of(element))

    def for_invisibility(self, element, timeout=webium.settings.wait_timeout):
        wait(lambda: not element.is_displayed(), timeout_seconds=timeout)

    def for_page_loaded(self):
        wait(lambda: self.app.session.navigation_bar.page_loader_wrapper.get_attribute('style') == "display: none;")

