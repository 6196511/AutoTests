from webium.driver import get_driver
from webium.driver import close_driver
from company_page import AddCompanyPage, EditCompanyPage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
from random import choice
from string import digits

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO197(BaseTest):
    def test_197(self):
        get_driver().maximize_window()
        page = AddCompanyPage()
        page.open()
        time.sleep(3)
        page.internal_pwd_field.send_keys('GD2018a!')
        NewCompanyName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.company_name_field.send_keys(NewCompanyName)
        NewCompanyEmail = (NewCompanyName + '@mailinator.com')
        page.company_email.send_keys(NewCompanyEmail)
        NewUserName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.pwd_field.send_keys(NewUserPassword)
        NewPhone = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone_field.send_keys(NewPhone)
        city_values = ('Washington','New York','Miami','Los Angeles','Chicago','Dallas')
        NewCity = random.choice(city_values)
        page.city_field.send_keys(NewCity)
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        select = Select(page.state_list)
        state_values = ('Washington','New York','Florida','Texas','California','Utah')
        NewState = random.choice(state_values )
        select.select_by_visible_text(NewState)
        NewZipCode = ('' + ''.join(choice(digits) for i in range(5)))
        page.zip_field.send_keys(NewZipCode)
        timezone_values = ('Atlantic', 'Eastern', 'Central', 'Mountain', 'Mountain (No DST)', 'Pacific', 'Alaska', 'Hawaii','Hawaii (No DST)')
        NewTimeZone = random.choice(timezone_values)
        select = Select(page.time_zone_list)
        select.select_by_visible_text(NewTimeZone)
        NewAddress ='test123456'
        page.address1_field.send_keys(NewAddress)
        page.addcompany_button.click()
        time.sleep(5)
        page = EditCompanyPage()
        page.open()
        time.sleep(3)
        assert page.company_name_field.get_attribute('value') == NewCompanyName
        assert page.company_email.get_attribute('value') == NewCompanyEmail
        assert page.phone_field.get_attribute('value') == NewPhone
        assert page.city_field.get_attribute('value') == NewCity
        assert page.address1_field.get_attribute('value') == NewAddress
        assert page.zip_field.get_attribute('value') == NewZipCode
        select = Select(page.country_list)
        assert select.first_selected_option.text == 'United States'
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewState
        select = Select(page.time_zone_list)
        assert select.first_selected_option.text == NewTimeZone


