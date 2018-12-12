from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement

switcher_OFF = '<div class="switch-button-button" style="width: 14px; height: 13px; left: -1px;"></div>'

class AddEditActivityPage(BasePage):

    url = 'https://ci004.godo.io/activity_information.aspx'
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
    switchers1 = Finds(by=By.XPATH, value="//div[@class='col-xs-12 col-sm-12 col-md-4 col-lg-4 demo'][1]//div[@class='switch-button-button']")
    switchers2 = Finds(by=By.XPATH,value="//div[@class='col-xs-12 col-sm-12 col-md-4 col-lg-4 demo'][2]//div[@class='switch-button-button']")
    switcher_minimum_enforce = Find(by=By.XPATH,value="//div[@class='col-xs-12 col-sm-12 col-md-4 col-lg-4 demo'][3]//div[@class='switch-button-button']")
    add_ticket_type = Find(by=By.XPATH, value="//a[@ng-click='vm.addNewPrice()']")
    first_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][1]//input[@ng-model='price.priceName']")
    first_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][1]//input[@ng-model='price.priceAmount']")
    first_ticket_viator = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][1]//select[@ng-model='price.priceViator']")
    second_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][2]//input[@ng-model='price.priceName']")
    second_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][2]//input[@ng-model='price.priceAmount']")
    second_ticket_viator = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][2]//select[@ng-model='price.priceViator']")
    third_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][3]//input[@ng-model='price.priceName']")
    third_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][3]//input[@ng-model='price.priceAmount']")
    third_ticket_viator = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][3]//select[@ng-model='price.priceViator']")
    fourth_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][4]//input[@ng-model='price.priceName']")
    fourth_ticket_price = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][4]//input[@ng-model='price.priceAmount']")
    fourth_ticket_viator = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][4]//select[@ng-model='price.priceViator']")
    first_guide = Find(by=By.XPATH, value="//h2[text()='Guides']/..//select")
    first_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][1]//select[@ng-model='ga.selectedItem']")
    second_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][2]//select[@ng-model='ga.selectedItem']")
    third_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][3]//select[@ng-model='ga.selectedItem']")
    fourth_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][4]//select[@ng-model='ga.selectedItem']")
    remove_first_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][1]//button[@ng-click='vm.removeItem($index)']")
    remove_second_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][2]//button[@ng-click='vm.removeItem($index)']")
    remove_third_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][3]//button[@ng-click='vm.removeItem($index)']")
    remove_fourth_linked_activity = Find(by=By.XPATH, value="//h2[text()='Linked Activities']/..//div[@ng-repeat='ga in vm.items track by $index'][4]//button[@ng-click='vm.removeItem($index)']")
    what_included = Find(by=By.XPATH, value="//textarea[@id='activityIncluded']")
    what_know = Find(by=By.XPATH, value="//textarea[@id='activityKnow']")
    what_bring = Find(by=By.XPATH, value="//textarea[@id='activityBring']")
    review_redirect = Find(by=By.XPATH, value="//select[@id='activity_review_threshold']")
    review_website = Find(by=By.XPATH, value="//input[@id='review_url']")
    cancel_button = Find(by=By.XPATH, value="//a[text()='Cancel']")
    save_button = Find(by=By.XPATH, value="//button[@id='submitactivity']")
    alert_message = Find(by=By.XPATH, value="//label[@id='errormsg']")
    duration_alert = Find(by=By.XPATH, value="//div[@id='divError']")
    ticket_maximum_alert = Find(by=By.XPATH, value="//div[@class='activity_minticketsformError parentFormform1 formError']")
    viator1_alert = Find(by=By.XPATH, value="//div[@class='viator_0formError parentFormform1 formError']")
    viator2_alert = Find(by=By.XPATH, value="//div[@class='viator_1formError parentFormform1 formError']")
    viator3_alert = Find(by=By.XPATH, value="//div[@class='viator_2formError parentFormform1 formError']")
    viator4_alert = Find(by=By.XPATH, value="//div[@class='viator_3formError parentFormform1 formError']")
    delete_first_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][1]//a[@ng-if='vm.activity.prices.length != 1']")
    delete_second_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][2]//a[@ng-if='vm.activity.prices.length != 1']")
    delete_third_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][3]//a[@ng-if='vm.activity.prices.length != 1']")
    delete_fourth_ticket_type = Find(by=By.XPATH, value="//div[@ng-repeat='price in vm.activity.prices track by $index'][4]//a[@ng-if='vm.activity.prices.length != 1']")
    ticket_type_alert = Find(by=By.XPATH, value="//div[@class='form-validation-field-0formError parentFormform1 formError']")
    ticket_price_alert = Find(by=By.XPATH, value="//div[@class='form-validation-field-5formError parentFormform1 formError']")

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def get_selected_value(self, web_element):
        return Select(web_element).first_selected_option.text

