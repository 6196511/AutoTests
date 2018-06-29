import pytest
from data.orders import *


@pytest.mark.parametrize("order", customer_booking_with_certificates[:6], ids=[repr(x) for x in customer_booking_with_certificates[:6]])
def test_customer_booking_with_certs(customer, order):
    """Order tickets via customer facing with gift certificate."""
    customer.certificate.open_page(order)
    customer.certificate.fill_first_form(order)
    customer.certificate.verify_payment_info(order)
    customer.certificate.make_successful_payment(order)
    customer.certificate.verify_summary_details(order)
    customer.certificate.copy_the_code(order)
    customer.booking.open_page(order)
    customer.booking.select_tickets_buttons(order)
    customer.booking.select_date(order)
    customer.booking.select_time(order)
    customer.booking.fill_info(order)
    customer.booking.skip_addons()
    customer.booking.redeem_gift_certificate(order)
    customer.booking.verify_payment_page(order)
    customer.booking.make_payment(order)
    customer.booking.verify_summary_details(order)


@pytest.mark.parametrize("order", customer_cert_discount[:8], ids=[repr(x) for x in customer_cert_discount[:8]])
def test_customer_booking_with_discount_and_cert(customer, order):
    """Order tickets via customer facing with discount and gift certificate."""

    # Discount is removed when gift certificate is applied.
    # All tests failed.
    # Bug 2019 Customer facing. Gift certificate + discount. Total amount is calculated incorrectly
    # Bug 2372 Errors on summary details page.

    customer.certificate.open_page(order)
    customer.certificate.fill_first_form(order)
    customer.certificate.verify_payment_info(order)
    customer.certificate.make_successful_payment(order)
    customer.certificate.verify_summary_details(order)
    customer.certificate.copy_the_code(order)
    customer.booking.open_page(order)
    customer.booking.select_tickets_buttons(order)
    customer.booking.select_date(order)
    customer.booking.select_time(order)
    customer.booking.fill_info(order)
    customer.booking.skip_addons()
    customer.booking.apply_valid_promo_code(order)
    customer.booking.redeem_gift_certificate(order)
    customer.booking.verify_payment_page(order)
    customer.booking.make_payment(order)
    customer.booking.verify_summary_details(order)


@pytest.mark.parametrize("order", customer_cert_discount[8:], ids=[repr(x) for x in customer_cert_discount[8:]])
def test_customer_booking_with_cert_and_discount(customer, order):
    """Order tickets via customer facing with gift certificate and discount."""

    # Discount is removed when gift certificate is applied.
    # All tests failed.
    # Bug 2019 Customer facing. Gift certificate + discount. Total amount is calculated incorrectly
    # Bug 2372 Errors on summary details page.

    customer.certificate.open_page(order)
    customer.certificate.fill_first_form(order)
    customer.certificate.verify_payment_info(order)
    customer.certificate.make_successful_payment(order)
    customer.certificate.verify_summary_details(order)
    customer.certificate.copy_the_code(order)
    customer.booking.open_page(order)
    customer.booking.select_tickets_buttons(order)
    customer.booking.select_date(order)
    customer.booking.select_time(order)
    customer.booking.fill_info(order)
    customer.booking.skip_addons()
    customer.booking.redeem_gift_certificate(order)
    customer.booking.apply_valid_promo_code(order)
    customer.booking.verify_payment_page(order)
    customer.booking.make_payment(order)
    customer.booking.verify_summary_details(order)



@pytest.mark.parametrize("order", customer_booking_with_certificates[6:], ids=[repr(x) for x in customer_booking_with_certificates[6:]])
def test_customer_booking_with_invalid_certs(customer, order):
    """Order tickets via customer facing with invalid gift certificate."""
    customer.certificate.open_page(order)
    customer.certificate.fill_first_form(order)
    customer.certificate.verify_payment_info(order)
    customer.certificate.make_successful_payment(order)
    customer.certificate.verify_summary_details(order)
    customer.certificate.copy_the_code(order)
    customer.booking.open_page(order)
    customer.booking.select_tickets_buttons(order)
    customer.booking.select_date(order)
    customer.booking.select_time(order)
    customer.booking.fill_info(order)
    customer.booking.skip_addons()
    customer.booking.redeem_invalid_gift_certificate(order)
    customer.booking.verify_payment_page(order)


@pytest.mark.parametrize("order", customer_booking_with_certificates[8:9], ids=[repr(x) for x in customer_booking_with_certificates[8:9]])
def test_customer_booking_with_unexisting_cert(customer, order):
    """Order tickets via customer facing with unexisting gift certificate."""
    customer.booking.open_page(order)
    customer.booking.select_tickets_buttons(order)
    customer.booking.select_date(order)
    customer.booking.select_time(order)
    customer.booking.fill_info(order)
    customer.booking.skip_addons()
    customer.booking.redeem_invalid_gift_certificate(order)
    customer.booking.verify_payment_page(order)


@pytest.fixture
def stop():
    """Override admin's finalizer."""
    pass
