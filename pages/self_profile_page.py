from selenium.webdriver.common.by import By
from webium import BasePage, Find


class SelfProfilePage(BasePage):
    url = 'https://dev.godo.io/administrator_self.aspx'
    first_name_field = Find(by=By.XPATH, value="//input[@id='administrator_firstname']")
    last_name_field = Find(by=By.XPATH, value="//input[@id='administrator_lastname']")
    phone1_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_1']")
    phone2_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_2']")
    email_field = Find(by=By.XPATH, value="//input[@id='administrator_email']")
    country_list = Find(by=By.XPATH, value="//select[@id='administrator_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='administrator_state']")
    user_zip = Find(by=By.XPATH, value="//input[@id='administrator_zipcode']")