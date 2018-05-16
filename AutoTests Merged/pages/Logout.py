from selenium.webdriver.common.by import By
from webium import BasePage, Find


class logoutpage (BasePage):
    profile_dropdown = Find(by=By.XPATH, value='//*[@id="nav-wrapper"]/div/ul/li[6]')
    logout_button = Find(by=By.XPATH, value='//*[@id="nav-wrapper"]/div/ul/li[6]/ul/li[5]/a')
