from calendar import month_name
from time import sleep

from webium.wait import wait

from pages.customer_booking import CustomerBookingPage


class CustomerActions:

    def __init__(self, app, domain):
        self.driver = app.driver
        self.booking = None
        self.domain = domain
        self.url = ""

    def open_page(self, tickets):
        self.url = self.domain + tickets.URL_tickets
        self.booking = CustomerBookingPage(driver=self.driver, url=self.url)
        self.booking.open()
        self.booking.close_alert()

    def select_tickets_buttons(self, tickets):
        if tickets.first_tickets_type is not None:
            self.booking.click_tickets(self.booking.first_plus_button, tickets.first_tickets_type)
        if tickets.second_tickets_type is not None:
            self.booking.click_tickets(self.booking.second_plus_button, tickets.second_tickets_type)
        if tickets.third_tickets_type is not None:
            self.booking.click_tickets(self.booking.third_plus_button, tickets.third_tickets_type)
        if tickets.fourth_tickets_type is not None:
            self.booking.click_tickets(self.booking.fourth_plus_button, tickets.fourth_tickets_type)
        wait(lambda: self.booking.next_button_1.is_enabled())
        self.booking.next_button_1.click()

    def select_tickets_input(self, tickets):
        wait(lambda: self.booking.first_tickets_type_input.is_enabled())
        if tickets.first_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.first_tickets_type_input.send_keys(tickets.first_tickets_type)
        if tickets.second_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.second_tickets_type_input.send_keys(tickets.second_tickets_type)
        if tickets.third_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.third_tickets_type_input.send_keys(tickets.third_tickets_type)
        if tickets.fourth_tickets_type is not None:
            self.booking.first_tickets_type_input.clear()
            self.booking.fourth_tickets_type_input.send_keys(tickets.fourth_tickets_type)
        self.booking.empty_space_first_page.click()
        wait(lambda: self.booking.next_button_1.is_enabled())
        self.booking.next_button_1.click()

    def select_date(self, tickets):
        wait(lambda: self.booking.calendar.is_displayed(), )
        self.booking._driver.execute_script(
            "$('#datepicker').datepicker('setDate', new Date(%s, %s-1, %s))" % (tickets.year, tickets.month,
                                                                                tickets.day))
        self.booking.click_date(tickets.day)
        self.booking.next_button_2.click()

    def select_time(self, tickets):
        self.booking.pick_this_time(tickets.time)
        wait(lambda: self.booking.next_button_3.is_enabled())
        self.booking.next_button_3.click()

    def time_is_unavailable(self, time):
        assert time not in self.booking.get_time_list()

    def fill_info(self, tickets):
        self.booking.first_name_input.send_keys(tickets.first_name)
        self.booking.last_name_input.send_keys(tickets.last_name)
        self.booking.phone_input.send_keys(tickets.phone)
        self.booking.email_input.send_keys(tickets.email)
        self.booking.zip_input.send_keys(tickets.zip_code)
        self.answer_questions()
        self.booking.empty_space_fourth_page.click()
        self.booking.scroll_down()
        self.booking.next_button_4.click()

    def skip_addons(self):
        if self.booking.addons_present():
            wait(lambda: self.booking.next_button_5.is_displayed() and self.booking.next_button_5.is_enabled())
            self.booking.next_button_5.click()

    def apply_valid_promo_code(self, tickets):
        wait(lambda: len(self.booking.tickets_cost.text) > 0, waiting_for="Final Step: Checkout page shows up.",
             timeout_seconds=15)
        self.booking.promo_code_input.send_keys(tickets.promo_code)
        wait(lambda: self.booking.promo_code_button.is_enabled())
        self.booking.promo_code_button.click()
        wait(lambda: self.booking.discount_pop_up.is_displayed(), timeout_seconds=15,
             waiting_for="discount notification.")
        expected_notification = "Your promo code ({}) was applied.".format(tickets.promo_code)
        assert expected_notification == self.booking.discount_pop_up.text
        self.booking.discount_pop_up_ok_button.click()

    def apply_invalid_promo_code(self, tickets):
        self.booking.promo_code_input.send_keys(tickets.promo_code)
        wait(lambda: self.booking.promo_code_button.is_enabled())
        self.booking.promo_code_button.click()
        wait(lambda: self.booking.discount_pop_up.is_displayed(), timeout_seconds=15,
             waiting_for="discount notification.")
        assert "The code is invalid" == self.booking.discount_pop_up.text
        self.booking.discount_pop_up_ok_button.click()

    def redeem_gift_certificate(self, tickets):
        wait(lambda: len(self.booking.total_price.text) > 0, timeout_seconds=15)
        self.booking.gift_certificate_input.send_keys(tickets.gift_certificate_code)
        wait(lambda: self.booking.gift_certificate_button.is_enabled())
        self.booking.gift_certificate_button.click()
        wait(lambda: self.booking.discount_pop_up.is_displayed(), timeout_seconds=15,
             waiting_for="discount notification.")
        expected_notification = "Your gift certificate ({}) was applied.".format(tickets.gift_certificate_code)
        assert expected_notification == self.booking.discount_pop_up.text
        self.booking.discount_pop_up_ok_button.click()

    def redeem_invalid_gift_certificate(self, tickets):
        wait(lambda: len(self.booking.total_price.text) > 0, timeout_seconds=15)
        self.booking.gift_certificate_input.send_keys(tickets.gift_certificate_code)
        wait(lambda: self.booking.gift_certificate_button.is_enabled())
        self.booking.gift_certificate_button.click()
        wait(lambda: self.booking.discount_pop_up.is_displayed(), timeout_seconds=15,
             waiting_for="discount notification.")
        expected_notification = "This code of gift certificate ({}) is not valid. Please make sure you spelled " \
                                "the code you were given correctly.".format(tickets.gift_certificate_code)
        assert expected_notification == self.booking.discount_pop_up.text
        self.booking.discount_pop_up_ok_button.click()

    def verify_payment_page(self, tickets):
        wait(lambda: len(self.booking.checkout_activity.text) > 0, timeout_seconds=15)
        assert tickets.activity == self.booking.checkout_activity.text
        month = month_name[int(tickets.month)]
        date = "{} {}, {}".format(month, tickets.day, tickets.year)
        wait(lambda: self.booking.checkout_date.is_displayed())
        assert date == self.booking.checkout_date.text
        assert tickets.ticket_total == self.booking.tickets_cost.text
        taxes_fees = float(tickets.taxes) + float(tickets.booking_fee)
        assert "{:.2f}".format(taxes_fees) == self.booking.tax.text
        if tickets.discount != "0.00":
            wait(lambda: len(self.booking.checkout_discount.text) > 0, timeout_seconds=5)
            assert tickets.discount == self.booking.checkout_discount.text
        assert tickets.grand_total == self.booking.total_price.text

    def submit_declined_card(self, tickets):
        self.booking.enter_cc_info(tickets.declined_card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
        wait(lambda: self.booking.next_button_6.is_enabled())
        self.booking.next_button_6.click()
        wait(lambda: len(self.booking.payment_notification.text) > 0, timeout_seconds=100)
        assert "Credit card declined: please try again." == self.booking.payment_notification.text

    def make_payment(self, tickets):
        if tickets.payment_type is None:
            wait(lambda: self.booking.next_button_6.is_enabled())
            self.booking.next_button_6.click()
        else:
            self.booking.enter_cc_info(tickets.card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
            wait(lambda: self.booking.next_button_6.is_enabled())
            self.booking.next_button_6.click()

    def refill_payment_info(self, tickets):
        self.booking.enter_cc_info(tickets.card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
        wait(lambda: self.booking.next_button_6.is_enabled(), timeout_seconds=60)
        attempt = 0
        while self.booking.next_button_6.text == 'Get Your Tickets!' and attempt < 10:
            self.booking.next_button_6.click()
            attempt += 1
            sleep(1)

    def verify_summary_details(self, tickets):
        wait(lambda: self.booking.customer_information.is_displayed(), timeout_seconds=60,
             waiting_for="Summary Detais is displayed")
        assert tickets.first_name + ' ' + tickets.last_name == self.booking.customer_information.text
        assert tickets.zip_code == self.booking.zip_information.text
        assert tickets.phone == self.booking.phone_information.text
        assert tickets.email == self.booking.email_information.text
        assert "$" + tickets.ticket_total == self.booking.ticket_total.text
        assert "$" + tickets.booking_fee == self.booking.booking_fee.text
        assert "$" + tickets.discount == self.booking.discount.text
        assert "$" + tickets.taxes == self.booking.tax_information.text
        assert "$" + tickets.grand_total == self.booking.grand_total.text

    def answer_questions(self):
        for input in self.booking.question_inputs:
            input.send_keys('test')
