from datetime import datetime, timedelta

import pytz
from webium import wait
from webium.wait import wait

from pages.admin_certificate import CertificatePage
from pages.navigation_bar import NavigationBar


class CertificateActions:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.certificate_page = CertificatePage(driver=self.driver)
        self.now = ""
        self.purchase_datetime = ""
        self.purchase_datetime_plus_one_minute = ""

    def select_certificate(self, cert):
        self.navigate_to()
        wait(lambda: self.certificate_page.first_row_code.text != "", timeout_seconds=30, waiting_for="the table")
        self.certificate_page.add_new_certificate_button.click()
        self.certificate_page.select_type(cert.certificate_type)
        self.certificate_page.first_name_input.send_keys(cert.first_name)
        self.certificate_page.last_name_input.send_keys(cert.last_name)
        self.certificate_page.email_input.send_keys(cert.email)
        self.enter_initial_amount(cert)
        self.select_activity_and_tickets(cert)
        self.check_initial_amount(cert)

    def make_successful_payment(self, cert):
        self.certificate_page.select_charge_type(cert.cert_charge_type)

        self.enter_payment_information(cert.cert_charge_type, cert.cert_card_number, cert.cert_card_date,
                                       cert.cert_card_cvc, cert.cert_card_zip, cert.cert_check_number)
        self.get_purchase_datetime()
        self.certificate_page.click_save_button()

    def make_declined_payment(self, cert):
        self.certificate_page.select_charge_type(cert.cert_charge_type)
        self.enter_payment_information(cert.cert_charge_type, cert.cert_declined_card_number, cert.cert_card_date,
                                       cert.cert_card_cvc, cert.cert_card_zip, cert.cert_check_number)
        self.certificate_page.save_button.click()
        wait(lambda: self.certificate_page.payment_alert.is_displayed(), timeout_seconds=100)
        assert "Credit card declined: please try again." == self.certificate_page.payment_alert.text
        self.certificate_page.payment_alert_button.click()
        wait(lambda: len(self.certificate_page.modal_pop_up) == 1)

    def verify_created_certificate(self, cert):
        expected_name = cert.first_name + " " + cert.last_name
        wait(lambda: self.certificate_page.first_row_name.text == expected_name, timeout_seconds=100,
             waiting_for="updating data in the table")
        assert expected_name == self.certificate_page.first_row_name.text
        assert cert.email == self.certificate_page.first_row_email.text
        expected_initial_amount = "$" + "{0:,.2f}".format(float(cert.initial_amount))
        assert expected_initial_amount == self.certificate_page.first_row_initial_amount.text
        expected_remain_amount = "$" + "{0:,.2f}".format(float(cert.initial_amount))
        assert expected_remain_amount == self.certificate_page.first_row_remain_amount.text
        assert self.purchase_datetime == self.certificate_page.first_row_purchase_date.text or \
            self.purchase_datetime_plus_one_minute == self.certificate_page.first_row_purchase_date.text
        if cert.certificate_type != "Specific Dollar Amount":
            assert cert.cert_activity == self.certificate_page.first_row_activity.text
        if cert.cert_name_first_tickets_type is not None:
            assert cert.cert_name_first_tickets_type in self.certificate_page.first_row_ticket_types.text,\
                "The first tickets type is not in the table!"
        if cert.cert_name_second_tickets_type is not None:
            assert cert.cert_name_second_tickets_type in self.certificate_page.first_row_ticket_types.text, \
                "The second tickets type is not in the table!"
        if cert.cert_name_third_tickets_type is not None:
            assert cert.cert_name_third_tickets_type in self.certificate_page.first_row_ticket_types.text, \
                "The third tickets type is not in the table!"
        if cert.cert_first_tickets_type is not None:
            assert cert.cert_first_tickets_type in self.certificate_page.first_row_quantity.text, \
                "Wrong amount of first tickets in the table!"
        if cert.cert_second_tickets_type is not None:
            assert cert.cert_second_tickets_type in self.certificate_page.first_row_quantity.text, \
                "Wrong amount of second tickets in the table!"
        if cert.cert_third_tickets_type is not None:
            assert cert.cert_third_tickets_type in self.certificate_page.first_row_quantity.text, \
                "Wrong amount of third tickets in the table!"

    def copy_the_code(self, order):
        order.gift_certificate_code = self.certificate_page.first_row_code.text

    def verify_remain_amount(self, order):
        assert order.remain_amount_after == self.certificate_page.first_row_remain_amount.text

    def get_purchase_datetime(self):
        self.now = datetime.now(tz=pytz.timezone('US/Central'))
        self.purchase_datetime = self.now.strftime('%m/%d/%Y %I:%M %p CT').lstrip("0")\
            .replace(" 0", " ").replace("/0", "/")
        self.purchase_datetime_plus_one_minute = self.now + timedelta(minutes=1)
        self.purchase_datetime_plus_one_minute = self.purchase_datetime_plus_one_minute\
            .strftime('%m/%d/%Y %I:%M %p CT').lstrip("0").replace(" 0", " ").replace("/0", "/")
        return self.purchase_datetime, self.purchase_datetime_plus_one_minute

    def enter_payment_information(self, charge_type, card_number, card_date, card_cvc, card_zip, check_number):
        if charge_type == 'creditcard':
            self.certificate_page.enter_cc_info(card_number, card_date, card_cvc, card_zip)
        elif charge_type == 'Check':
            self.certificate_page.check_number_input.send_keys(check_number)

    def check_initial_amount(self, cert):
        if cert.certificate_type == "Activity Tickets":
            initial_amount = self.certificate_page.initial_amount_input.get_attribute("value")
            expected_result = float(cert.initial_amount)
            if expected_result.is_integer():
                assert initial_amount == "%g" % expected_result
            else:
                assert initial_amount == "{}".format(expected_result)

    def select_activity_and_tickets(self, cert):
        if cert.cert_activity is not None:
            self.certificate_page.select_activity(cert.cert_activity)
            if cert.cert_first_tickets_type is not None:
                self.certificate_page.first_tickets_type_input.send_keys(cert.cert_first_tickets_type)
            if cert.cert_second_tickets_type is not None:
                self.certificate_page.second_tickets_type_input.send_keys(cert.cert_second_tickets_type)
            if cert.cert_third_tickets_type is not None:
                self.certificate_page.third_tickets_type_input.send_keys(cert.cert_third_tickets_type)
            if cert.cert_fourth_tickets_type is not None:
                self.certificate_page.fourth_tickets_type_input.send_keys(cert.cert_fourth_tickets_type)

    def enter_initial_amount(self, cert):
        if cert.certificate_type == "Specific Dollar Amount" and cert.initial_amount is not None:
            self.certificate_page.initial_amount_input.clear()
            self.certificate_page.initial_amount_input.send_keys(cert.initial_amount)
        self.certificate_page.charge_type_label.click()

    def navigate_to(self):
        if "/giftcertificate.aspx" not in self.app.current_url():
            wait(lambda: self.navigation_bar.main_actions_drop_down is not None, timeout_seconds=20)
            self.navigation_bar.main_actions_drop_down.click()
            self.navigation_bar.sell_gift_certificates.click()
        elif self.certificate_page.certificate_pop_up() is True:
            self.certificate_page.click_cancel_button()

    def find_by_code(self, order):
        self.certificate_page.search_input.send_keys(order.gift_certificate_code)
        wait(lambda: self.certificate_page.first_row_code.text == order.gift_certificate_code)
