from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds


class CompanyList(WebElement):
    company_name = Find(by=By.XPATH, value="./td")
    login_button = Find(by=By.XPATH, value=".//a[@title='Login']")


class LoginPage(BasePage):

    def __init__(self, domain, *args, **kwargs):
        super().__init__(url=domain, *args, **kwargs)

    # Base login page.

    login_input = Find(by=By.NAME, value="username")
    password_input = Find(by=By.NAME, value="password")
    login_button = Find(by=By.CSS_SELECTOR, value="input[type=submit]")

    # Page to select company for call center user. ccu_companyList.aspx

    logout_button = Find(by=By.XPATH, value="//a[@href='/login.aspx?command=logout']")
    company_list = Finds(CompanyList, by=By.XPATH, value="//tbody/tr")

    def choose_company(self, company):
        for item in self.company_list:
            title = item.company_name.text
            if title == company:
                item.login_button.click()
                break

    def get_url(self):
        return self._driver.current_url
