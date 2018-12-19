import pytest
from data.orders import customer_certificates, customer_certificates_declines, get_ids


@pytest.mark.parametrize("certificate", customer_certificates, ids=get_ids)
def test_purchasing_certificate(customer, certificate):
    """Purchasing gift certificates via customer facing with valid credit card."""
    customer.certificate.open_page(certificate)
    customer.certificate.fill_first_form(certificate)
    customer.certificate.verify_payment_info(certificate)
    customer.certificate.make_successful_payment(certificate)
    customer.certificate.verify_summary_details(certificate)


@pytest.mark.parametrize("certificate", customer_certificates_declines, ids=get_ids)
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
