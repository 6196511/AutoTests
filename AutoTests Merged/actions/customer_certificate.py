from time import sleep

from webium.wait import wait

from pages.customer_certificate import CustomerCertPage


class CustomerCertActions:

    def __init__(self, app):
        self.driver = app.driver
        self.certificate = None

    def open_page(self, certificate):
        self.certificate = CustomerCertPage(driver=self.driver, url=certificate.customer_URL)
        self.certificate.open()
        self.close_alert()

    def fill_first_form(self, cert):
        self.certificate.select(self.certificate.certificate_type, cert.certificate_type)
        self.certificate.email.send_keys(cert.email)
        self.certificate.first_name.send_keys(cert.first_name)
        self.certificate.last_name.send_keys(cert.last_name)
        if cert.certificate_type == "Specific Dollar Amount":
            self.certificate.initial_amount.send_keys(cert.initial_amount)
        if cert.activity is not None:
            self.certificate.select(self.certificate.activity, cert.activity)
            if cert.first_tickets_type is not None:
                self.certificate.first_tickets_type.send_keys(cert.first_tickets_type)
            if cert.second_tickets_type is not None:
                self.certificate.second_tickets_type.send_keys(cert.second_tickets_type)
            if cert.third_tickets_type is not None:
                self.certificate.third_tickets_type.send_keys(cert.third_tickets_type)
        self.certificate.empty_space.click()

    def verify_payment_info(self, cert):
        if cert.certificate_type == "Activity Tickets":
            assert self.certificate.initial_amount.text == cert.initial_amount, "Wrong initial amount! '%s'" % \
                                                                                self.certificate.initial_amount.text
        assert self.certificate.booking_fee.text == cert.booking_fee, "Wrong booking fee! '%s'" % \
                                                                      self.certificate.booking_fee.text
        assert self.certificate.total_amount.text == cert.total_amount, "Wrong total amount! '%s'" % \
                                                                        self.certificate.total_amount.text
        wait(lambda: self.certificate.next_step_button.is_enabled())
        self.certificate.next_step_button.click()
        assert self.certificate.full_charge.text == cert.total_amount, "Wrong full charge! '%s'" % \
                                                                       self.certificate.full_charge.text

    def make_successful_payment(self, cert):
        self.certificate.enter_cc_info(cert.card_number, cert.card_date, cert.card_cvc, cert.card_zip)
        wait(lambda: self.certificate.pay_button.is_enabled())
        attempt = 0
        while self.certificate.pay_button.is_enabled() and attempt < 15:
            self.certificate.pay_button.click()
            attempt += 1
            sleep(1)

    def make_declined_payment(self, cert):
        self.certificate.enter_cc_info(cert.declined_card_number, cert.card_date, cert.card_cvc, cert.card_zip)
        wait(lambda: self.certificate.pay_button.is_enabled())
        self.certificate.pay_button.click()
        wait(lambda: len(self.certificate.payment_notification.text) > 0, timeout_seconds=100)
        assert self.certificate.payment_notification.text == "Credit card declined: please try again.",\
            "Wrong text of the final alert: '%s'" % self.certificate.payment_notification.text

    def verify_summary_details(self, cert):
        self.certificate.close_final_alert()
        assert self.certificate.customer.text == "%s %s" % (cert.first_name, cert.last_name)
        assert self.certificate.email_sd.text == cert.email
        assert self.certificate.amount.text == cert.initial_amount
        assert len(self.certificate.gift_code.text) == 15, "Someting with gift code: '%s'" % self.certificate.gift_code.text

    def close_alert(self):
        self.certificate.close_alert()
