from time import sleep

import pytest
from data.orders import admin_data, customer_data


@pytest.mark.parametrize("order", admin_data[20:21], ids=[repr(x) for x in admin_data[20:21]])
def test_full_refund_cash_100(app, order):
    """Full refund (Cash) 100%."""
    app.booking.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.full_refund_cash_100(order)


@pytest.mark.parametrize("order", admin_data[21:22], ids=[repr(x) for x in admin_data[21:22]])
def test_full_refund_cash_50_190(app, order):
    """Full refund (Cash) 50%."""
    app.booking.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.full_refund_cash_50(order)


@pytest.mark.parametrize("order", admin_data[23:24], ids=[repr(x) for x in admin_data[23:24]])
def test_406(app, order):
    """Charge customer's due (cash)."""
    app.booking.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.charge_due(order, charge="Charge Full Due", charge_type="Cash", cash_received=True,
                            button_name="Cash Received, Adjust Booking", button_name_after="Booking Complete",
                            status='Request Complete: "Booked"', charge_status="Received")


@pytest.mark.parametrize("order", admin_data[24:25], ids=[repr(x) for x in admin_data[24:25]])
def test_450(app, order):
    """Charge customer's due (credit card)."""
    app.booking.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.charge_due(order, charge="Charge Full Due", charge_type="Credit Card", cash_received=False,
                            button_name="Credit Card Pending, Adjust Booking", button_name_after="Booking Complete",
                            status='Request Complete: "CHARGED"', charge_status="Charged")


@pytest.mark.parametrize("order", admin_data[25:26], ids=[repr(x) for x in admin_data[25:26]])
def test_451(app, order):
    """Charge customer's due (check)."""
    app.booking.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.charge_due(order, charge="Charge Full Due", charge_type="Check", cash_received=False,
                            button_name="Accept Check, Adjust Booking", button_name_after="Booking Complete",
                            status='Request Complete: "Booked"', charge_status="Received, Not Cleared")


@pytest.mark.parametrize("order", admin_data[26:27], ids=[repr(x) for x in admin_data[26:27]])
def test_421(app, order):
    """Event Pop-Up - Add booking."""

    # At least 1 guest should be booked on the event before start the test.

    app.booking.refresh_page()
    app.calendar.select_event(order)
    app.calendar.click_add_booking_button(order)
    app.booking.select_tickets(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_admin(order)


@pytest.mark.parametrize("order", admin_data[27:29], ids=[repr(x) for x in admin_data[27:29]])
def test_cancel_event(app, order):
    """Event Pop-Up - Cancel Event without/with booking."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.cancel_event()
    app.calendar.verify_event_status(status="Cancelled")


@pytest.mark.parametrize("order", customer_data[16:17], ids=[repr(x) for x in customer_data[16:17]])
def test_413(app, order):
    """Cancelled event should not be allowed for booking (customer-facing)."""
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.time_is_unavailable(time="08:40 PM - 09:40 PM")


@pytest.mark.parametrize("order", admin_data[28:29], ids=[repr(x) for x in admin_data[28:29]])
def test_414(app, order):
    """Cancelled event should not be allowed for booking (admin)."""
    app.booking.refresh_page()
    app.booking.select_activity_and_day(order)
    app.booking.verify_time_list(time="10:00 AM CT")


@pytest.mark.parametrize("order", admin_data[29:31], ids=[repr(x) for x in admin_data[29:31]])
def test_close_event(app, order):
    """Event Pop-Up - Close bookings for Event without/with booking."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.close_event()
    app.calendar.verify_event_status(status="Closed")


@pytest.mark.parametrize("order", customer_data[17:18], ids=[repr(x) for x in customer_data[17:18]])
def test_417(app, order):
    """Closed event should not be allowed for booking (customer-facing)."""
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.time_is_unavailable(time="10:00 AM - 12:30 PM")


@pytest.mark.parametrize("order", admin_data[30:31], ids=[repr(x) for x in admin_data[30:31]])
def test_419(app, order):
    """Event Pop-Up - Re-Open closed booking."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.re_open_event()
    app.calendar.verify_event_status(status="Pending")


@pytest.mark.parametrize("order", admin_data[31:32], ids=[repr(x) for x in admin_data[31:32]])
def test_428(app, order):
    """Event Pop-Up - Cancel guest."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.click_add_booking_button(order)
    app.booking.select_tickets(order)
    app.booking.wait_pricing_table_updating()
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.cancel_guest(order)
    app.calendar.no_such_guest(order)


@pytest.mark.parametrize("order", admin_data[32:33], ids=[repr(x) for x in admin_data[32:33]])
def test_434(app, order):
    """Event Pop-Up - Rain check."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.click_add_booking_button(order)
    app.booking.select_tickets(order)
    app.booking.wait_pricing_table_updating()
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.rain_check(order)
    app.calendar.no_such_guest(order)
    app.rain_checks.verify_table(order)


@pytest.mark.parametrize("order", admin_data[33:34], ids=[repr(x) for x in admin_data[33:34]])
def test_468(app, order):
    """Event Pop-Up - Rain check. Cancel button check."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.click_add_booking_button(order)
    app.booking.select_tickets(order)
    app.booking.wait_pricing_table_updating()
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.rain_check_cancel(order)
    app.calendar.verify_event_manifest(order)


@pytest.mark.parametrize("order", admin_data[34:35], ids=[repr(x) for x in admin_data[34:35]])
def test_470(app, order):
    """Event Pop-Up - Cancel guest. Cancel button check."""
    app.booking.refresh_page()
    app.calendar.navigate_to()
    app.calendar.show_events_without_booking()
    app.calendar.pick_event(order)
    app.calendar.click_add_booking_button(order)
    app.booking.select_tickets(order)
    app.booking.wait_pricing_table_updating()
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.cancel_guest_cancel(order)
    app.calendar.verify_event_manifest(order)


@pytest.mark.parametrize("order", customer_data[18:19], ids=[repr(x) for x in customer_data[18:19]])
def test_500(app, order):
    """Stop booking after first sale via customer facing."""
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)
    app.session.go_to_admin()
    app.calendar.select_event(order)
    app.calendar.verify_event_status(status="Closed")
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.time_is_unavailable(time="10:40 AM - 11:25 AM")


@pytest.mark.parametrize("order", customer_data[19:20], ids=[repr(x) for x in customer_data[19:20]])
def test_453(app, order):
    """Event Pop-Up - Refund. Cancel button check."""
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)
    app.session.go_to_admin()
    app.calendar.select_event(order)
    app.calendar.refund_cancel(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)
