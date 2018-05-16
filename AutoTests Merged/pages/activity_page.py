from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find


class AddEditActivityPage(BasePage):

    activity_name = Find(by=By.XPATH, value="//input[@id='activity_name']")
    activity_url = Find(by=By.XPATH, value="//input[@id='activity_Url']")
    activity_status = Find(by=By.XPATH, value="//select[@id='activity_status']")
    branch = Find(by=By.XPATH, value="//select[@id='branch_id']")
    starting_location = Find(by=By.XPATH, value="//select[@id='location_id']")
    time_zone = Find(by=By.XPATH, value="//select[@id='timezone_id']")
    activity_description = Find(by=By.XPATH, value="//textarea[@id='activity_description_entity']")
    cancellation_policy = Find(by=By.XPATH, value="//input[@id='cancellation_policy_description']")
    sales_tax = Find(by=By.XPATH, value="//input[@id='activity_salestax']")
    activity_duration_days = Find(by=By.XPATH, value="//input[@name='activity-days']")
    activity_duration_hours = Find(by=By.XPATH, value="//input[@name='activity-hours']")
    activity_duration_minutes = Find(by=By.XPATH,value="//input[@name='activity-minutes']")
    activity_color = Find(by=By.XPATH, value="//select[@name='activity-color']")
    ticket_maximum = Find(by=By.XPATH, value="//input[@id='activity_maxtickets']")
    sell_out_alert = Find(by=By.XPATH, value="//select[@id='activity_alert_selloutthreshold_percent']")
    alert_guide_upon_sellout = Find(by=By.XPATH, value="//select[@ng-model='vm.activity.shouldAlertGuideUponSelloutThreshold']")
    stop_booking_sold = Find(by=By.XPATH, value="//select[@ng-model='vm.activity.stopBookingMinuteBefore']")
    ticket_minimum = Find(by=By.XPATH, value="//input[@id='activity_mintickets']")
    minimum_not_met_alert = Find(by=By.XPATH, value="//input[@id='activity_min_not_met_hours']")
    stop_no_sales = Find(by=By.XPATH, value="//input[@id='activity_stop_before_hours']")
    stop_midnight_before = Find(by=By.XPATH, value="//label[contains(text(), 'Stop Booking Midnight Before')]/..//div[@class='switch-button-background']")
    first_sale_closes_event = Find(by=By.XPATH, value="//label[contains(text(), 'First Sale Closes Event')]/..//div[@class='switch-button-background']")
    add_ticket_type = Find(by=By.XPATH, value="//a[text()='+ Add a Ticket Type']")
    first_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][1]//input[@ng-model='price.priceName']")
    first_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][1]//input[@ng-model='price.priceAmount']")
    second_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][2]//input[@ng-model='price.priceName']")
    second_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][2]//input[@ng-model='price.priceAmount']")
    third_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][3]//input[@ng-model='price.priceName']")
    third_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][3]//input[@ng-model='price.priceAmount']")
    fourth_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][4]//input[@ng-model='price.priceName']")
    fourth_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices'][4]//input[@ng-model='price.priceAmount']")
    first_guide = Find(by=By.XPATH, value="//h2[text()='Guides']/..//select")
    first_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//select")
    what_included = Find(by=By.XPATH, value="//textarea[@id='activityIncluded']")
    what_know = Find(by=By.XPATH, value="//textarea[@id='activityKnow']")
    what_bring = Find(by=By.XPATH, value="//textarea[@id='activityBring']")
    review_redirect = Find(by=By.XPATH, value="//select[@id='activity_review_threshold']")
    review_website = Find(by=By.XPATH, value="//input[@id='review_url']")

    cancel_button = Find(by=By.XPATH, value="//a[text()='Cancel']")
    save_button = Find(by=By.XPATH, value="//button[@id='submitactivity']")

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)