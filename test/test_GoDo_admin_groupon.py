import pytest
from data.orders import admin_groupons, get_ids


@pytest.mark.parametrize("order", admin_groupons[:10], ids=get_ids)
def test_admin_booking_with_groupons(app, order):
    """Booking tickets via admin with groupon."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_event(order)
    app.booking.apply_valid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[10:17], ids=get_ids)
def test_admin_booking_with_invalid_groupons(app, order):
    """Booking tickets via admin with invalid groupon."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_event(order)
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[17:18], ids=get_ids)
def test_admin_booking_with_nonexistent_groupon(app, order):
    """Booking tickets via admin with nonexistent groupon."""
    app.refresh_page()
    app.booking.select_event(order)
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[18:19], ids=get_ids)
def test_admin_booking_for_today_with_valid_groupons(app, order):
    """Groupon. Admin booking. "Days Booked In Advance" is set to 0 (= up to time of event - time is met)."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_today_event(order)
    app.booking.apply_valid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[19:20], ids=get_ids)
def test_admin_booking_for_today_with_valid_groupon_810(app, order):
    """Groupon. Admin booking. "Days Booked In Advance" is set to 1 (= a day before the event the code must be
    used - the day is not met)"""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_today_event(order)
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[20:21], ids=get_ids)
def test_admin_booking_for_today_with_valid_groupon_809(app, order):
    """Groupon. Admin booking. "Days Booked In Advance" is set to 0 (= up to time of event - time is not met)."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.booking.select_today_event(order)
    app.booking.close_booking_is_over_alert()
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("order", admin_groupons[21:22], ids=get_ids)
def test_admin_booking_with_redeemed_groupon(app, order):
    """Groupon. Admin booking. Trying to apply the same code twice."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_redeemed_code(order)
    app.booking.select_event(order)
    app.booking.apply_invalid_promo_code(order)
    app.booking.fill_out_customer_info(order)
    app.booking.select_payment_method(order)
    app.booking.verify_payment_table(order)
    app.booking.submit_successful_booking()


data = admin_groupons[:5] + admin_groupons[7:8] + admin_groupons[10:14] + admin_groupons[17:18] + admin_groupons[19:22]


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_admin(order)
