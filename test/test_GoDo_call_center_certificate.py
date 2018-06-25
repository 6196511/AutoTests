import pytest
from data.orders import center_certificates, center_certificates_declines


@pytest.mark.parametrize("certificate", center_certificates, ids=[repr(x) for x in center_certificates])
def test_purchasing_certificate(app, certificate):
    """Selling certificates via call center."""
    app.certificate.select_certificate(certificate)
    app.certificate.make_successful_payment(certificate)
    app.certificate.verify_created_certificate(certificate)


@pytest.mark.parametrize("certificate", center_certificates_declines, ids=[repr(x) for x in center_certificates_declines])
def test_purchasing_certificate_declines(app, certificate):
    """Selling certificates via call center."""
    app.certificate.select_certificate(certificate)
    app.certificate.make_declined_payment(certificate)
    app.certificate.make_successful_payment(certificate)
    app.certificate.verify_created_certificate(certificate)
