from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from employees import EmployeePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from creds import admin_login, admin_password
from webium import BasePage, Finds

user_name = 'Test Zip'


class BaseTest(object):
    def teardown_class(self):
         close_driver()

class LocationLink(BasePage):
    location_links = Finds(by=By.XPATH, value="//a[contains(text(), 'Chris Falvey')]")



class Test_GODO731(BaseTest):
    def test_731(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        time.sleep(5)
        page = EmployeePage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(user_name)
        time.sleep(2)
        page.edit_user_button.click()
        time.sleep(2)
        select = Select(page.state_list)
        State = select.first_selected_option.text
        Zip = page.user_zip.get_attribute('value')
        select = Select(page.country_list)
        select.select_by_visible_text('Canada')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.user_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('Mexico')
        time.sleep(3)
        assert page.user_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.user_zip.get_attribute('value') == Zip

