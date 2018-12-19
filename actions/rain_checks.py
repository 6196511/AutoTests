from webium.wait import wait

from pages.activity_hub_page import ActivityHubPage
from pages.navigation_bar import NavigationBar
from pages.rain_checks import RainChecksPage


class RainChecks:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.activity_hub = ActivityHubPage(driver=self.driver)
        self.rain_checks_page = RainChecksPage(driver=self.driver)

    def navigate_to(self):
        self.navigation_bar.sitemap.click()
        wait(lambda: self.navigation_bar.marketing_hub.is_displayed())
        self.navigation_bar.activity_hub.click()
        self.activity_hub.rain_checks.click()

    def verify_table(self, order):
        self.navigate_to()
        wait(lambda: self.rain_checks_page.page_title.text == "Rain Checks")
        assert order.activity == self.rain_checks_page.event_name.text
        assert order.first_name + " " + order.last_name == self.rain_checks_page.guest.text
        assert order.email == self.rain_checks_page.email.text
        assert order.phone == self.rain_checks_page.phone.text
