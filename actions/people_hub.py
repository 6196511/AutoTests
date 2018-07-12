from pages.navigation_bar import NavigationBar
from pages.people_hub_page import PeopleHubPage
from pages.add_guide_page import AddGuidePage
from webium.wait import wait
import random
import string
from time import sleep


class PeopleHub:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.people_hub_page = PeopleHubPage(driver=self.driver)
        self.add_guide_page = AddGuidePage(driver=self.driver)

    def navigate_to(self):
        self.navigation_bar.sitemap.click()
        wait(lambda: self.navigation_bar.people_hub.is_displayed())
        self.navigation_bar.people_hub.click()

    def add_guide(self, guides):
        self.add_guide_form()
        self.get_unique_data(guides)
        self.add_guide_page.username.send_keys(guides.username)
        self.add_guide_page.password.send_keys(guides.password)
        self.add_guide_page.first_name.send_keys(guides.first_name)
        self.add_guide_page.last_name.send_keys(guides.last_name)
        self.add_guide_page.email.send_keys(guides.email)
        self.add_guide_page.select(self.add_guide_page.timezone, guides.timezone)
        self.add_guide_page.phone_number.send_keys(guides.phone_number)
        if guides.secondary_phone_number is not None:
            self.add_guide_page.secondary_phone_number.send_keys(guides.secondary_phone_number)
        if guides.emergency_contact is not None:
            self.add_guide_page.emergency_contact.send_keys(guides.emergency_contact)
        if guides.hire_date is not None:
            self.add_guide_page.hire_date.send_keys(guides.hire_date)
        if guides.end_date is not None:
            self.add_guide_page.end_date.send_keys(guides.end_date)
        if guides.bank_name is not None:
            self.add_guide_page.bank_name.send_keys(guides.bank_name)
        if guides.account_type is not None:
            self.add_guide_page.select(self.add_guide_page.account_type, guides.account_type)
        if guides.bank_routing_number is not None:
            self.add_guide_page.bank_routing_number.send_keys(guides.bank_routing_number)
        if guides.account_number is not None:
            self.add_guide_page.account_number.send_keys(guides.account_number)
        self.add_guide_page.select(self.add_guide_page.pay_rate_type, guides.pay_rate_type)
        if guides.trained_activities is not None:
            self.add_guide_page.select_trained_activity(guides.trained_activities)
        self.add_guide_page.save_button.click()

    def add_guide_form(self):
        self.navigate_to()
        self.people_hub_page.add_guide_button.click()
        sleep(2)

    def find_guide_by_email(self, guides):
        self.people_hub_page.search_input.send_keys(guides.email)
        assert self.people_hub_page.name.text == guides.first_name + " " + guides.last_name
        assert self.people_hub_page.phone_number.text == guides.phone_number
        assert self.people_hub_page.email.text == guides.email

    def delete_guide(self, guides):
        self.people_hub_page.delete.click()
        wait(lambda: self.people_hub_page.pop_up.is_displayed())
        assert self.people_hub_page.pop_up.text == "Are you sure you want to delete %s %s?" % (guides.first_name,
                                            guides.last_name), "Wrong alert: %s" % self.people_hub_page.pop_up.text
        self.people_hub_page.pop_up_ok_button.click()
        sleep(1)
        wait(lambda: self.people_hub_page.pop_up.is_displayed())
        assert self.people_hub_page.pop_up.text == "Guide deleted successfully!", \
            "Wrong alert: %s" % self.people_hub_page.pop_up.text
        self.people_hub_page.pop_up_ok_button.click()
        sleep(2)

    def get_unique_data(self, guides, size=10, chars=string.ascii_lowercase + string.digits):
        username = ''.join(random.choice(chars) for _ in range(size))
        guides.username = username
        email = username + "@mailinator.com"
        guides.email = email
        print(username)

    def verify_guides_details(self, guides):
        self.people_hub_page.edit.click()
        wait(lambda: len(self.add_guide_page.username.text) > 0)
        assert self.add_guide_page.username.text == guides.username
        assert self.add_guide_page.first_name.text == guides.first_name
        assert self.add_guide_page.last_name.text == guides.last_name
        assert self.add_guide_page.email.text == guides.email
        assert self.add_guide_page.get_selected_value(self.add_guide_page.timezone) == guides.timezone
        assert self.add_guide_page.phone_number.text == guides.phone_number
        if guides.secondary_phone_number is not None:
            assert self.add_guide_page.secondary_phone_number.text == guides.secondary_phone_number
        if guides.emergency_contact is not None:
            assert self.add_guide_page.emergency_contact.text == guides.emergency_contact
        if guides.hire_date is not None:
            assert self.add_guide_page.hire_date.text == guides.hire_date
        if guides.end_date is not None:
            assert self.add_guide_page.end_date.text == guides.end_date
        if guides.bank_name is not None:
            assert self.add_guide_page.bank_name.text == guides.bank_name
        if guides.account_type is not None:
            assert self.add_guide_page.account_type.text == guides.account_type
        if guides.bank_routing_number is not None:
            assert self.add_guide_page.bank_routing_number.text == guides.bank_routing_number
        if guides.account_number is not None:
            assert self.add_guide_page.account_number.text == guides.account_number
        assert self.add_guide_page.get_selected_value(self.add_guide_page.pay_rate_type) == guides.pay_rate_type
        if guides.trained_activities is not None:
            assert self.add_guide_page.trained_activity.text == guides.trained_activities

    def add_guide_with_invalid_username(self, guides):
        self.add_guide_form()
        self.add_guide_page.username.send_keys(guides.username)
        self.add_guide_page.empty_space.click()
        wait(lambda: len(self.add_guide_page.bootstrap_alert.text) > 0)
        print(self.add_guide_page.bootstrap_alert.text)
        assert self.add_guide_page.bootstrap_alert.text == "Username (%s) not valid." % guides.username

    def import_guide(self, guides):
        self.add_guide_form()
        self.add_guide_page.import_guide_button.click()
        self.add_guide_page.i_username.send_keys(guides.username)
        self.add_guide_page.select(self.add_guide_page.i_pay_type, guides.pay_rate_type)
        self.add_guide_page.i_rate.send_keys(guides.rate)
        self.add_guide_page.i_import_button.click()

    def import_guide_username_only(self, guides):
        self.add_guide_form()
        self.add_guide_page.import_guide_button.click()
        self.add_guide_page.i_username.send_keys(guides.username)
        self.add_guide_page.i_import_button.click()

    def find_imported_guide(self, guides):
        self.find_by_name(guides)
        assert self.people_hub_page.name.text == guides.first_name + " " + guides.last_name + " (pending)"

    def find_by_name(self, guides):
        self.people_hub_page.search_input.send_keys(guides.first_name + " " + guides.last_name)

    def verify_alert(self):
        self.add_guide_page.verify_alert("Guide not found")

    def close_pop_up(self):
        self.add_guide_page.i_close_button.click()
        sleep(2)

    def submit_empty_form(self):
        self.add_guide_form()
        self.add_guide_page.import_guide_button.click()
        sleep(2)
        self.add_guide_page.i_import_button.click()

    def verify_error_messages(self, wording, quantity):
        assert len(self.add_guide_page.error_messages) == quantity
        for notification in self.add_guide_page.error_messages:
            assert notification.text == wording

    def edit_guide_activity(self, activity):
        self.people_hub_page.edit.click()
        wait(lambda: len(self.add_guide_page.username.text) > 0)
        self.add_guide_page.select(self.add_guide_page.trained_activity, activity)
        self.add_guide_page.save_button.click()
        self.add_guide_page.wait_redirection()

    def edit_guide_remove_activity(self):
        self.people_hub_page.edit.click()
        wait(lambda: len(self.add_guide_page.username.text) > 0)
        self.add_guide_page.trained_activity_remove.click()
        self.add_guide_page.save_button.click()
        self.add_guide_page.wait_redirection()
