from time import sleep
import pytest
from data.live_smoke import *
from data.guides import guides


@pytest.mark.parametrize("certificate", admin_certificates[:4], ids=[repr(x) for x in admin_certificates[:4]])
def test_purchasing_certificate(app, certificate):
    """Selling certificates via admin."""
    app.certificate.select_certificate(certificate)
    app.certificate.make_successful_payment(certificate)
    app.certificate.verify_created_certificate(certificate)


@pytest.mark.parametrize("order", admin_booking_with_certificates, ids=[repr(x) for x in admin_booking_with_certificates])
def test_admin_booking_with_gift_certificates(app, order):
    """Booking tickets via admin with gift certificates."""
    app.certificate.select_certificate(order)
    app.certificate.make_successful_payment(order)
    app.certificate.verify_created_certificate(order)
    app.certificate.copy_the_code(order)
    app.booking.select_event(order)
    app.booking.apply_valid_gift_cert(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.booking.refresh_page()
    app.certificate.navigate_to()
    app.certificate.verify_remain_amount(order)
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_admin(order)


@pytest.mark.parametrize("order", customer_booking_with_certificates[8:9], ids=[repr(x) for x in customer_booking_with_certificates[8:9]])
def test_customer_booking_with_unexisting_cert(app, order):
    """Order tickets via customer facing with unexisting gift certificate."""

    # GoDo-53 - Bug 2674 Customer-facing. 500 error after entering an invalid gift certificate code.

    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.redeem_invalid_gift_certificate(order)
    app.customer_booking.verify_payment_page(order)
    app.session.login_as_admin()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)

@pytest.mark.parametrize("order", customer_booking_with_certificates[3:4], ids=[repr(x) for x in customer_booking_with_certificates[3:4]])
def test_customer_booking_with_certs(app, order):
    """Order tickets via customer facing with gift certificate."""
    app.booking.refresh_page()
    app.certificate.select_certificate(order)
    app.certificate.make_successful_payment(order)
    app.certificate.verify_created_certificate(order)
    app.certificate.copy_the_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.redeem_gift_certificate(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)
    app.session.login_as_admin()
    app.certificate.navigate_to()
    app.certificate.find_by_code(order)
    app.certificate.verify_remain_amount(order)
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)  # Issue with discount.


def test_admin_booking(call_center):
    """Booking tickets via call-center."""


@pytest.mark.parametrize("tickets", customer_invalid_codes, ids=[repr(x) for x in customer_invalid_codes])
def test_customer_booking_invalid_promo_codes(customer, tickets):
    """Order tickets via customer facing with invalid promo codes."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets_buttons(tickets)
    customer.booking.select_date(tickets)
    customer.booking.select_time(tickets)
    customer.booking.fill_info(tickets)
    customer.booking.skip_addons()
    customer.booking.verify_payment_page(tickets)
    customer.booking.apply_invalid_promo_code(tickets)
    customer.booking.verify_payment_page(tickets)


@pytest.mark.parametrize("guides", guides[0:1], ids=[repr(x) for x in guides[0:1]])
def test_add_and_delete_guide(app, guides):
    """Add guide and delete. Only required fields."""
    app.people_hub.add_guide(guides)
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.verify_guides_details(guides)
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.delete_guide(guides)


@pytest.mark.parametrize("tickets", admin_invalid_codes, ids=[repr(x) for x in admin_invalid_codes])
def test_admin_booking_invalid_promo_codes(app, tickets):
    """Booking tickets via admin with invalid promo codes."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_invalid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()
    app.calendar.select_event(tickets)
    app.calendar.verify_event_manifest(tickets)
    app.calendar.verify_customer_event_admin(tickets)  # 304 and 307 event in december


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
    app.refresh_page()
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
    app.calendar.no_current_bookings()


@pytest.mark.parametrize("order", admin_groupons[10:11], ids=[repr(x) for x in admin_groupons[10:11]])
def test_admin_booking_with_invalid_groupons(app, order):
    """Booking tickets via admin with invalid groupon."""
    app.booking.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_event(order)
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", customer_groupons[4:5], ids=[repr(x) for x in customer_groupons[4:5]])
def test_customer_booking_with_groupons(app, order):
    """Booking tickets via customer with groupon."""
    app.booking.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.apply_valid_promo_code(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)


