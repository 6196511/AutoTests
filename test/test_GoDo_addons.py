import pytest
from data.addons import addons
from data.orders import addons as admin
from data.orders import get_ids


@pytest.mark.parametrize("addons", addons[0:1], ids=get_ids)
def test_add_addon_222(app, addons):
    """Add add-on."""
    app.addons.create_addon(addons)
    app.addons.find_addon(addons)


@pytest.mark.parametrize("addons", addons[0:1], ids=get_ids)
def test_add_type_199(app, addons):
    """Adding Add-On(s) Type (Extensions) (all fields)."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_type(addons)
    app.addons.check_type_present(addons)


@pytest.mark.parametrize("addons", addons[0:1], ids=get_ids)
def test_add_activity_92_and_372(app, addons):
    """Adding an activity for an Add-on addon_new.aspx."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_activity(addons)
    app.addons.verify_activity_table(addons)


@pytest.mark.parametrize("addons", addons[1:2], ids=get_ids)
def test_add_activity_94_373_cancel(app, addons):
    """Add new activity Add on(s) (cancel button check)."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_activity_cancel(addons)
    app.addons.verify_activity_not_present(addons)


@pytest.mark.parametrize("addons", addons[2:3], ids=get_ids)
def test_delete_activity_96(app, addons):
    """Delete activity from add-on."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.delete_activity_cancel(addons)
    app.addons.verify_activity_present(addons)


@pytest.mark.parametrize("addons", addons[2:3], ids=get_ids)
def test_delete_activity_95(app, addons):
    """Delete activity from add-on."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.delete_activity(addons)
    app.addons.verify_activity_not_present(addons)


@pytest.mark.parametrize("admin", admin[0:1], ids=get_ids)
def test_admin_booking_206_241_237(app, admin):
    """Booking tickets via admin with addons."""
    app.refresh_page()
    app.addons.get_addon_name(admin)
    app.booking.select_event(admin)
    app.booking.select_addon(admin)
    app.booking.fill_out_customer_info(admin)
    app.booking.select_payment_method(admin)
    app.booking.verify_payment_table(admin)
    app.booking.submit_successful_booking()


@pytest.mark.parametrize("admin", admin[1:2], ids=get_ids)
def test_admin_booking_207(app, admin):
    """Deleted activity add-ons should not be available for booking."""
    app.refresh_page()
    app.addons.get_addon_name(admin)
    app.booking.select_event(admin)
    app.booking.addon_not_present(admin)


@pytest.mark.parametrize("addons", addons[3:4], ids=get_ids)
def test_add_type_inactive(app, addons):
    """Adding Add-On(s) Type with inactive status."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_type(addons)
    app.addons.check_type_present(addons)


@pytest.mark.parametrize("admin", admin[3:4], ids=get_ids)
def test_admin_booking_236(app, admin):
    """Checking addon type (extension) with inactive status while booking."""
    app.refresh_page()
    app.addons.get_addon_name(admin)
    app.booking.select_event(admin)
    app.booking.type_not_present(admin)


@pytest.mark.parametrize("addons", addons[4:5], ids=get_ids)
def test_add_type_cancel_368(app, addons):
    """Creating Add-on's Type (cancel button check)."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_type_cancel(addons)
    app.addons.check_type_not_present(addons)


@pytest.mark.parametrize("addons", addons[3:4], ids=get_ids)
def test_delete_type_cancel_370(app, addons):
    """Delete Add-on's Type (cancel button check)."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.delete_type_cancel(addons)
    app.addons.check_type_present(addons)


@pytest.mark.parametrize("addons", addons[3:4], ids=get_ids)
def test_delete_type_369(app, addons):
    """Delete Add-on's Type."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.delete_type(addons)
    app.addons.check_type_not_present(addons)


@pytest.mark.parametrize("addons", addons[5:6], ids=get_ids)
def test_add_type_366(app, addons):
    """Creating Add-on's Type (maximal length of the fields)."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.find_addon(addons)
    app.addons.add_type(addons)
    app.addons.check_type_present(addons)


@pytest.mark.parametrize("addons", addons[0:1], ids=get_ids)
def test_delete_addon_cancel_229(app, addons):
    """Delete add-on."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.delete_addon_cancel(addons)
    app.addons.find_addon(addons)


@pytest.mark.parametrize("addons", addons[0:1], ids=get_ids)
def test_delete_addon_230(app, addons):
    """Delete add-on."""
    app.addons.get_addon_name(addons)
    app.refresh_page()
    app.addons.navigate_to()
    app.addons.delete_addon(addons)
    app.addons.verify_deletion(addons)


@pytest.mark.parametrize("admin", admin[2:3], ids=get_ids)
def test_admin_booking_221(app, admin):
    """Deleted addons shouldn't show up in the select addons list while booking."""
    app.refresh_page()
    app.addons.get_addon_name(admin)
    app.booking.select_event(admin)
    app.booking.addon_not_present(admin)
