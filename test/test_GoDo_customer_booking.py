import pytest
from data.orders import customer_data, customer_declines, customer_valid_codes, customer_invalid_codes


@pytest.mark.parametrize("tickets", customer_data, ids=[repr(x) for x in customer_data])
def test_customer_booking(customer, tickets):
    """Order tickets via customer facing with valid credit card."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets_buttons(tickets)
    customer.booking.select_date(tickets)
    customer.booking.select_time(tickets)
    customer.booking.fill_info(tickets)
    customer.booking.skip_addons()
    customer.booking.verify_payment_page(tickets)
    customer.booking.make_payment(tickets)
    customer.booking.verify_summary_details(tickets)


@pytest.mark.parametrize("tickets", customer_declines, ids=[repr(x) for x in customer_declines])
def test_customer_declines(customer, tickets):
    """Order tickets via customer facing with invalid credit card number."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets_buttons(tickets)
    customer.booking.select_date(tickets)
    customer.booking.select_time(tickets)
    customer.booking.fill_info(tickets)
    customer.booking.skip_addons()
    customer.booking.verify_payment_page(tickets)
    customer.booking.submit_declined_card(tickets)
    customer.booking.refill_payment_info(tickets)
    customer.booking.verify_summary_details(tickets)


@pytest.mark.parametrize("tickets", customer_valid_codes, ids=[repr(x) for x in customer_valid_codes])
def test_customer_booking_promo_codes(customer, tickets):
    """Order tickets via customer facing with valid promo codes."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets_buttons(tickets)
    customer.booking.select_date(tickets)
    customer.booking.select_time(tickets)
    customer.booking.fill_info(tickets)
    customer.booking.skip_addons()
    customer.booking.apply_valid_promo_code(tickets)
    customer.booking.verify_payment_page(tickets)
    customer.booking.make_payment(tickets)
    customer.booking.verify_summary_details(tickets)


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


@pytest.fixture
def stop():
    """Override admin's finalizer."""
    pass
