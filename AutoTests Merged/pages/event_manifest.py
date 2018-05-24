from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement


class EventManifestPage(BasePage):
    close_button = Find(by=By.XPATH, value="//i[@class='close-x fa fa-times pull-right visible-md visible-lg hidden-xs hidden-sm']")
    date_time_title = Find(by=By.XPATH, value="//h3[@class='calendar_modal_header_left_subtitle ng-binding']")
    activity_name_title = Find(by=By.XPATH, value="//h2[@class='modal-title ng-binding']")