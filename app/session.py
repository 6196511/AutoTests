from selenium.common.exceptions import NoSuchElementException
from webium.wait import wait

from pages.login_page import LoginPage
from pages.navigation_bar import NavigationBar
from time import sleep


class SessionHelper:

    def __init__(self, app, domain, credentials):
        self.driver = app.driver
        self.login_page = LoginPage(driver=self.driver, domain=domain)
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.credentials = credentials

    def ensure_login(self, user):
        if not self.logged_in():
            if user == "admin":
                self.login_as_admin()
            elif user == "guide":
                self.login_as_guide()
            elif user == "call_center":
                self.login_as_call_center()
            else:
                raise ValueError

    def login_as_admin(self):
        self.login_page.open()
        if self.is_login_page():
            self.login(self.credentials['admin']['login'], self.credentials['admin']['password'])
        elif self.which_profile() == "admin":
            pass
        elif self.which_profile() == "guide":
            self.logout()
        else:
            print("Unable to log in...")
            print(self.which_profile())

    def login_as_guide(self):
        self.login_page.open()
        if self.is_login_page():
            self.login(self.credentials['guide']['login'], self.credentials['guide']['password'])
        elif self.which_profile() == "guide":
            pass
        elif self.which_profile() == "admin":
            self.logout()
        else:
            print("Unable to log in...")
            print(self.which_profile())

    def login_as_call_center(self):
        self.login_page.open()
        sleep(1)
        if self.is_login_page():
            self.login(self.credentials['call_center']['login'], self.credentials['call_center']['password'])
            self.login_page.choose_company(self.credentials['call_center']['company'])
            self.wait_for_company_opened()
        elif "ccu_companyList.aspx" in self.login_page.get_url():
            self.login_page.choose_company(self.credentials['call_center']['company'])
            self.wait_for_company_opened()

    def login(self, login, password):
        self.login_page.login_input.send_keys(login)
        self.login_page.password_input.send_keys(password)
        self.login_page.login_button.click()

    def which_profile(self):
        try:
            current_profile = self.navigation_bar.profile_pic.get_attribute("src")
            if "admin_profile" in current_profile:
                return "admin"
            elif "guide_profile" in current_profile:
                return "guide"
            elif "defaults" in current_profile:
                return "call_center"
            else:
                print(current_profile)
        except NoSuchElementException:
            return "There is no profile pic on the page."

    def wait_for_company_opened(self):
        wait(lambda: self.which_profile() == "call_center", timeout_seconds=60)

    def is_login_page(self):
        return "login.aspx" in self.login_page.get_url()

    def ensure_logout(self):
        sleep(2)
        if self.logged_in():
            self.logout()

    def logged_in(self):
        if len(self.navigation_bar.profile_pics) == 1:
            return True
        else:
            return False

    def logout(self):
        self.navigation_bar.menu_drop_down.click()
        self.navigation_bar.logout.click()

    def sell_certificate(self):
        self.navigation_bar.main_actions_drop_down.click()
        self.navigation_bar.sell_gift_certificates.click()
