from webium import BasePage, Find, Finds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webium.wait import wait


class CertificatePage(BasePage):

    # Current Gift Certificates page.

    add_new_certificate_button = Find(by=By.CSS_SELECTOR, value="[ng-click='vm.openAddGiftCertificateModal();']")
    first_row_name = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[2]")
    first_row_email = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[3]")
    first_row_initial_amount = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[4]")
    first_row_remain_amount = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[5]")
    first_row_purchase_date = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[6]")
    first_row_activity = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[7]")
    first_row_ticket_types = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[8]")
    first_row_quantity = Find(by=By.XPATH, value="//tbody/tr[contains(@ng-repeat, 'results')][1]/td[9]")

    # Add new certificate pop-up.

    modal_pop_up = Finds(by=By.CSS_SELECTOR, value=".modal-content")
    certificate_select = Find(by=By.ID, value="type")
    first_name_input = Find(by=By.CSS_SELECTOR, value="#firstname")
    last_name_input = Find(by=By.CSS_SELECTOR, value="#lastname")
    email_input = Find(by=By.CSS_SELECTOR, value="#email")
    initial_amount_input = Find(by=By.ID, value="initialamount")
    activity_list = Find(by=By.CSS_SELECTOR, value="#activity")
    first_tickets_type_input = Find(by=By.XPATH, value="//div[@ng-if='vm.selectedType.key===3']/div[2]//input")
    second_tickets_type_input = Find(by=By.XPATH, value="//div[@ng-if='vm.selectedType.key===3']/div[3]//input")
    third_tickets_type_input = Find(by=By.XPATH, value="//div[@ng-if='vm.selectedType.key===3']/div[3]//input")
    charge_type_label = Find(by=By.XPATH, value="//label[@for='chargetype']")
    charge_type_list = Find(by=By.CSS_SELECTOR, value="#chargetype")
    check_number_input = Find(by=By.CSS_SELECTOR, value="#charge_checknumbner")
    card_number_input = Find(by=By.XPATH, value="//input[contains(@class, '__PrivateStripeElement')]")
    card_date_input = Find(by=By.XPATH, value="//input[contains(@class, '__PrivateStripeElement')]")
    card_cvc_input = Find(by=By.XPATH, value="//input[contains(@class, '__PrivateStripeElement')]")
    card_zip_input = Find(by=By.XPATH, value="//input[contains(@class, '__PrivateStripeElement')]")
    save_button = Find(by=By.XPATH, value="//button[contains(.,'Save')]")
    cancel_button = Find(by=By.XPATH, value="//button[contains(.,'Cancel')]")

    def certificate_pop_up(self):
        return len(self.modal_pop_up) > 0

    def select_type(self, certificate_type):
        Select(self.certificate_select).select_by_visible_text(certificate_type)

    def select_activity(self, activity):
        if activity is not None:
            Select(self.activity_list).select_by_visible_text(activity)

    def select_charge_type(self, charge_type):
        self.charge_type_label.click()
        Select(self.charge_type_list).select_by_visible_text(charge_type)

    def click_save_button(self):
        self.save_button.click()
        wait(lambda: len(self.modal_pop_up) == 0)

    def click_cancel_button(self):
        self.cancel_button.click()
        wait(lambda: len(self.modal_pop_up) == 0)
