from calendar import month_name

from waiting import wait

from pages.customer_booking import CustomerBookingPage


class CustomerActions:

    def __init__(self, app):
        self.driver = app.driver
        self.booking = None

    def open_page(self, tickets):
        self.booking = CustomerBookingPage(driver=self.driver, url=tickets.customer_URL)
        self.booking.open()

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
        wait(lambda: self.booking.calendar.is_displayed())
        self.booking._driver.execute_script(
            "$('#datepicker').datepicker('setDate', new Date(%s, %s-1, %s))" % (tickets.year, tickets.month, tickets.day))
        self.booking.click_date(tickets.day)
        wait(lambda: self.booking.next_button_2.is_enabled())
        self.booking.next_button_2.click()

    def select_time(self, tickets):
        self.booking.pick_this_time(tickets.time)
        wait(lambda: self.booking.next_button_3.is_enabled())
        self.booking.next_button_3.click()

    def fill_info(self, tickets):
        self.booking.first_name_input.send_keys(tickets.first_name)
        self.booking.last_name_input.send_keys(tickets.last_name)
        self.booking.phone_input.send_keys(tickets.phone)
        self.booking.email_input.send_keys(tickets.email)
        self.booking.zip_input.send_keys(tickets.zip_code)
        self.booking.empty_space_fourth_page.click()
        wait(lambda: self.booking.next_button_4.is_enabled())
        self.booking.next_button_4.click()

    def verify_payment_page(self, tickets):
        assert self.booking.checkout_activity.text == tickets.activity
        month = month_name[int(tickets.month)]
        date = "%s %s, %s" % (month, tickets.day, tickets.year)
        wait(lambda: self.booking.checkout_date.is_displayed())
        assert self.booking.checkout_date.text == date, "Wrong date: %s" % self.booking.checkout_date.text
        assert self.booking.tickets_cost.text == tickets.ticket_total, "Wrong ticket cost on the payment page!"
        taxes_fees = float(tickets.taxes) + float(tickets.booking_fee)
        assert self.booking.tax.text == "%.2f" % taxes_fees, "Wrong Taxes & Fees on the payment page!"
        assert self.booking.total_price.text == tickets.grand_total, "Wrong grand total on the payment page! '%s'" % \
                                                                     self.booking.total_price.text

    def make_payment(self, tickets):
        self.booking.enter_cc_info(tickets.card_number, tickets.card_date, tickets.card_cvc, tickets.card_zip)
        wait(lambda: self.booking.next_button_5.is_enabled())
        self.booking.next_button_5.click()

    def verify_summary_details(self, tickets):
        wait(lambda: self.booking.customer_information.is_displayed())
        assert self.booking.customer_information.text == (tickets.first_name + ' ' + tickets.last_name), "Wrong customer!"
        assert self.booking.zip_information.text == tickets.zip_code, "Wrong zip code!"
        assert self.booking.phone_information.text == tickets.phone, "Wrong phone number!"
        assert self.booking.email_information.text == tickets.email, "Wrong email!"
        assert self.booking.ticket_total.text == ("$" + tickets.ticket_total), "Summary Details: Wrong ticket total!"
        assert self.booking.booking_fee.text == ("$" + tickets.booking_fee), "Summary Details: Wrong booking fee!"
        assert self.booking.discount.text == ("$" + tickets.discount), "Summary Details: Wrong discount!"
        assert self.booking.tax_information.text == ("$" + tickets.taxes), "Summary Details: Wrong tax!"
        assert self.booking.grand_total.text == ("$" + tickets.grand_total), "Summary Details: Wrong grand total!"

    def close(self):
        self.booking.close_window()
