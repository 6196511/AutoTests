import pytest

from data.orders import center_data, center_declines, center_valid_codes, center_invalid_codes
from data.orders import center_booking_with_certificates
from data.orders import get_ids


@pytest.mark.parametrize("tickets", center_data, ids=get_ids)
def test_call_center_booking(call_center, tickets):
    """Booking tickets via call center."""
    call_center.refresh_page()
    call_center.booking.select_event(tickets)
    call_center.booking.fill_out_customer_info(tickets)
    call_center.booking.select_payment_method(tickets)
    call_center.booking.verify_payment_table(tickets)
    call_center.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", center_declines, ids=get_ids)
def test_call_center_booking_declines(call_center, tickets):
    """Booking tickets via call center with invalid credit card."""
    call_center.refresh_page()
    call_center.booking.select_event(tickets)
    call_center.booking.fill_out_customer_info(tickets)
    call_center.booking.submit_declined_card(tickets)
    call_center.booking.select_payment_method(tickets)
    call_center.booking.verify_payment_table(tickets)
    call_center.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", center_valid_codes, ids=get_ids)
def test_center_booking_promo_codes(call_center, tickets):
    """Booking tickets via call center with valid promo codes."""
    call_center.refresh_page()
    call_center.booking.select_event(tickets)
    call_center.booking.apply_valid_promo_code(tickets)
    call_center.booking.fill_out_customer_info(tickets)
    call_center.booking.select_payment_method(tickets)
    call_center.booking.verify_payment_table(tickets)
    call_center.booking.submit_successful_booking()


@pytest.mark.parametrize("tickets", center_invalid_codes, ids=get_ids)
def test_center_booking_invalid_promo_codes(call_center, tickets):
    """Booking tickets via call center with invalid promo codes."""
    call_center.refresh_page()
    call_center.booking.select_event(tickets)
    call_center.booking.apply_invalid_promo_code(tickets)
    call_center.booking.fill_out_customer_info(tickets)
    call_center.booking.select_payment_method(tickets)
    call_center.booking.verify_payment_table(tickets)
    call_center.booking.submit_successful_booking()


@pytest.mark.parametrize("order", center_booking_with_certificates, ids=get_ids)
def test_center_booking_with_gift_certificates(call_center, order):
    """Booking tickets via call center with gift certificates."""
    call_center.certificate.select_certificate(order)
    call_center.certificate.make_successful_payment(order)
    call_center.certificate.verify_created_certificate(order)
    call_center.certificate.copy_the_code(order)
    call_center.booking.select_event(order)
    call_center.booking.apply_valid_gift_cert(order)
    call_center.booking.fill_out_customer_info(order)
    call_center.booking.select_payment_method(order)
    call_center.booking.verify_payment_table(order)
    call_center.booking.submit_successful_booking()
    call_center.refresh_page()
    call_center.certificate.navigate_to()
    call_center.certificate.verify_remain_amount(order)


data = center_data + center_declines + center_valid_codes[:8] + center_invalid_codes[:5] + center_invalid_codes[7:8] +\
       center_booking_with_certificates


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(call_center, order):
    """Checking booked tickets in the event manifest and customer event page."""
    call_center.calendar.select_event(order)
    call_center.calendar.verify_event_manifest(order)
    call_center.calendar.verify_customer_event_admin(order)
