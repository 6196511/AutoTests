import pytest
from data.tickets import testdata_cus1, testdata_cus2


@pytest.mark.parametrize("tickets", testdata_cus1[0:16], ids=[repr(x) for x in testdata_cus1[0:16]])
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


@pytest.mark.parametrize("tickets", testdata_cus2, ids=[repr(x) for x in testdata_cus2])
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


@pytest.mark.parametrize("tickets", testdata_cus1[16:26], ids=[repr(x) for x in testdata_cus1[16:26]])
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


@pytest.mark.parametrize("tickets", testdata_cus1[26:], ids=[repr(x) for x in testdata_cus1[26:]])
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
