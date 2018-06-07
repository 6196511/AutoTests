from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from starting_location import AddStartingLocationPage
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from creds import admin_login, admin_password
from webium import BasePage, Finds
from activity_page import AddEditActivityPage

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class LocationLink(BasePage):
    location_links = Finds(by=By.XPATH, value="//a[contains(text(), 'Helena')]")



class Test_GODO108(BaseTest):
    def test_108(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.add_location_button.click()
        page = AddStartingLocationPage()
        OldLocationNamePart = "AutoTestLoc"
        page.search_location.send_keys(OldLocationNamePart)
        page = LocationLink()
        for i in range(0, len(page.location_links)):
            if OldLocationNamePart in page.location_links[i].get_attribute("textContent"):
                if page.location_links[i].is_displayed():
                    page.location_links[i].click()
        page = AddStartingLocationPage()
        ExistedLocationName = page.location_name.get_attribute('value')
        get_driver().back()
        page.location_name.send_keys(ExistedLocationName)
        time.sleep(8)
        assert page.is_element_present('alert_message') == True
        assert page.save_button.is_enabled()==False
