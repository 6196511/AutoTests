import pytest
from data.orders import customer_data, customer_declines, customer_valid_codes, get_ids

data = customer_data[:16] + customer_declines + customer_valid_codes


@pytest.mark.parametrize("order", data, ids=get_ids)
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""
    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)
