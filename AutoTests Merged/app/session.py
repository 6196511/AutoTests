from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from time import sleep


class SessionHelper:

    def __init__(self, app):
        self.driver = app.driver
        self.login_page = LoginPage(driver=self.driver)
        self.navigation_bar = NavigationBar(driver=self.driver)

    def login(self, login, password):
        self.login_page.open()
        self.login_page.login_input.send_keys(login)
        self.login_page.password_input.send_keys(password)
        self.login_page.login_button.click()

    def ensure_login(self, login, password):
        if not self.is_logged_in_as_admin():
            self.login(login, password)

    def logout(self):
        self.navigation_bar.menu_drop_down.click()
        self.navigation_bar.logout.click()

    def ensure_logout(self):
        sleep(2)
        if self.is_logged_in_as_admin():
            self.logout()

    def is_logged_in_as_admin(self):
        return len(self.navigation_bar.navigation_bar) > 0

    def sell_certificate(self):
        self.navigation_bar.main_actions_drop_down.click()
        self.navigation_bar.sell_gift_certificates.click()
