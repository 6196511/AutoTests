import pytest
from data.orders import center_certificates, center_certificates_declines


@pytest.mark.parametrize("certificate", center_certificates, ids=[repr(x) for x in center_certificates])
def test_purchasing_certificate(call_center, certificate):
    """Selling certificates via call center."""
    call_center.certificate.select_certificate(certificate)
    call_center.certificate.make_successful_payment(certificate)
    call_center.certificate.verify_created_certificate(certificate)


@pytest.mark.parametrize("certificate", center_certificates_declines, ids=[repr(x) for x in center_certificates_declines])
def test_purchasing_certificate_declines(call_center, certificate):
    """Selling certificates via call center."""
    call_center.certificate.select_certificate(certificate)
    call_center.certificate.make_declined_payment(certificate)
    call_center.certificate.make_successful_payment(certificate)
    call_center.certificate.verify_created_certificate(certificate)
