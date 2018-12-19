from pages.groupon_page import GrouponPage
from pages.navigation_bar import NavigationBar
from pages.marketing_hub_page import MarketingHubPage
from webium.wait import wait


class Groupons:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.marketing_hub = MarketingHubPage(driver=self.driver)
        self.groupon_page = GrouponPage(driver=self.driver)

    def navigate_to(self):
        self.navigation_bar.sitemap.click()
        wait(lambda: self.navigation_bar.marketing_hub.is_displayed())
        self.navigation_bar.marketing_hub.click()
        wait(lambda: self.marketing_hub.groupon_button.is_enabled())
        self.marketing_hub.groupon_button.click()

    def get_code(self, order):
        self.navigate_to_view_codes(order)
        self.groupon_page.copy_code(order)

    def get_redeemed_code(self, order):
        self.navigate_to_view_codes(order)
        self.groupon_page.copy_redeemed_code(order)

    def navigate_to_view_codes(self, order):
        self.groupon_page.select_groupon(order.groupon_name)
        self.groupon_page.view_codes.click()
        wait(lambda: len(self.groupon_page.code_list_not_redeemed) > 1)
