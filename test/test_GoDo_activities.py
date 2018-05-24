import pytest
from data.activity import testdata1


@pytest.mark.parametrize("activity", testdata1, ids=[repr(x) for x in testdata1])
def test_activity_creation(app, activity):
    """Create new activity."""
    app.activity_hub.add_activity(activity)

