import pytest

from data.orders import customer_booking_with_certificates, customer_cert_discount, get_ids


@pytest.mark.parametrize("order", customer_booking_with_certificates[:6], ids=get_ids)
def test_customer_booking_with_certs(app, order):
    """Order tickets via customer facing with gift certificate."""
    app.customer_certs.open_page(order)
    app.customer_certs.fill_first_form(order)
    app.customer_certs.verify_payment_info(order)
    app.customer_certs.make_successful_payment(order)
    app.customer_certs.verify_summary_details(order)
    app.customer_certs.copy_the_code(order)
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


@pytest.mark.xfail(reason="Bug 2019, 2372. Discount is removed when gift certificate is applied.")
@pytest.mark.parametrize("order", customer_cert_discount[:8], ids=get_ids)
def test_customer_booking_with_discount_and_cert(app, order):
    """Order tickets via customer facing with discount and gift certificate."""
    app.customer_certs.open_page(order)
    app.customer_certs.fill_first_form(order)
    app.customer_certs.verify_payment_info(order)
    app.customer_certs.make_successful_payment(order)
    app.customer_certs.verify_summary_details(order)
    app.customer_certs.copy_the_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.apply_valid_promo_code(order)
    app.customer_booking.redeem_gift_certificate(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)
    app.session.login_as_admin()
    app.certificate.navigate_to()
    app.certificate.find_by_code(order)
    app.certificate.verify_remain_amount(order)


@pytest.mark.xfail(reason="Bug 2019, 2372. Discount is removed when gift certificate is applied.")
@pytest.mark.parametrize("order", customer_cert_discount[8:], ids=get_ids)
def test_customer_booking_with_cert_and_discount(app, order):
    """Order tickets via customer facing with gift certificate and discount."""
    app.customer_certs.open_page(order)
    app.customer_certs.fill_first_form(order)
    app.customer_certs.verify_payment_info(order)
    app.customer_certs.make_successful_payment(order)
    app.customer_certs.verify_summary_details(order)
    app.customer_certs.copy_the_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.redeem_gift_certificate(order)
    app.customer_booking.apply_valid_promo_code(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)
    app.session.login_as_admin()
    app.certificate.navigate_to()
    app.certificate.find_by_code(order)
    app.certificate.verify_remain_amount(order)


@pytest.mark.xfail(reason="GoDo-323 Bug 2675 Customer-facing. Wrong notification upon redeeming gift certificate "
                          "with tickets invalid for chosen tickets.")
@pytest.mark.parametrize("order", customer_booking_with_certificates[6:8], ids=get_ids)
def test_customer_booking_with_invalid_certs(app, order):
    """Order tickets via customer facing with invalid gift certificate."""
    app.customer_certs.open_page(order)
    app.customer_certs.fill_first_form(order)
    app.customer_certs.verify_payment_info(order)
    app.customer_certs.make_successful_payment(order)
    app.customer_certs.verify_summary_details(order)
    app.customer_certs.copy_the_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.redeem_invalid_gift_certificate(order)
    app.customer_booking.verify_payment_page(order)


@pytest.mark.xfail(reason="GoDo-53 - Bug 2674 Customer-facing. 500 error after entering an invalid gift certificate "
                          "code.")
@pytest.mark.parametrize("order", customer_booking_with_certificates[8:9], ids=get_ids)
def test_customer_booking_with_unexisting_cert(app, order):
    """Order tickets via customer facing with unexisting gift certificate."""
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.redeem_invalid_gift_certificate(order)
    app.customer_booking.verify_payment_page(order)


data = customer_booking_with_certificates[:6]


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer_cert(order)


@pytest.fixture
def stop():
    """Override admin's finalizer."""
    pass
