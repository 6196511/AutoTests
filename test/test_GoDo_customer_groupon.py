import pytest
from data.orders import customer_groupons, get_ids


@pytest.mark.parametrize("order", customer_groupons[:8], ids=get_ids)
def test_customer_booking_with_groupons(app, order):
    """Booking tickets via customer with groupon."""
    app.refresh_page()
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


@pytest.mark.parametrize("order", customer_groupons[8:13], ids=get_ids)
def test_customer_booking_with_invalid_groupons(app, order):
    """Booking tickets via customer with invalid groupon."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.apply_invalid_promo_code(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)


@pytest.mark.parametrize("order", customer_groupons[13:14], ids=get_ids)
def test_customer_booking_with_nonexistent_groupons(app, order):
    """Booking tickets via customer with nonexistent groupon."""
    app.refresh_page()
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.apply_invalid_promo_code(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)


@pytest.mark.parametrize("order", customer_groupons[14:15], ids=get_ids)
def test_customer_booking_with_redeemed_groupon(app, order):
    """Groupon. Customer Facing. Trying to apply the same code twice."""
    app.refresh_page()
    app.groupons.navigate_to()
    app.groupons.get_redeemed_code(order)
    app.customer_booking.open_page(order)
    app.customer_booking.select_tickets_buttons(order)
    app.customer_booking.select_date(order)
    app.customer_booking.select_time(order)
    app.customer_booking.fill_info(order)
    app.customer_booking.skip_addons()
    app.customer_booking.apply_invalid_promo_code(order)
    app.customer_booking.verify_payment_page(order)
    app.customer_booking.make_payment(order)
    app.customer_booking.verify_summary_details(order)


data = customer_groupons[0:5] + customer_groupons[7:12] + customer_groupons[13:15]


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)
