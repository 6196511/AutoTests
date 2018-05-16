from webium import BasePage, Find
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(url='https://dev.godo.io', *args, **kwargs)

    login_input = Find(by=By.NAME, value="username")
    password_input = Find(by=By.NAME, value="password")
    login_button = Find(by=By.CSS_SELECTOR, value="input[type=submit]")
