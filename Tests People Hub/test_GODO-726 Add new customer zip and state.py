from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from people_hub_page import PeopleHubPage
from customer_list import CustomerListPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from creds import admin_login, admin_password
from webium import BasePage, Finds


class BaseTest(object):
    def teardown_class(self):
         close_driver()

class LocationLink(BasePage):
    location_links = Finds(by=By.XPATH, value="//a[contains(text(), 'Chris Falvey')]")



class Test_GODO726(BaseTest):
    def test_726(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=PeopleHubPage()
        page.open()
        time.sleep(2)
        page.your_customer_button.click()
        time.sleep(2)
        page = CustomerListPage()
        page.add_customer_button.click()
        time.sleep(3)
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        select = Select(page.state_list)
        time.sleep(3)
        select.select_by_visible_text('Florida')
        page.customer_zip.send_keys('54321')
        State = select.first_selected_option.text
        Zip = page.customer_zip.get_attribute('value')
        select = Select(page.country_list)
        select.select_by_visible_text('Canada')
        time.sleep(5)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.customer_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('Mexico')
        time.sleep(3)
        assert page.customer_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.customer_zip.get_attribute('value') == Zip
