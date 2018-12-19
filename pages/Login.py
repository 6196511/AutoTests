from selenium.webdriver.common.by import By
from webium import BasePage, Find

class loginpage (BasePage):
    url = 'https://ci004.godo.io/login.aspx'
    login_field = Find(by=By.NAME, value='username')
    password_field = Find(by=By.NAME, value='password')
    button = Find(by=By.XPATH, value='//input[@class="btn-sm btn-primary"]')
