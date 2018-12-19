from time import sleep

from webium.wait import wait

from pages.customer_certificate import CustomerCertPage


class CustomerCertActions:

    def __init__(self, app, domain):
        self.driver = app.driver
        self.certificate = None
        self.domain = domain
        self.url = ""

    def open_page(self, certificate):
        self.url = self.domain + certificate.URL_cert
        self.certificate = CustomerCertPage(driver=self.driver, url=self.url)
        self.certificate.open()
        self.close_alert()

    def fill_first_form(self, cert):
        self.certificate.select(self.certificate.certificate_type, cert.certificate_type)
        self.certificate.email.send_keys(cert.email)
        self.certificate.first_name.send_keys(cert.first_name)
        self.certificate.last_name.send_keys(cert.last_name)
        if cert.certificate_type == "Specific Dollar Amount":
            self.certificate.initial_amount.send_keys(cert.initial_amount)
        if cert.cert_activity is not None:
            self.certificate.select(self.certificate.activity, cert.cert_activity)
            if cert.cert_first_tickets_type is not None:
                self.certificate.first_tickets_type.send_keys(cert.cert_first_tickets_type)
            if cert.cert_second_tickets_type is not None:
                self.certificate.second_tickets_type.send_keys(cert.cert_second_tickets_type)
            if cert.cert_third_tickets_type is not None:
                self.certificate.third_tickets_type.send_keys(cert.cert_third_tickets_type)
            if cert.cert_fourth_tickets_type is not None:
                self.certificate.fourth_tickets_type.send_keys(cert.cert_fourth_tickets_type)
        self.certificate.empty_space.click()

    def verify_payment_info(self, cert):
        if cert.certificate_type == "Activity Tickets":
            assert cert.initial_amount == self.certificate.initial_amount.text
        assert cert.cert_booking_fee == self.certificate.booking_fee.text
        assert cert.cert_total_amount == self.certificate.total_amount.text
        wait(lambda: self.certificate.next_step_button.is_enabled())
        self.certificate.next_step_button.click()
        assert cert.cert_total_amount == self.certificate.full_charge.text

    def make_successful_payment(self, cert):
        self.certificate.enter_cc_info(cert.cert_card_number, cert.cert_card_date, cert.cert_card_cvc,
                                       cert.cert_card_zip)
        wait(lambda: self.certificate.pay_button.is_enabled())
        attempt = 0
        while self.certificate.pay_button.is_enabled() and attempt < 15:
            self.certificate.pay_button.click()
            attempt += 1
            sleep(1)

    def make_declined_payment(self, cert):
        self.certificate.enter_cc_info(cert.cert_declined_card_number, cert.cert_card_date, cert.cert_card_cvc,
                                       cert.cert_card_zip)
        wait(lambda: self.certificate.pay_button.is_enabled())
        self.certificate.pay_button.click()
        wait(lambda: len(self.certificate.payment_notification.text) > 0, timeout_seconds=100)
        assert "Credit card declined: please try again." == self.certificate.payment_notification.text,\
            "Wrong text on the final alert."

    def verify_summary_details(self, cert):
        self.certificate.close_final_alert()
        assert "{} {}".format(cert.first_name, cert.last_name) == self.certificate.customer.text
        assert self.certificate.email_sd.text == cert.email
        assert self.certificate.amount.text == cert.initial_amount
        expected_length_of_giftcode = 16
        assert expected_length_of_giftcode == len(self.certificate.gift_code.text)

    def close_alert(self):
        self.certificate.close_alert()

    def copy_the_code(self, order):
        order.gift_certificate_code = self.certificate.gift_code.text
