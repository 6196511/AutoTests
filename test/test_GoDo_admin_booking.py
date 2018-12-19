import pytest

from data.orders import admin_booking_with_certificates, admin_cert_discount, get_ids
from data.orders import admin_data, admin_declines, admin_declines_not_finished, admin_valid_codes, admin_invalid_codes


@pytest.mark.parametrize("tickets", admin_data[:18], ids=get_ids)
def test_admin_booking(app, tickets):
    """Booking tickets via admin."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", admin_declines, ids=get_ids)
def test_admin_booking_declines(app, tickets):
    """Booking tickets via admin with invalid credit card."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.submit_declined_card(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", admin_declines_not_finished, ids=get_ids)
def test_admin_booking_declines_not_finished(app, tickets):
    """Booking tickets via admin with invalid credit card."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.submit_declined_card(tickets)


@pytest.mark.parametrize("tickets", admin_valid_codes, ids=get_ids)
def test_admin_booking_promo_codes(app, tickets):
    """Booking tickets via admin with valid promo codes."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_valid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", admin_invalid_codes, ids=get_ids)
def test_admin_booking_invalid_promo_codes(app, tickets):
    """Booking tickets via admin with invalid promo codes."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_invalid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_booking_with_certificates, ids=get_ids)
def test_admin_booking_with_gift_certificates(app, order):
    """Booking tickets via admin with gift certificates."""
    app.refresh_page()
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
    app.refresh_page()
    app.certificate.navigate_to()
    app.certificate.verify_remain_amount(order)


@pytest.mark.parametrize("order", admin_cert_discount, ids=get_ids)
def test_admin_booking_with_gift_certificate_and_promo_code(app, order):
    """Booking tickets via admin with gift certificates and promo code."""
    app.certificate.select_certificate(order)
    app.certificate.make_successful_payment(order)
    app.certificate.verify_created_certificate(order)
    app.certificate.copy_the_code(order)
    app.booking.select_event(order)
    app.booking.apply_valid_promo_code(order)
    app.booking.apply_valid_gift_cert(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.refresh_page()
    app.certificate.navigate_to()
    app.certificate.verify_remain_amount(order)


@pytest.mark.parametrize("tickets", admin_data[18:20], ids=get_ids)
def test_admin_booking_customer_price(app, tickets):
    """Booking tickets via admin with custom price."""
    app.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_custom_price(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_data[22:23], ids=get_ids)
def test_361_private_party(app, order):
    """Booking tickets for Private Party."""
    app.refresh_page()
    app.booking.select_event(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_event_status(status="Pending")


data = admin_data[:18] + admin_declines + admin_valid_codes[0:8] + admin_invalid_codes[0:5] + \
       admin_invalid_codes[7:] + admin_booking_with_certificates + admin_cert_discount + admin_data[18:20] + \
       admin_data[22:23]


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_admin(order)
