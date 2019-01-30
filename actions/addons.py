from time import sleep

from pages.navigation_bar import NavigationBar
from pages.activity_hub_page import ActivityHubPage
from pages.activity_addons_page import ActivityAddonsPage
from pages.addon_page import AddonPage
from webium.wait import wait
import datetime


class Addons:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.activity_hub = ActivityHubPage(driver=self.driver)
        self.activity_addons = ActivityAddonsPage(driver=self.driver)
        self.addon_page = AddonPage(driver=self.driver)

    def navigate_to(self):
        wait(lambda: not self.navigation_bar.page_loader_wrapper.is_displayed(), timeout_seconds=20)
        wait(lambda: self.navigation_bar.main_tab is not None, timeout_seconds=20)
        self.navigation_bar.main_tab.click()
        self.navigation_bar.activities.click()
        wait(lambda: self.navigation_bar.expanded_list)
        self.navigation_bar.addons.click()
        wait(lambda: not self.navigation_bar.page_loader_wrapper.is_displayed(), timeout_seconds=20)

    def create_addon(self, addons):
        self.navigate_to()
        self.open_creation_form()
        self.get_addon_name(addons)
        self.addon_page.addon_name.send_keys(addons.addon_name)
        self.addon_page.addon_price.clear()
        self.addon_page.addon_price.send_keys(addons.addon_price)
        self.addon_page.addon_description.send_keys(addons.addon_description)
        self.addon_page.select(self.addon_page.addon_status, addons.addon_status)
        self.addon_page.save_addon.click()
        wait(lambda: self.addon_page.pop_up.is_displayed())
        assert "New add-on has been successfully added." == self.addon_page.pop_up.text
        self.addon_page.pop_up_ok_button.click()

    def get_addon_name(self, addons):
        today = datetime.date.today().isoformat()
        addons.addon_name = "New auto add-on " + today

    def open_creation_form(self):
        self.activity_addons.create_addon.click()

    def find_addon(self, addons):
        self.activity_addons.search_feild.clear()
        self.activity_addons.search_feild.send_keys(addons.addon_name)
        assert addons.addon_name == self.activity_addons.name.text
        assert addons.addon_description == self.activity_addons.description.text
        assert "$" + addons.addon_price == self.activity_addons.price.text
        assert addons.addon_status == self.activity_addons.status.text

    def delete_addon(self, addons):
        self.find_addon(addons)
        self.activity_addons.delete_button.click()
        wait(lambda: self.activity_addons.pop_up.is_displayed())
        expected_notification = "Are you sure you want to delete {}?".format(addons.addon_name)
        assert expected_notification == self.activity_addons.pop_up.text
        self.activity_addons.pop_up_ok_button.click()
        wait(lambda: not self.activity_addons.pop_up.is_displayed())
        sleep(2)

    def verify_deletion(self, addons):
        self.activity_addons.search_feild.send_keys(addons.addon_name)
        assert "No matching records found" == self.activity_addons.name.text

    def delete_addon_cancel(self, addons):
        self.find_addon(addons)
        self.activity_addons.delete_button.click()
        wait(lambda: self.activity_addons.pop_up.is_displayed())
        expected_notification = "Are you sure you want to delete {}?".format(addons.addon_name)
        assert expected_notification == self.activity_addons.pop_up.text
        self.activity_addons.pop_up_cancel_button.click()
        wait(lambda: not self.activity_addons.pop_up.is_displayed())
        sleep(2)

    def add_type(self, addons):
        self.activity_addons.edit_button.click()
        wait(lambda: not self.navigation_bar.page_loader_wrapper.is_displayed(), timeout_seconds=20)
        self.fill_type_form(addons)
        save_type_button = self.addon_page.save_type
        save_type_button.click()
        wait(lambda: self.addon_page.add_type_button.is_displayed())

    def fill_type_form(self, addons):
        self.addon_page.add_type_button.click()
        wait(lambda: self.addon_page.save_type.is_displayed())
        sleep(2)
        self.addon_page.select(self.addon_page.addon_select, addons.addon_name)
        self.addon_page.type_name.send_keys(addons.type_name)
        self.addon_page.type_price.send_keys(addons.type_price)
        if addons.type_status == "Active":
            self.addon_page.type_status.click()

    def add_type_cancel(self, addons):
        self.activity_addons.edit_button.click()
        self.fill_type_form(addons)
        self.addon_page.cancel_type.click()
        wait(lambda: self.addon_page.add_type_button.is_displayed())
        sleep(2)

    def delete_type(self, addons):
        self.activity_addons.edit_button.click()
        self.find_and_delete_type(addons)
        self.addon_page.pop_up_ok_button.click()
        sleep(2)

    def delete_type_cancel(self, addons):
        self.activity_addons.edit_button.click()
        self.find_and_delete_type(addons)
        self.addon_page.pop_up_cancel_button.click()
        sleep(2)

    def find_and_delete_type(self, addons):
        wait(lambda: len(self.addon_page.addon_name.get_attribute('value')) > 0)
        for item in self.addon_page.addon_types_table:
            if item.name.text == addons.type_name:
                item.delete.click()
                break
        wait(lambda: self.addon_page.pop_up.is_displayed())
        expected_notification = "Are you sure you want to remove this add-on type?"
        assert expected_notification == self.addon_page.pop_up.text

    def check_type_table(self, addons, count):
        for item in self.addon_page.addon_types_table:
            if item.name.text == addons.type_name:
                assert addons.type_price == item.price.text
                assert addons.type_status == item.status.text
                count += 1
        return count

    def check_type_present(self, addons):
        count = 0
        count = self.check_type_table(addons, count)
        assert 1 == count

    def check_type_not_present(self, addons):
        count = 0
        count = self.check_type_table(addons, count)
        assert 0 == count

    def get_activity_list(self, addons):
        activity_list = addons.activity.split(", ")
        addons.activity = activity_list

    def add_activity(self, addons):
        self.activity_addons.edit_button.click()
        self.get_activity_list(addons)
        for activity in addons.activity:
            wait(lambda: self.addon_page.add_activity.is_displayed())
            self.addon_page.add_activity.click()
            wait(lambda: self.addon_page.select_activity.is_displayed())
            self.addon_page.select(self.addon_page.select_activity, activity)
            self.addon_page.save_activity.click()
            wait(lambda: self.addon_page.select_activity.is_displayed())
        sleep(2)

    def add_activity_cancel(self, addons):
        self.activity_addons.edit_button.click()
        wait(lambda: self.addon_page.add_activity.is_displayed())
        self.addon_page.add_activity.click()
        wait(lambda: self.addon_page.select_activity.is_displayed())
        self.addon_page.select(self.addon_page.select_activity, addons.activity)
        self.addon_page.cancel_activity.click()
        wait(lambda: self.addon_page.add_activity.is_displayed())

    def delete_activity(self, addons):
        self.activity_addons.edit_button.click()
        self.click_delete_activity(addons)
        self.addon_page.pop_up_ok_button.click()

    def delete_activity_cancel(self, addons):
        self.activity_addons.edit_button.click()
        self.click_delete_activity(addons)
        self.addon_page.pop_up_cancel_button.click()

    def click_delete_activity(self, addons):
        wait(lambda: len(self.addon_page.addon_name.get_attribute('value')) > 0)
        added_activities = self.addon_page.activity_table
        for row in added_activities:
            if row.activity.text == addons.activity:
                row.delete.click()
                break
        wait(lambda: len(self.addon_page.pop_up.text) > 0)
        expected_notification = "Are you sure you want to delete?"
        assert expected_notification == self.addon_page.pop_up.text

    def verify_activity_present(self, addons):
        sleep(2)
        added_activities = self.addon_page.activity_table
        count = 0
        for row in added_activities:
            if row.activity.text == addons.activity:
                count += 1
        assert 1 == count

    def verify_activity_not_present(self, addons):
        sleep(2)
        added_activities = self.addon_page.activity_table
        for row in added_activities:
            assert addons.activity != row.activity.text

    def verify_activity_table(self, addons):
        added_activities = self.addon_page.activity_table
        assert len(addons.activity) == len(added_activities)
        for row in added_activities:
            assert row.activity.text in addons.activity
            assert row.addon.text in addons.addon_name

    def refresh_page(self):
        self.addon_page._driver.refresh()





