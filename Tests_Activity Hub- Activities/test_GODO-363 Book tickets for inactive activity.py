from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO363(BaseTest):
    def test_363(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ActivityHubPage()
        page.open()
        InactiveActivity = 'Sometimes inactive activity'
        page.search_activity_field.send_keys(InactiveActivity)
        page.show_inactive.click()
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(10)
        select = Select(page.activity_status)
        NewActivityStatus = "Inactive"
        select.select_by_visible_text(NewActivityStatus )
        page.save_button.click()
        page = NavigationBar()
        time.sleep(8)
        page.main_actions_drop_down.click()
        page.add_a_booking.click()
        time.sleep(8)
        page = AdminBookingPage()
        page.activity_list.click()
        L=[]
        for i in range(0, len(page.activities_in_list)):
            L.append(page.activities_in_list[i].get_attribute("textContent"))
        assert InactiveActivity not in L










