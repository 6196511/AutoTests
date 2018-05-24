import pytest
from data.certificates import testdata_cus1, testdata_cus2


@pytest.mark.parametrize("certificate", testdata_cus1, ids=[repr(x) for x in testdata_cus1])
def test_purchasing_certificate(customer, certificate):
    """Purchasing gift certificates via customer facing with valid credit card."""
    customer.certificate.open_page(certificate)
    customer.certificate.fill_first_form(certificate)
    customer.certificate.verify_payment_info(certificate)
    customer.certificate.make_successful_payment(certificate)
    customer.certificate.verify_summary_details(certificate)


@pytest.mark.parametrize("certificate", testdata_cus2, ids=[repr(x) for x in testdata_cus2])
def test_purchasing_certificate_declines(customer, certificate):
    """Purchasing gift certificates via customer facing with invalid credit card."""
    customer.certificate.open_page(certificate)
    customer.certificate.fill_first_form(certificate)
    customer.certificate.verify_payment_info(certificate)
    customer.certificate.make_declined_payment(certificate)
    customer.certificate.make_successful_payment(certificate)
    customer.certificate.verify_summary_details(certificate)


@pytest.fixture
def stop():
    """Override admin's finalizer."""
    pass
