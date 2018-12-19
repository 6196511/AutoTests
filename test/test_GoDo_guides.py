import pytest
from data.guides import guides
from data.orders import get_ids


@pytest.mark.parametrize("guides", guides[0:1], ids=get_ids)
def test_add_and_delete_guide(app, guides):
    """Add guide and delete. Only required fields."""
    app.people_hub.add_guide(guides)
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.verify_guides_details(guides)
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.delete_guide(guides)


@pytest.mark.parametrize("guides", guides[1:2], ids=get_ids)
def test_invalid_username(app, guides):
    """Trying to add already existed guide."""
    app.people_hub.add_guide_with_invalid_username(guides)


@pytest.mark.parametrize("guides", guides[2:3], ids=get_ids)
def test_import_guide(app, guides):
    """Import guide."""
    app.people_hub.import_guide(guides)
    app.people_hub.find_imported_guide(guides)


@pytest.mark.parametrize("guides", guides[3:4], ids=get_ids)
def test_import_guide_invalid_name(app, guides):
    """Import guide with invalid name."""
    app.people_hub.import_guide(guides)
    app.people_hub.verify_alert()
    app.people_hub.close_pop_up()


@pytest.mark.parametrize("guides", guides[4:5], ids=get_ids)
def test_import_guide_invalid_rate(app, guides):
    """Import guide with invalid pay rate."""
    app.people_hub.import_guide(guides)
    app.people_hub.verify_error_messages("* Invalid Amount", 1)
    app.people_hub.close_pop_up()


def test_import_submit_empty_form_177(app):
    """Import guide submit empty form."""
    app.people_hub.submit_empty_form()
    app.people_hub.verify_error_messages("* This field is required", 2)
    app.people_hub.close_pop_up()


@pytest.mark.parametrize("guides", guides[5:6], ids=get_ids)
def test_import_guide_blank_pay_rate(app, guides):
    """Import guide with black pay rate field."""
    app.people_hub.import_guide_username_only(guides)
    app.people_hub.verify_error_messages("* This field is required", 1)
    app.people_hub.close_pop_up()


@pytest.mark.parametrize("guides", guides[6:7], ids=get_ids)
def test_guide_assign_activity(app, guides):
    """Assign Activity to Guide - Guide's page."""
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.edit_guide_activity(guides.trained_activities)
    app.activity_hub.navigate_to()
    app.activity_hub.to_edit_page(guides.trained_activities)
    app.activity_hub.verify_trained_guides(guides.first_name + " " + guides.last_name)


@pytest.mark.parametrize("guides", guides[7:8], ids=get_ids)
def test_guide_unassign_activity(app, guides):
    """Unassign Activity from Guide - Guide's page."""
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.edit_guide_remove_activity()
    app.activity_hub.navigate_to()
    app.activity_hub.to_edit_page(guides.trained_activities)
    app.activity_hub.verify_trained_guides("-- Select Guide --")


@pytest.mark.parametrize("guides", guides[8:9], ids=get_ids)
def test_guide_change_activity(app, guides):
    """Change Activity on guide page."""
    old_activity = "Swamp & Bayou Tour"
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.edit_guide_activity(old_activity)
    app.people_hub.navigate_to()
    app.people_hub.find_guide_by_email(guides)
    app.people_hub.edit_guide_activity(guides.trained_activities)
    app.activity_hub.navigate_to()
    app.activity_hub.to_edit_page(old_activity)
    app.activity_hub.verify_trained_guides("-- Select Guide --")
    app.activity_hub.navigate_to()
    app.activity_hub.to_edit_page(guides.trained_activities)
    app.activity_hub.verify_trained_guides(guides.first_name + " " + guides.last_name)
