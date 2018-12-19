from pytest import register_assert_rewrite

register_assert_rewrite('actions.activity_hub',
                        'actions.addons',
                        'actions.admin_booking',
                        'actions.calendar',
                        'actions.certificate',
                        'actions.customer_booking',
                        'actions.customer_certificate',
                        'actions.groupons',
                        'actions.people_hub',
                        'actions.rain_checks')

