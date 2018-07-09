import pytest
from data.orders import customer_groupons


@pytest.mark.parametrize("order", customer_groupons[:8], ids=[repr(x) for x in customer_groupons[:8]])
def test_customer_booking_with_groupons(app, order):
    """Booking tickets via customer with groupon."""
    app.booking.refresh_page()
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


@pytest.mark.parametrize("order", customer_groupons[8:13], ids=[repr(x) for x in customer_groupons[8:13]])
def test_customer_booking_with_invalid_groupons(app, order):
    """Booking tickets via customer with invalid groupon."""
    app.booking.refresh_page()
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


@pytest.mark.parametrize("order", customer_groupons[13:14], ids=[repr(x) for x in customer_groupons[13:14]])
def test_customer_booking_with_nonexistent_groupons(app, order):
    """Booking tickets via customer with nonexistent groupon."""
    app.booking.refresh_page()
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


@pytest.mark.parametrize("order", customer_groupons[14:15], ids=[repr(x) for x in customer_groupons[14:15]])
def test_customer_booking_with_redeemed_groupon(app, order):
    """Groupon. Customer Facing. Trying to apply the same code twice."""
    app.booking.refresh_page()
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
