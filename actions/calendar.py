from calendar import month_name
from time import sleep

from pages.navigation_bar import NavigationBar
from pages.calendar import CalendarPage, EventManifest, CustomerEventPage
from webium.wait import wait


class Calendar:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.calendar_page = CalendarPage(driver=self.driver)
        self.event_manifest = EventManifest(driver=self.driver)
        self.customer_event = CustomerEventPage(driver=self.driver)

    def navigate_to(self):
        self.navigation_bar.calendar.click()

    def pick_event(self, order):
        wait(lambda: len(self.calendar_page.days_list) == 28)
        month = month_name[int(order.month)]
        our_date = "%s %s" % (month[:3], order.day)
        for day in self.calendar_page.days_list:
            if day.date.text == our_date:
                print(day.date.text)
                if day.is_element_present('view_all'):
                    day.view_all.click()
                    wait(lambda: len(day.events_list) > 5)
                wait(lambda: len(day.events_list) > 0)
                for event in day.events_list:
                    if event.activity_name.text == order.activity and event.time.text.startswith(order.time.lstrip("0")):
                        event.activity_name.click()
                        break
        wait(lambda: len(self.event_manifest.event_title.text) > 0, timeout_seconds=15)

    def select_event(self, order):
        if not self.event_manifest.is_element_present('event_title'):
            self.navigate_to()
            self.pick_event(order)
        elif self.event_manifest.event_title.text != order.activity or \
                self.event_manifest.event_date.text.find(order.time.lstrip("0")) == -1:
            self.event_manifest.close_button.click()
            self.pick_event(order)

    def verify_event_manifest(self, order):
        print()
        print(self.event_manifest.event_title.text)
        print(self.event_manifest.event_date.text)
        count = 0
        expected_name = order.first_name + " " + order.last_name
        print("Expected name: " + expected_name)
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            print(guest.name.text)
            if guest.name.text == expected_name:
                count += 1
                self.verify_amount_due(guest, order)
                assert guest.email.text == order.email, "Wrong email: '%s'" % guest.email.text
                print(guest.email.text)
                self.verify_tickets(guest, order)
        assert count == 1, count

    def verify_tickets(self, guest, order):
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for ticket in guest.tickets:
            tickets.append(ticket.text)
        assert sorted(tickets) == sorted(expected_tickets), "Error in tickets %s but expected %s" % \
                                                            (tickets, expected_tickets)

    def get_expected_tickets(self, order):
        expected_tickets = []
        if order.first_tickets_type is not None:
            expected_tickets.append(order.first_tickets_type + " x " + order.name_first_tickets_type)
        if order.second_tickets_type is not None:
            expected_tickets.append(order.second_tickets_type + " x " + order.name_second_tickets_type)
        if order.third_tickets_type is not None:
            expected_tickets.append(order.third_tickets_type + " x " + order.name_third_tickets_type)
        if order.fourth_tickets_type is not None:
            expected_tickets.append(order.fourth_tickets_type + " x " + order.name_fourth_tickets_type)
        return expected_tickets

    def verify_amount_due(self, guest, order):
        grand_total = order.grand_total
        grand_total = grand_total.replace(",", "")
        grand_total = grand_total.replace("$", "")
        grand_total = float(grand_total)
        booking_fee = order.booking_fee
        booking_fee = booking_fee.replace(",", "")
        booking_fee = booking_fee.replace("$", "")
        booking_fee = float(booking_fee)
        grand_total = grand_total - booking_fee
        if order.grand_total != "$0.00" and order.payment_type == "Cash" and order.cash_recieved is None:
            print("Total Paid: $0.00 Total Due: ${:.2f}".format(grand_total))
            print(guest.amount_due.text)
            assert guest.amount_due.text == "Total Paid: $0.00 Total Due: ${:.2f}".format(grand_total), guest.amount_due.text
            print("===========>>> He has to pay!")
        else:
            print("Paid in full : %s" % order.grand_total.replace(",", ""))
            print(guest.amount_due.text)
            assert guest.amount_due.text == "Paid in Full : ${:.2f}".format(grand_total), guest.amount_due.text
            print("Paid in full! <<<===========")

    def verify_customer_event_admin(self, order):
        self.go_to_customer_event_charges(order)
        assert self.customer_event.name.text == order.first_name + " " + order.last_name
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("%s x %s" % (row.quantity.text, row.type.text))
        assert sorted(tickets) == sorted(expected_tickets), "Error in tickets %s but expected %s" % \
                                                            (tickets, expected_tickets)
        assert self.customer_event.ticket_total.text == order.ticket_total
        if order.addon is not None:
            assert self.customer_event.addon.text == order.addon, \
                "%s but expected %s" % (self.customer_event.addon.text, order.addon)
        else:
            assert self.customer_event.addon.text == '$0.00', \
                "%s but expected %s" % (self.customer_event.addon.text, '$0.00')
        if order.discount != "- $0.00":
            assert self.customer_event.discount.text == "(%s)" % order.discount.lstrip("- "), \
                "%s but expected %s" % (self.customer_event.discount.text, order.discount.lstrip("- "))
        if order.gift_certificate != "- $0.00":
            assert self.customer_event.gift_certificate.text == "(%s)" % order.gift_certificate.lstrip("- "), \
                "%s but expected %s" % (self.customer_event.discount.text, order.gift_certificate.lstrip("- "))
        assert self.customer_event.booking_fee.text == order.booking_fee, \
            "%s but expected %s" % (self.customer_event.booking_fee.text, order.booking_fee)
        assert self.customer_event.tax.text == order.taxes, \
            "%s but expected %s" % (self.customer_event.tax.text, order.taxes)
        assert self.customer_event.grand_total.text == order.grand_total, \
            "%s but expected: %s" % (self.customer_event.grand_total.text, order.grand_total)
        if order.payment_type != "Cash" or order.cash_recieved is not None:
            assert self.customer_event.total_charges.text == order.grand_total, \
                "%s but expected: %s" % (self.customer_event.total_charges.text, order.grand_total)
        else:
            assert self.customer_event.total_charges.text == "$0.00", \
                "%s but expected: %s" % (self.customer_event.total_charges.text, "$0.00")
        if order.payment_type != "Cash" or order.cash_recieved is not None:
            assert self.customer_event.total_due.text == "0.00", \
                "%s but expected: %s" % (self.customer_event.total_due.text, "0.00")
        else:
            assert self.customer_event.total_due.text == order.grand_total, \
                "%s but expected: %s" % (self.customer_event.total_due.text, order.grand_total)

    def verify_customer_event_customer(self, order):
        self.go_to_customer_event_charges(order)
        assert self.customer_event.name.text == order.first_name + " " + order.last_name
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("%s x %s" % (row.quantity.text, row.type.text))
        assert sorted(tickets) == sorted(expected_tickets), "Error in tickets %s but expected %s" % \
                                                            (tickets, expected_tickets)
        assert self.customer_event.ticket_total.text == "$" + order.ticket_total
        if order.addon is not None:
            assert self.customer_event.addon.text == "$" + order.addon, \
                "%s but expected %s" % (self.customer_event.addon.text, "$" + order.addon)
        else:
            assert self.customer_event.addon.text == '$0.00', \
                "%s but expected %s" % (self.customer_event.addon.text, '$0.00')
        if order.discount != "0.00":
            assert self.customer_event.discount.text == "($%s)" % order.discount.lstrip("-"), \
                "%s but expected %s" % (self.customer_event.discount.text, "($%s)" % order.discount.lstrip("-"))
        if order.gift_certificate is not None:
            assert self.customer_event.gift_certificate.text == "($%s)" % order.gift_certificate.lstrip("-"), \
                "%s but expected %s" % (self.customer_event.gift_certificate.text, "($%s)" % order.gift_certificate.lstrip("-"))
        assert self.customer_event.booking_fee.text == "$" + order.booking_fee, \
            "%s but expected %s" % (self.customer_event.booking_fee.text, "$" + order.booking_fee)
        assert self.customer_event.tax.text == "$" + order.taxes, \
            "%s but expected %s" % (self.customer_event.tax.text, "$" + order.taxes)
        assert self.customer_event.grand_total.text == "$" + order.grand_total, \
            "%s but expected: %s" % (self.customer_event.grand_total.text, "$" + order.grand_total)
        assert self.customer_event.total_charges.text == "$" + order.grand_total, \
                "%s but expected: %s" % (self.customer_event.total_charges.text, "$" + order.grand_total)
        assert self.customer_event.total_due.text == "0.00", \
            "%s but expected: %s" % (self.customer_event.total_due.text, "0.00")

    def verify_customer_event_customer_cert(self, order):
        self.go_to_customer_event_charges(order)
        assert self.customer_event.name.text == order.first_name + " " + order.last_name
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("%s x %s" % (row.quantity.text, row.type.text))
        assert sorted(tickets) == sorted(expected_tickets), "Error in tickets %s but expected %s" % \
                                                            (tickets, expected_tickets)
        assert self.customer_event.ticket_total.text == "$" + order.ticket_total
        if order.addon is not None:
            assert self.customer_event.addon.text == "$" + order.addon, \
                "%s but expected %s" % (self.customer_event.addon.text, "$" + order.addon)
        else:
            assert self.customer_event.addon.text == '$0.00', \
                "%s but expected %s" % (self.customer_event.addon.text, '$0.00')
        if order.discount is not None:
            assert self.customer_event.gift_certificate.text == "($%s)" % order.discount.lstrip("-"), \
                "%s but expected %s" % (self.customer_event.gift_certificate.text, "($%s)" % order.discount.lstrip("-"))
        assert self.customer_event.booking_fee.text == "$" + order.booking_fee, \
            "%s but expected %s" % (self.customer_event.booking_fee.text, "$" + order.booking_fee)
        assert self.customer_event.tax.text == "$" + order.taxes, \
            "%s but expected %s" % (self.customer_event.tax.text, "$" + order.taxes)
        assert self.customer_event.grand_total.text == "$" + order.grand_total, \
            "%s but expected: %s" % (self.customer_event.grand_total.text, "$" + order.grand_total)
        assert self.customer_event.total_charges.text == "$" + order.grand_total, \
                "%s but expected: %s" % (self.customer_event.total_charges.text, "$" + order.grand_total)
        assert self.customer_event.total_due.text == "0.00", \
            "%s but expected: %s" % (self.customer_event.total_due.text, "0.00")

    def go_to_customer_event_charges(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.amount_due.click()
                break

    def full_refund_cash_100(self, order):
        self.go_to_customer_event_charges(order)
        self.customer_event.select(self.customer_event.amount_options, "Refund 100%")
        self.customer_event.select(self.customer_event.charge_type, "Cash")
        wait(lambda: self.customer_event.cash_received.is_displayed())
        self.customer_event.cash_received.click()
        print(self.customer_event.final_button.text)
        wait(lambda: self.customer_event.final_button.text == "Cash Received, Adjust Booking")
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == "Adjust Booking")
        wait(lambda: len(self.customer_event.status.text) > 0)
        assert self.customer_event.status.text == 'Request Complete: "Refunded"', self.customer_event.status
        sleep(2)
        assert self.customer_event.charge_history_amount.text == "(%s)" % order.grand_total, self.customer_event.charge_history_amount.text
        assert self.customer_event.charge_history_status.text == "Received", self.customer_event.charge_history_status.text

    def full_refund_cash_50(self, order):
        self.go_to_customer_event_charges(order)
        self.customer_event.select(self.customer_event.amount_options, "Refund 50%")
        self.customer_event.select(self.customer_event.charge_type, "Cash")
        wait(lambda: self.customer_event.cash_received.is_displayed())
        self.customer_event.cash_received.click()
        print(self.customer_event.final_button.text)
        wait(lambda: self.customer_event.final_button.text == "Cash Received, Adjust Booking")
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == "Adjust Booking")
        wait(lambda: len(self.customer_event.status.text) > 0)
        assert self.customer_event.status.text == 'Request Complete: "Refunded"', self.customer_event.status.text
        sleep(2)
        amount = float(order.grand_total.lstrip("$")) / 2
        assert self.customer_event.charge_history_amount.text == "(${0:,.2f})".format(amount), self.customer_event.charge_history_amount.text
        assert self.customer_event.charge_history_status.text == "Received", self.customer_event.charge_history_status.text

    # def verify_event_status(self, status):
    #     assert self.event_manifest.event_status.text == status, "%s but expected %s" % \
    #                                                             (self.event_manifest.event_status.text, status)

    def charge_due(self, order, charge, charge_type, cash_received, button_name, button_name_after, status, charge_status):
        self.go_to_customer_event_charges(order)
        self.customer_event.select(self.customer_event.amount_options, charge)
        self.customer_event.select(self.customer_event.charge_type, charge_type)
        if charge_type == "Credit Card":
            self.customer_event.enter_cc_info(card_number="4242424242424242", card_date="1020",
                                              card_cvc="303", card_zip="12345")
        elif charge_type == "Check":
            self.customer_event.check_input.send_keys("123456")
        if cash_received:
            wait(lambda: self.customer_event.cash_received.is_displayed())
            self.customer_event.cash_received.click()
        wait(lambda: self.customer_event.final_button.text == button_name)
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == button_name_after, timeout_seconds=60)
        assert self.customer_event.status.text == status, self.customer_event.status.text
        sleep(2)
        assert self.customer_event.charge_history_amount.text == order.grand_total, self.customer_event.charge_history_amount.text
        assert self.customer_event.charge_history_status.text == charge_status, self.customer_event.charge_history_status.text
        assert self.customer_event.grand_total.text == order.grand_total, \
            "%s but expected: %s" % (self.customer_event.grand_total.text, order.grand_total)
        assert self.customer_event.total_charges.text == order.grand_total, \
            "%s but expected: %s" % (self.customer_event.total_charges.text, order.grand_total)
        assert self.customer_event.total_due.text == "0.00", \
            "%s but expected: %s" % (self.customer_event.total_due.text, "0.00")
        assert self.customer_event.final_button.get_attribute('disabled') == "true", \
            self.customer_event.final_button.get_attribute('disabled')

    def click_add_booking_button(self, order):
        self.event_manifest.add_booking.click()
        wait(lambda: self.event_manifest.activity_cart.text == order.activity)
        sleep(3)

    def show_events_without_booking(self):
        self.calendar_page.without_booking.click()
        sleep(2)

    def cancel_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.cancel_event.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed())
        assert self.event_manifest.pop_up.text == "Are you sure you would like to cancel this event? Once you do, your guests will be automatically notified of the cancellation."
        self.event_manifest.pop_up_ok_button.click()

    def close_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.close_bookings.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed(), timeout_seconds=25)
        assert self.event_manifest.pop_up.text == "Are you sure you would like to close this event? This will disallow any further bookings unless it is re-opened."
        self.event_manifest.pop_up_ok_button.click()

    def re_open_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.re_open_bookings.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed(), timeout_seconds=25)
        assert self.event_manifest.pop_up.text == "Are you sure you would like to re-open this event? This will open up the event to more bookings."
        self.event_manifest.pop_up_ok_button.click()

    def verify_event_status(self, status):
        assert self.event_manifest.event_status.text == status, self.event_manifest.event_status.text
        if status == "Cancelled":
            assert self.event_manifest.add_booking.get_attribute('disabled') == "true", \
                self.event_manifest.add_booking.get_attribute('disabled')
            # assert self.event_manifest.close_bookings.get_attribute('disabled') == "true", \
            #     self.event_manifest.close_bookings.get_attribute('disabled')
            # assert self.event_manifest.cancel_event.get_attribute('disabled') == "true", \
            #     self.event_manifest.cancel_event.get_attribute('disabled')
        elif status == "Closed":
            assert self.event_manifest.add_booking.get_attribute('disabled') == "true", \
                self.event_manifest.add_booking.get_attribute('disabled')
            self.event_manifest.actions_button.click()
            assert self.event_manifest.re_open_bookings.text == "Re-Open Bookings", \
                self.event_manifest.re_open_bookings.text
        elif status == "Pending":
            assert self.event_manifest.add_booking.get_attribute('disabled') == None, \
                self.event_manifest.add_booking.get_attribute('disabled')
            # assert self.event_manifest.close_bookings.text == "Close Bookings", \
            #     self.event_manifest.re_open_bookings.text

    def cancel_guest(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.cancel.click()
                break
        wait(lambda: len(self.event_manifest.pop_up.text) > 0)
        assert self.event_manifest.pop_up.text == "Are you sure you would like to cancel this guest? They will be removed from the event without a refund.", \
            "'%s'" % self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()
        sleep(2)

    def cancel_guest_cancel(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.cancel.click()
                break
        wait(lambda: len(self.event_manifest.pop_up.text) > 0)
        assert self.event_manifest.pop_up.text == "Are you sure you would like to cancel this guest? They will be removed from the event without a refund.", \
            self.event_manifest.pop_up.text
        self.event_manifest.pop_up_cancel_button.click()
        sleep(2)

    def rain_check(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.rain_check.click()
                break
        assert self.event_manifest.pop_up.text == "Are you sure you want to mark this as a Rain Check?", \
            self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()
        sleep(2)

    def rain_check_cancel(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.rain_check.click()
                break
        assert self.event_manifest.pop_up.text == "Are you sure you want to mark this as a Rain Check?", \
            self.event_manifest.pop_up.text
        self.event_manifest.pop_up_cancel_button.click()
        sleep(2)

    def no_such_guest(self, order):
        list_of_guests = []
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            list_of_guests.append(guest.name.text)
        expected_name = order.first_name + " " + order.last_name
        print(list_of_guests)
        assert expected_name not in list_of_guests, "%s in list %s" % (expected_name, list_of_guests)

    def refund_cancel(self, order):
        expected_name = order.first_name + " " + order.last_name
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.refund.click()
                break
        wait(lambda: self.event_manifest.pop_up_refund.text == "%s will be refunded $%s for this event."
            % (expected_name, order.grand_total))
        self.event_manifest.process_refund.click()
        sleep(1)
        assert self.event_manifest.pop_up.text == "You are about to issue $%s to %s to the card ending in 5556. Are you sure you want to proceed?" % \
            (order.grand_total, expected_name), self.event_manifest.pop_up.text
        wait(lambda: self.event_manifest.pop_up_cancel_button.is_displayed())
        self.event_manifest.pop_up_cancel_button.click()
        sleep(1)
        assert self.event_manifest.pop_up.text == "An error occured. Please try again.", self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()
        sleep(2)
