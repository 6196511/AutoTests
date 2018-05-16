from pages.admin_booking import AdminBookingPage
from pages.navigation_bar import NavigationBar
from webium.wait import wait
from time import sleep


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
        self.booking_page.select_date(tickets.year, tickets.month, tickets.day, tickets.grand_total)
        self.booking_page.select_time(tickets.time)

    def navigate_to(self):
        self.navigation_bar.main_actions_drop_down.click()
        self.navigation_bar.add_a_booking.click()

    def select_tickets(self, tickets):
        if tickets.first_tickets_type is not None:
            self.booking_page.first_tickets_type.send_keys(tickets.first_tickets_type)
        if tickets.second_tickets_type is not None:
            self.booking_page.second_tickets_type.send_keys(tickets.second_tickets_type)
        if tickets.third_tickets_type is not None:
            self.booking_page.third_tickets_type.send_keys(tickets.third_tickets_type)
        if tickets.fourth_tickets_type is not None:
            self.booking_page.fourth_tickets_type.send_keys(tickets.fourth_tickets_type)
        self.booking_page.empty_space_first_tab.click()

    def fill_out_customer_info(self, tickets):
        self.booking_page.click_enter_customer_information()
        self.booking_page.first_name.send_keys(tickets.first_name)
        self.booking_page.last_name.send_keys(tickets.last_name)
        self.booking_page.email_address.send_keys(tickets.email)
        self.booking_page.phone_number.send_keys(tickets.phone)
        self.booking_page.zip_code.send_keys(tickets.zip_code)
        self.booking_page.empty_space.click()
        self.booking_page.complete_booking_button.click()

    def submit_declined_card(self, tickets):
        self.booking_page.select_payment_type(tickets.payment_type)
        self.booking_page.enter_cc_info(tickets.declined_card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
        self.booking_page.submit_booking_button.click()
        wait(lambda: self.booking_page.final_alert.is_displayed(), timeout_seconds=100)
        assert self.booking_page.final_alert.text == "Credit card declined: please try again.",\
            "Wrong text of the final alert: '%s'" % self.booking_page.final_alert.text
        self.booking_page.final_alert_ok_button.click()
        sleep(1)

    def select_payment_method(self, tickets):
        self.booking_page.select_payment_type(tickets.payment_type)
        if tickets.payment_type == "Credit Card":
            if tickets.saved_card is None:
                self.booking_page.enter_cc_info(tickets.card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
            else:
                self.booking_page.select_saved_card(tickets.saved_card)
        elif tickets.payment_type == "Cash":
            if tickets.cash_recieved:
                self.booking_page.cash_recieved.click()

    def verify_payment_table(self, tickets):
        assert self.booking_page.ticket_total.text == tickets.ticket_total, "Wrong ticket total!"
        assert self.booking_page.discount.text == tickets.discount, "Wrong discount!"
        assert self.booking_page.giftcertificate.text == tickets.gift_certificate, "Wrong discount (gift certificate)!"
        assert self.booking_page.taxes.text == tickets.taxes, "Wrong taxes!"
        assert self.booking_page.booking_fee.text == tickets.booking_fee, "Wrong booking fee!"
        assert self.booking_page.grand_total.text == tickets.grand_total, "Wrong grand total! %s" % \
                                                                          self.booking_page.grand_total.text

    def submit_successful_booking(self):
        self.booking_page.submit_booking_button.click()
        wait(lambda: self.booking_page.final_alert.is_displayed(), timeout_seconds=100)
        assert self.booking_page.final_alert.text == "Booking Successful!", "Wrong text of the final alert: '%s'" % \
                                                                            self.booking_page.final_alert.text
        self.booking_page.final_alert_ok_button.click()

    def refresh_page(self):
        self.booking_page._driver.refresh()

