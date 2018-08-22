from webium.driver import get_driver
from webium.driver import close_driver
from branch_page import BranchPage
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password


class BaseTest(object):
    def teardown_class(self):
        close_driver()


class Test_GODO795(BaseTest):
    def test_795(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = BranchPage()
        page.open()
        page.add_branch_button.click()
        time.sleep(3)
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        select = Select(page.state_list)
        select.select_by_visible_text('Florida')
        page.branch_zip.send_keys('54321')
        State = select.first_selected_option.text
        Zip = page.branch_zip.get_attribute('value')
        select = Select(page.country_list)
        select.select_by_visible_text('Canada')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.branch_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('Mexico')
        time.sleep(3)
        select = Select(page.state_list)
        assert page.branch_zip.get_attribute('value') == Zip
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        time.sleep(3)
        select = Select(page.state_list)
        assert select.first_selected_option.text == State
        assert page.branch_zip.get_attribute('value') == Zip
