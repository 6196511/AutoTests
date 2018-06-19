import pytest
from data.orders import admin_data, admin_declines, admin_valid_codes, admin_invalid_codes, admin_booking_with_certificates


@pytest.mark.parametrize("tickets", admin_data, ids=[repr(x) for x in admin_data])
def test_admin_booking(app, tickets):
    """Booking tickets via admin."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", admin_declines, ids=[repr(x) for x in admin_declines])
def test_admin_booking_declines(app, tickets):
    """Booking tickets via admin with invalid credit card."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.submit_declined_card(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", admin_valid_codes, ids=[repr(x) for x in admin_valid_codes])
def test_admin_booking_promo_codes(app, tickets):
    """Booking tickets via admin with valid promo codes."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_valid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.skip  # Due to the bug 2550
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


@pytest.mark.parametrize("order", admin_booking_with_certificates, ids=[repr(x) for x in admin_booking_with_certificates])
def test_admin_booking_with_gift_certificates(app, order):
    """Booking tickets via admin with gift certificates. Grand total = 0."""
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
