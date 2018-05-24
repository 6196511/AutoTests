import pytest
from data.tickets import testdata1, testdata2


@pytest.mark.parametrize("tickets", testdata1[0:18], ids=[repr(x) for x in testdata1[0:18]])
def test_admin_booking(app, tickets):
    """Booking tickets via admin."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", testdata2, ids=[repr(x) for x in testdata2])
def test_admin_booking_declines(app, tickets):
    """Booking tickets via admin."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.submit_declined_card(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", testdata1[18:28], ids=[repr(x) for x in testdata1[18:28]])
def test_admin_booking_promo_codes(app, tickets):
    """Booking tickets via admin with valid promo codes."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_valid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", testdata1[28:], ids=[repr(x) for x in testdata1[28:]])
def test_admin_booking_invalid_promo_codes(app, tickets):
    """Booking tickets via admin with invalid promo codes."""
    app.booking.refresh_page()
    app.booking.select_event(tickets)
    app.booking.apply_invalid_promo_code(tickets)
    app.booking.fill_out_customer_info(tickets)
    app.booking.select_payment_method(tickets)
    app.booking.verify_payment_table(tickets)
    app.booking.submit_successful_booking()
