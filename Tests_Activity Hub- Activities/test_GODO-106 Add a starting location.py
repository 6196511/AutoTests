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



class Test_GODO106(BaseTest):
    def test_106(self):
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
        NewLocationName = ("AutoTestLoc"+''.join(choice(digits) for i in range(3)))
        page.location_name.send_keys(NewLocationName)
        NewLocationAddress1 = '221 Breckenridge St'
        page.location_address_1.send_keys(NewLocationAddress1)
        NewLocationAddress2 = 'qwerty'
        page.location_address_2.send_keys(NewLocationAddress2)
        NewLocationCountry = "United States"
        select = Select(page.location_Country)
        select.select_by_visible_text(NewLocationCountry)
        NewLocationState = "Montana"
        select = Select(page.location_state)
        select.select_by_visible_text(NewLocationState )
        NewLocationCity = "Helena"
        page.location_city.send_keys(NewLocationCity)
        NewLocationZipcode = "59601"
        page.location_zipcode.send_keys(NewLocationZipcode)
        NewLocationDescription = "This location has been created automatically"
        page.location_description.clear()
        page.location_description.send_keys(NewLocationDescription)
        a = page.location_name.get_attribute('value')
        print(a)
        page.save_button.click()
        page.search_location.send_keys(a)
        time.sleep(3)
        page = LocationLink()
        for i in range(0, len(page.location_links)):
            if a in page.location_links[i].get_attribute("textContent"):
                page.location_links[i].click()
        time.sleep(5)
        page = AddStartingLocationPage()
        assert page.location_name.get_attribute('value') == NewLocationName
        assert page.location_address_1.get_attribute('value') == NewLocationAddress1
        assert page.location_address_2.get_attribute('value') == NewLocationAddress2
        select = Select(page.location_Country)
        assert select.first_selected_option.text == NewLocationCountry
        select = Select(page.location_state)
        assert select.first_selected_option.text == NewLocationState
        assert page.location_city.get_attribute('value') == NewLocationCity
        assert page.location_zipcode.get_attribute('value') == NewLocationZipcode
        assert page.location_description.get_attribute('value') == NewLocationDescription
        page=ActivityHubPage()
        page.open()
        page.add_activity_button.click()
        page=AddEditActivityPage()
        time.sleep(10)
        select = Select(page.starting_location)
        select.select_by_visible_text(NewLocationName)
        assert select.first_selected_option.text == NewLocationName