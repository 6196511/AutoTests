import pytest
from data.tickets import testdata_cus1


@pytest.mark.parametrize("tickets", testdata_cus1, ids=[repr(x) for x in testdata_cus1])
def test_customer_booking(customer, tickets):
    """Order tickets via customer facing."""
    customer.booking.open_page(tickets)
    customer.booking.select_tickets_buttons(tickets)
    customer.booking.select_date(tickets)
    customer.booking.select_time(tickets)
    customer.booking.fill_info(tickets)
    customer.booking.verify_payment_page(tickets)
    customer.booking.make_payment(tickets)
    customer.booking.verify_summary_details(tickets)
    customer.booking.close()
