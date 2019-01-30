import datetime

from webium.wait import wait

from pages.admin_booking import AdminBookingPage
from pages.navigation_bar import NavigationBar


class AdminBooking:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.booking_page = AdminBookingPage(driver=self.driver)

    def select_event(self, tickets):
        self.navigate_to()
        self.booking_page.select_activity(tickets.activity)
        self.select_tickets(tickets)
        self.booking_page.select_date(tickets.year, tickets.month, tickets.day)
        self.booking_page.select_time(tickets.time)
        wait(lambda: self.booking_page.order_cart.is_displayed())

    def select_activity_and_day(self, order):
        self.navigate_to()
        self.booking_page.select_activity(order.activity)
        self.select_tickets(order)
        self.booking_page.select_date(order.year, order.month, order.day)

    def verify_time_list(self, time):
        wait(lambda: len(self.booking_page.get_time_list()) > 1)
        time_list = self.booking_page.get_time_list()
        time_options = []
        for time in time_list:
            time_options.append(time.text)
        assert time not in time_options, time_options

    def select_today_event(self, tickets):
        purchase_date = datetime.date.today()
        tickets.year = str(purchase_date.year)
        tickets.month = str(purchase_date.month)
        tickets.day = str(purchase_date.day)
        self.select_event(tickets)

    def close_booking_is_over_alert(self):
        self.wait_pop_up_displayed()
        self.booking_page.discount_pop_up_ok_button.click()
        self.booking_page.wait_pop_up_closed()

    def navigate_to(self):
        wait(lambda: self.navigation_bar.main_tab is not None, timeout_seconds=20)
        wait(lambda: not self.navigation_bar.page_loader_wrapper.is_displayed(), timeout_seconds=20)
        self.navigation_bar.main_tab.click()
        self.navigation_bar.sell_tickets.click()
        wait(lambda: self.navigation_bar.expanded_list)
        self.navigation_bar.add_booking.click()

    def select_tickets(self, tickets):
        if tickets.first_tickets_type is not None:
            self.booking_page.first_tickets_type.send_keys(tickets.first_tickets_type)
            self.booking_page.empty_space_first_tab.click()
            self.wait_pricing_table_updating()
        if tickets.second_tickets_type is not None:
            self.booking_page.second_tickets_type.send_keys(tickets.second_tickets_type)
            self.wait_pricing_table_updating()
        if tickets.third_tickets_type is not None:
            self.booking_page.third_tickets_type.send_keys(tickets.third_tickets_type)
            self.wait_pricing_table_updating()
        if tickets.fourth_tickets_type is not None:
            self.booking_page.fourth_tickets_type.send_keys(tickets.fourth_tickets_type)
            self.wait_pricing_table_updating()
        self.booking_page.empty_space_first_tab.click()

    def wait_pricing_table_updating(self):
        wait(lambda: self.booking_page.grand_total.text != '$0.00', timeout_seconds=20)

    def apply_custom_price(self, tickets):
        self.booking_page.custom_price.send_keys(tickets.custom_price)
        self.booking_page.empty_space_first_tab.click()

    def apply_valid_promo_code(self, tickets):
        self.enter_promo_code(tickets)
        expected_notification = "The promo code {} has been applied to {}.".format(tickets.promo_code, tickets.activity)
        assert expected_notification == self.booking_page.discount_pop_up.text
        self.booking_page.discount_pop_up_ok_button.click()
        self.booking_page.wait_pop_up_closed()

    def apply_valid_gift_cert(self, order):
        self.enter_gift_cert(order)
        expected_notification = "Your gift code has been applied to this order!"
        assert expected_notification == self.booking_page.discount_pop_up.text
        self.booking_page.discount_pop_up_ok_button.click()
        self.booking_page.wait_pop_up_closed()

    def apply_invalid_promo_code(self, tickets):
        self.enter_promo_code(tickets)
        expected_notification = "Sorry, the promo code {} is not valid for your selected events.".format(
            tickets.promo_code)
        assert expected_notification == self.booking_page.discount_pop_up.text
        self.booking_page.discount_pop_up_ok_button.click()
        self.booking_page.wait_pop_up_closed()

    def wait_pop_up_displayed(self):
        wait(lambda: self.booking_page.discount_pop_up.is_displayed())

    def enter_promo_code(self, tickets):
        self.booking_page.promo_code_input.send_keys(tickets.promo_code)
        self.booking_page.apply_discount.click()
        self.wait_pop_up_displayed()

    def enter_gift_cert(self, order):
        self.booking_page.gift_certificate_input.send_keys(order.gift_certificate_code)
        self.booking_page.apply_discount.click()
        self.wait_pop_up_displayed()

    def select_addon(self, order):
        self.booking_page.addons_link.click()
        wait(lambda: len(self.booking_page.addons_list) > 0)
        for addon in self.booking_page.addons_list:
            if addon.name.text.startswith(order.addon_name):
                addon.checkbox.click()
                self.booking_page.select(addon.type_list, order.addon_type)
                self.booking_page.add_to_cart.click()
                break

    def addon_not_present(self, order):
        self.booking_page.addons_link.click()
        wait(lambda: len(self.booking_page.addons_list) > 0)
        for addon in self.booking_page.addons_list:
            assert addon.name.text != order.addon_name
        self.booking_page.cancel_addon.click()

    def type_not_present(self, order):
        self.booking_page.addons_link.click()
        wait(lambda: len(self.booking_page.addons_list) > 0)
        for addon in self.booking_page.addons_list:
            if addon.name.text == order.addon_name:
                addon.checkbox.click()
                options = self.booking_page.get_options(addon.type_list)
                for opt in options:
                    assert order.addon_type != opt.text
        self.booking_page.cancel_addon.click()

    def fill_out_customer_info(self, tickets):
        self.booking_page.click_enter_customer_information()
        self.booking_page.first_name.send_keys(tickets.first_name)
        self.booking_page.last_name.send_keys(tickets.last_name)
        self.booking_page.email_address.send_keys(tickets.email)
        if tickets.phone is not None:
            self.booking_page.phone_number.send_keys(tickets.phone)
        self.booking_page.zip_code.send_keys(tickets.zip_code)
        self.booking_page.empty_space.click()
        self.booking_page.complete_booking_button.click()

    def submit_declined_card(self, tickets):
        self.booking_page.select_payment_type(tickets.payment_type)
        self.booking_page.enter_cc_info(tickets.declined_card_number, tickets.card_date, tickets.card_cvc,
                                        tickets.card_zip)
        self.booking_page.submit_booking_button.click()
        wait(lambda: self.booking_page.final_alert.is_displayed(), timeout_seconds=100)
        assert "Credit card declined: please try again." == self.booking_page.final_alert.text
        self.booking_page.final_alert_ok_button.click()

    def select_payment_method(self, tickets):
        if tickets.payment_type is not None:
            self.booking_page.select_payment_type(tickets.payment_type)
        if tickets.payment_type == "Credit Card":
            if tickets.saved_card is None:
                self.booking_page.enter_cc_info(tickets.card_number, tickets.card_date, tickets.card_cvc,
                                                tickets.card_zip)
            else:
                self.booking_page.select_saved_card(tickets.saved_card)
        elif tickets.payment_type == "Cash":
            if tickets.cash_recieved:
                self.booking_page.cash_recieved.click()

    def verify_payment_table(self, tickets):
        assert tickets.ticket_total == self.booking_page.ticket_total.text
        assert tickets.discount == self.booking_page.discount.text
        assert tickets.gift_certificate == self.booking_page.giftcertificate.text
        if tickets.addon is not None:
            assert tickets.addon == self.booking_page.addons.text
        assert tickets.taxes == self.booking_page.taxes.text
        assert tickets.booking_fee == self.booking_page.booking_fee.text
        assert tickets.grand_total == self.booking_page.grand_total.text

    def submit_successful_booking(self):
        self.booking_page.submit_booking_button.click()
        wait(lambda: self.booking_page.final_alert.is_displayed(), timeout_seconds=200)
        assert "Booking Successful!" == self.booking_page.final_alert.text, "Wrong text on the final pop-up."
        self.booking_page.final_alert_ok_button.click()
