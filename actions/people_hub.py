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
        assert guides.first_name + " " + guides.last_name == self.people_hub_page.name.text
        assert guides.phone_number == self.people_hub_page.phone_number.text
        assert guides.email == self.people_hub_page.email.text

    def delete_guide(self, guides):
        self.people_hub_page.delete.click()
        wait(lambda: self.people_hub_page.pop_up.is_displayed())
        expected_notification = "Are you sure you want to delete {} {}?".format(guides.first_name, guides.last_name)
        assert expected_notification == self.people_hub_page.pop_up.text
        self.people_hub_page.pop_up_ok_button.click()
        sleep(1)
        wait(lambda: self.people_hub_page.pop_up.is_displayed())
        assert "Guide deleted successfully!" == self.people_hub_page.pop_up.text
        self.people_hub_page.pop_up_ok_button.click()
        sleep(2)

    def get_unique_data(self, guides, size=10, chars=string.ascii_lowercase + string.digits):
        username = ''.join(random.choice(chars) for _ in range(size))
        guides.username = username
        email = username + "@mailinator.com"
        guides.email = email

    def verify_guides_details(self, guides):
        self.people_hub_page.edit.click()
        wait(lambda: len(self.add_guide_page.username.text) > 0)
        assert guides.username == self.add_guide_page.username.text
        assert guides.first_name == self.add_guide_page.first_name.text
        assert guides.last_name == self.add_guide_page.last_name.text
        assert guides.email == self.add_guide_page.email.text
        assert guides.timezone == self.add_guide_page.get_selected_value(self.add_guide_page.timezone)
        assert guides.phone_number == self.add_guide_page.phone_number.text
        if guides.secondary_phone_number is not None:
            assert guides.secondary_phone_number == self.add_guide_page.secondary_phone_number.text
        if guides.emergency_contact is not None:
            assert guides.emergency_contact == self.add_guide_page.emergency_contact.text
        if guides.hire_date is not None:
            assert guides.hire_date == self.add_guide_page.hire_date.text
        if guides.end_date is not None:
            assert guides.end_date == self.add_guide_page.end_date.text
        if guides.bank_name is not None:
            assert guides.bank_name == self.add_guide_page.bank_name.text
        if guides.account_type is not None:
            assert guides.account_type == self.add_guide_page.account_type.text
        if guides.bank_routing_number is not None:
            assert guides.bank_routing_number == self.add_guide_page.bank_routing_number.text
        if guides.account_number is not None:
            assert guides.account_number == self.add_guide_page.account_number.text
        assert guides.pay_rate_type == self.add_guide_page.get_selected_value(self.add_guide_page.pay_rate_type)
        if guides.trained_activities is not None:
            assert guides.trained_activities == self.add_guide_page.trained_activity.text

    def add_guide_with_invalid_username(self, guides):
        self.add_guide_form()
        self.add_guide_page.username.send_keys(guides.username)
        self.add_guide_page.empty_space.click()
        wait(lambda: len(self.add_guide_page.bootstrap_alert.text) > 0)
        print(self.add_guide_page.bootstrap_alert.text)
        assert "Username ({}) not valid.".format(guides.username) == self.add_guide_page.bootstrap_alert.text

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
        expected_name = guides.first_name + " " + guides.last_name + " (pending)"
        assert expected_name == self.people_hub_page.name.text

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
        assert quantity == len(self.add_guide_page.error_messages)
        for notification in self.add_guide_page.error_messages:
            assert wording == notification.text

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
