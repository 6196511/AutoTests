import pytest
from data.orders import *

data = customer_data[:16] + customer_declines + customer_valid_codes


@pytest.mark.parametrize("order", data, ids=[repr(x) for x in data])
def test_event_manifest_verification(app, order):
    """Checking booked tickets in the event manifest and customer event page."""

    # GoDo-157 Bug 2601 Customer-facing. Fully paid booking with promo code shows in the event manifest as debt
    # GoDo-312, Grand Total = 0 %, Grand Total = 0 $
    # Bug 3111 Customer Event Charges. Discount field is missing in case grand total  = 0 after applying a promo code

    app.calendar.select_event(order)
    app.calendar.verify_event_manifest(order)
    app.calendar.verify_customer_event_customer(order)
