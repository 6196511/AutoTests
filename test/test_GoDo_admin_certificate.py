import pytest
from data.orders import admin_certificates, admin_certificates_declines


@pytest.mark.parametrize("certificate", admin_certificates, ids=[repr(x) for x in admin_certificates])
def test_purchasing_certificate(app, certificate):
    """Selling certificates via admin."""
    app.certificate.select_certificate(certificate)
    app.certificate.make_successful_payment(certificate)
    app.certificate.verify_created_certificate(certificate)


@pytest.mark.parametrize("certificate", admin_certificates_declines, ids=[repr(x) for x in admin_certificates_declines])
def test_purchasing_certificate_declines(app, certificate):
    """Selling certificates via admin."""
    app.certificate.select_certificate(certificate)
    app.certificate.make_declined_payment(certificate)
    app.certificate.make_successful_payment(certificate)
    app.certificate.verify_created_certificate(certificate)
