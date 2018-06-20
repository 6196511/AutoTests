from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class AddStartingLocationPage(BasePage):
    url = 'https://dev.godo.io/location_information.aspx'
    location_name = Find(by=By.XPATH, value="//input[@id='location_name']")
    location_address_1 = Find(by=By.XPATH, value="//input[@id='location_address_1']")
    location_address_2 = Find(by=By.XPATH, value="//input[@id='location_address_2']")
    location_Country = Find(by=By.XPATH, value="//select[@id='location_Country']")
    location_state = Find(by=By.XPATH, value="//select[@id='location_state']")
    location_city = Find(by=By.XPATH, value="//input[@id='location_city']")
    location_zipcode = Find(by=By.XPATH, value="//input[@id='location_zipcode']")
    location_description = Find(by=By.XPATH, value="//textarea[@id='location_description']")
    save_button = Find(by=By.XPATH, value="//button[@class='btn w-sm btn-blue waves-effect waves-light m-l-15 addlocation']")
    search_location = Find(by=By.XPATH, value="//input[@id='search']")
    search_activity_field = Find(by=By.XPATH, value="//input[@placeholder='Start typing to search...']")
    activity_title = Find(by=By.XPATH, value="//h2[@class='hub-card-title ng-binding']")
    activity_actions = Find(by=By.XPATH, value="//button[@class='btn btn-primary dropdown-toggle activity-actions-btn']")
    edit_activity = Find(by=By.XPATH, value="//i[@class='fa fa-pencil mr20']")
    add_events = Find(by=By.XPATH, value="//i[@class='fa fa-plus mr20']")
    show_inactive = Find(by=By.XPATH, value="//*[@id='activityBG']/div[3]/div[2]/div/div/label")
    add_location_button = Find(by=By.XPATH, value="//a[@href='location_information.aspx']//h3[text()='Locations']")
    alert_message = Find(by=By.XPATH, value="//div[@class='alert alert-danger alert-dismissable']")