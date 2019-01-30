from calendar import month_name
from time import sleep

from webium.wait import wait

from pages.calendar import CalendarPage, EventManifest, CustomerEventPage
from pages.navigation_bar import NavigationBar


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
        self.app.waiting.for_page_loaded()

    def pick_event(self, order):
        wait(lambda: len(self.calendar_page.days_list) == 28)
        month = month_name[int(order.month)]
        our_date = "{} {}".format(month[:3], order.day)
        for day in self.calendar_page.days_list:
            if day.date.text == our_date:
                if day.is_element_present('view_all'):
                    day.view_all.click()
                    wait(lambda: len(day.events_list) > 5)
                for event in day.events_list:
                    if event.activity_name.text == order.activity and event.time.text.startswith(order.time.lstrip("0")):
                        event.activity_name.click()
                        break
                break

    def select_event(self, order):
        if not self.event_manifest.is_element_present('event_title'):
            self.navigate_to()
            self.pick_event(order)
        elif self.event_manifest.event_title.text != order.activity or \
                self.event_manifest.event_date.text.find(order.time.lstrip("0")) == -1:
            self.event_manifest.close_button.click()
            self.pick_event(order)

    def verify_event_manifest(self, order):
        count = 0
        expected_name = order.first_name + " " + order.last_name
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                count += 1
                self.verify_amount_due(guest, order)
                assert order.email == guest.email.text
                self.verify_tickets(guest, order)
        assert 1 == count, "Wrong amount of guests in the Event manifest."

    def verify_tickets(self, guest, order):
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for ticket in guest.tickets:
            tickets.append(ticket.text)
        assert sorted(expected_tickets) == sorted(tickets), "Wrong list of tickets in the Event manifest."

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
            assert "Total Paid: $0.00 Total Due: ${:.2f}".format(grand_total) == guest.amount_due.text
        else:
            assert "Paid in Full : ${:.2f}".format(grand_total) == guest.amount_due.text

    def verify_customer_event_admin(self, order):
        self.go_to_customer_event_charges(order)
        assert order.first_name + " " + order.last_name == self.customer_event.name.text
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("{} x {}".format(row.quantity.text, row.type.text))
        assert sorted(expected_tickets) == sorted(tickets)
        assert order.ticket_total == self.customer_event.ticket_total.text
        if order.addon is not None:
            assert order.addon == self.customer_event.addon.text
        else:
            assert '$0.00' == self.customer_event.addon.text
        if order.discount != "- $0.00":
            assert "({})".format(order.discount.lstrip("- ")) == self.customer_event.discount.text
        if order.gift_certificate != "- $0.00":
            assert "({})".format(order.gift_certificate.lstrip("- ")) == self.customer_event.gift_certificate.text
        assert order.booking_fee == self.customer_event.booking_fee.text
        assert order.taxes == self.customer_event.tax.text
        assert order.grand_total == self.customer_event.grand_total.text
        if order.payment_type != "Cash" or order.cash_recieved is not None:
            assert order.grand_total == self.customer_event.total_charges.text
        else:
            assert "$0.00" == self.customer_event.total_charges.text
        if order.payment_type != "Cash" or order.cash_recieved is not None:
            assert "$0.00" == self.customer_event.total_due.text
        else:
            assert order.grand_total == self.customer_event.total_due.text

    def verify_customer_event_customer(self, order):
        self.go_to_customer_event_charges(order)
        assert order.first_name + " " + order.last_name == self.customer_event.name.text
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("{} x {}".format(row.quantity.text, row.type.text))
        assert sorted(expected_tickets) == sorted(tickets)
        assert "$" + order.ticket_total == self.customer_event.ticket_total.text
        if order.addon is not None:
            assert "$" + order.addon == self.customer_event.addon.text
        else:
            assert '$0.00' == self.customer_event.addon.text
        if order.discount != "0.00":
            assert "(${})".format(order.discount.lstrip("-")) == self.customer_event.discount.text
        if order.gift_certificate is not None:
            assert "(${})".format(order.gift_certificate.lstrip("-")) == self.customer_event.gift_certificate.text
        assert "$" + order.booking_fee == self.customer_event.booking_fee.text
        assert "$" + order.taxes == self.customer_event.tax.text
        assert "$" + order.grand_total == self.customer_event.grand_total.text
        assert "$" + order.grand_total == self.customer_event.total_charges.text
        assert "$0.00" == self.customer_event.total_due.text

    def verify_customer_event_customer_cert(self, order):
        self.go_to_customer_event_charges(order)
        assert self.customer_event.name.text == order.first_name + " " + order.last_name
        expected_tickets = self.get_expected_tickets(order)
        tickets = []
        for row in self.customer_event.tickets_table:
            tickets.append("{} x {}".format(row.quantity.text, row.type.text))
        assert sorted(expected_tickets) == sorted(tickets)
        assert "$" + order.ticket_total == self.customer_event.ticket_total.text
        if order.addon is not None:
            assert "$" + order.addon == self.customer_event.addon.text
        else:
            assert '$0.00' == self.customer_event.addon.text
        if order.discount is not None:
            assert "(${})".format(order.discount.lstrip("-")) == self.customer_event.gift_certificate.text
        assert "$" + order.booking_fee == self.customer_event.booking_fee.text
        assert "$" + order.taxes == self.customer_event.tax.text
        assert "$" + order.grand_total == self.customer_event.grand_total.text
        assert "$" + order.grand_total == self.customer_event.total_charges.text
        assert "$0.00" == self.customer_event.total_due.text

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
        wait(lambda: self.customer_event.final_button.text == "Cash Received, Adjust Booking")
        charge_history = self.customer_event.charge_history_amount
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == "Adjust Booking")
        self.app.waiting.for_staleness(element=charge_history, timeout=15)
        assert 'Request Complete: "Refunded"' == self.customer_event.status.text
        assert "({})".format(order.grand_total) == self.customer_event.charge_history_amount.text
        assert "Received" == self.customer_event.charge_history_status.text

    def full_refund_cash_50(self, order):
        self.go_to_customer_event_charges(order)
        self.customer_event.select(self.customer_event.amount_options, "Refund 50%")
        self.customer_event.select(self.customer_event.charge_type, "Cash")
        wait(lambda: self.customer_event.cash_received.is_displayed())
        self.customer_event.cash_received.click()
        wait(lambda: self.customer_event.final_button.text == "Cash Received, Adjust Booking")
        charge_history = self.customer_event.charge_history_amount
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == "Adjust Booking")
        assert 'Request Complete: "Booked"' == self.customer_event.status.text
        self.app.waiting.for_staleness(element=charge_history, timeout=15)
        amount = float(order.grand_total.lstrip("$")) / 2
        assert "(${0:,.2f})".format(amount) == self.customer_event.charge_history_amount.text
        assert "Received" == self.customer_event.charge_history_status.text

    def charge_due(self, order, charge, charge_type, cash_received, button_name, button_name_after, status,
                   charge_status):
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
        charge_history = self.customer_event.charge_history_amount
        self.customer_event.final_button.click()
        wait(lambda: self.customer_event.final_button.text == button_name_after, timeout_seconds=60)
        assert status == self.customer_event.status.text
        self.app.waiting.for_staleness(element=charge_history, timeout=15)
        assert order.grand_total == self.customer_event.charge_history_amount.text
        assert charge_status == self.customer_event.charge_history_status.text
        assert order.grand_total == self.customer_event.grand_total.text
        assert order.grand_total == self.customer_event.total_charges.text
        assert "$0.00" == self.customer_event.total_due.text
        assert "true" == self.customer_event.final_button.get_attribute('disabled')

    def click_add_booking_button(self):
        self.event_manifest.add_booking.click()
        self.app.waiting.for_invisibility(self.event_manifest.add_booking)

    def show_events_without_booking(self):
        self.calendar_page.without_booking.click()
        wait(lambda: len(self.calendar_page.view_all_links) == 28, timeout_seconds=120)

    def cancel_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.cancel_event.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed())
        expected_notification = "Are you sure you would like to cancel this event? Once you do, your guests will be " \
                                "automatically notified of the cancellation."
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()

    def close_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.close_bookings.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed(), timeout_seconds=25)
        expected_notification = "Are you sure you would like to close this event? This will disallow any further " \
                                "bookings unless it is re-opened."
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()

    def re_open_event(self):
        self.event_manifest.actions_button.click()
        self.event_manifest.re_open_bookings.click()
        wait(lambda: self.event_manifest.pop_up.is_displayed(), timeout_seconds=25)
        expected_notification = "Are you sure you would like to re-open this event? This will open up the event to " \
                                "more bookings."
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()

    def verify_event_status(self, status):
        assert self.event_manifest.event_status.text == status, self.event_manifest.event_status.text
        if status == "Cancelled":
            assert "true" == self.event_manifest.add_booking.get_attribute('disabled')
        elif status == "Closed":
            assert "true" == self.event_manifest.add_booking.get_attribute('disabled')
            self.event_manifest.actions_button.click()
            assert "Re-Open Bookings" == self.event_manifest.re_open_bookings.text
        elif status == "Pending":
            assert None == self.event_manifest.add_booking.get_attribute('disabled')

    def cancel_guest(self, order):
        expected_name = order.first_name + " " + order.last_name
        initial_guests_list = self.event_manifest.guests_list
        for guest in initial_guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.cancel.click()
                break
        wait(lambda: len(self.event_manifest.pop_up.text) > 0)
        expected_notification = "Are you sure you would like to cancel this guest? They will be removed from " \
                                "the event without a refund."
        assert expected_notification == self.event_manifest.pop_up.text
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
        expected_notification = "Are you sure you would like to cancel this guest? They will be removed from " \
                                "the event without a refund."
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_cancel_button.click()
        sleep(2)

    def rain_check(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.rain_check.click()
                break
        expected_notification = "Are you sure you want to mark this as a Rain Check?"
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()
        sleep(2)

    def rain_check_cancel(self, order):
        expected_name = order.first_name + " " + order.last_name
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.rain_check.click()
                break
        expected_notification = "Are you sure you want to mark this as a Rain Check?"
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_cancel_button.click()
        sleep(2)

    def no_such_guest(self, order):
        list_of_guests = []
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            list_of_guests.append(guest.name.text)
        expected_name = order.first_name + " " + order.last_name
        assert expected_name not in list_of_guests

    def no_current_bookings(self):
        assert "There are no current bookings." == self.event_manifest.no_bookings.text

    def refund_cancel(self, order):
        expected_name = order.first_name + " " + order.last_name
        wait(lambda: len(self.event_manifest.guests_list) > 0)
        for guest in self.event_manifest.guests_list:
            if guest.name.text == expected_name:
                guest.actions.click()
                guest.refund.click()
                break
        wait(lambda: self.event_manifest.pop_up_refund.text == "{} will be refunded $%s for this event.".format(
            expected_name, order.grand_total))
        self.event_manifest.process_refund.click()
        sleep(1)
        expected_notification = "You are about to issue $%s to %s to the card ending in 5556. Are you sure you " \
                                "want to proceed?".format(order.grand_total, expected_name)
        assert expected_notification == self.event_manifest.pop_up.text
        wait(lambda: self.event_manifest.pop_up_cancel_button.is_displayed())
        self.event_manifest.pop_up_cancel_button.click()
        sleep(1)
        expected_notification = "An error occured. Please try again."
        assert expected_notification == self.event_manifest.pop_up.text
        self.event_manifest.pop_up_ok_button.click()
        sleep(2)
