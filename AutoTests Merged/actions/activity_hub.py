from time import sleep

from waiting import wait

from pages.activity_hub_page import ActivityHubPage
from pages.activity_page import AddEditActivityPage
from pages.navigation_bar import NavigationBar


class ActivityHub:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = NavigationBar(driver=self.driver)
        self.activity_hub = ActivityHubPage(driver=self.driver)
        self.activity_page = AddEditActivityPage(driver=self.driver)

    def add_activity(self, activity):
        self.navigate_to()
        self.activity_hub.add_activity_button.click()
        self.fill_out_form(activity)
        self.activity_page.save_button.click()

    def fill_out_form(self, activity):
        sleep(5)
        self.activity_page.activity_name.send_keys(activity.activity_name)
        if activity.activity_url is not None:
            self.activity_page.activity_url.send_keys(activity.activity_url)
        self.activity_page.select(self.activity_page.activity_status, activity.activity_status)
        self.activity_page.select(self.activity_page.branch, activity.branch)
        self.activity_page.select(self.activity_page.starting_location, activity.starting_location)
        self.activity_page.select(self.activity_page.time_zone, activity.time_zone)
        if activity.activity_description is not None:
            self.activity_page.activity_description.send_keys(activity.activity_description)
        self.activity_page.cancellation_policy.send_keys(activity.cancellation_policy)
        if activity.sales_tax is not None:
            self.activity_page.sales_tax.send_keys(activity.sales_tax)
        self.activity_page.activity_duration_days.clear()
        self.activity_page.activity_duration_days.send_keys(activity.activity_duration_days)
        self.activity_page.activity_duration_hours.clear()
        self.activity_page.activity_duration_hours.send_keys(activity.activity_duration_hours)
        self.activity_page.activity_duration_minutes.clear()
        self.activity_page.activity_duration_minutes.send_keys(activity.activity_duration_minutes)
        if activity.activity_color is not None:
            self.activity_page.select(self.activity_page.activity_color, activity.activity_color)
        self.activity_page.ticket_maximum.clear()
        self.activity_page.ticket_maximum.send_keys(activity.ticket_maximum)
        self.activity_page.select(self.activity_page.sell_out_alert, activity.sell_out_alert)
        if activity.alert_guide_upon_sellout is not None:
            self.activity_page.select(self.activity_page.alert_guide_upon_sellout, activity.alert_guide_upon_sellout)
        self.activity_page.select(self.activity_page.stop_booking_sold, activity.stop_booking_sold)
        self.activity_page.ticket_minimum.send_keys(activity.ticket_minimum)
        self.activity_page.minimum_not_met_alert.send_keys(activity.minimum_not_met_alert)
        if activity.stop_no_sales is not None:
            self.activity_page.stop_no_sales.send_keys(activity.stop_no_sales)
        if activity.stop_midnight_before is not None:
            self.activity_page.stop_midnight_before.click()
        if activity.first_sale_closes_event is not None:
            self.activity_page.first_sale_closes_event.click()
        self.activity_page.first_ticket_type.send_keys(activity.first_ticket_type)
        self.activity_page.first_ticket_price.send_keys(activity.first_ticket_price)
        self.activity_page.what_included.send_keys(activity.what_included)
        self.activity_page.what_know.send_keys(activity.what_know)
        self.activity_page.what_bring.send_keys(activity.what_bring)
        self.activity_page.review_redirect.send_keys(activity.review_redirect)

    def navigate_to(self):
        self.navigation_bar.sitemap.click()
        wait(lambda: self.navigation_bar.activity_hub.is_displayed())
        self.navigation_bar.activity_hub.click()



