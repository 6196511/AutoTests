from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class RequestOFFPage(BasePage):

    url='https://dev.godo.io/guide_requestOff.aspx'
    request_off_entry = Finds(by=By.XPATH, value="//tr[@class='row']|//tr[@class='odd']|//tr[@class='even']")
    approval_dropdown = Finds(by=By.XPATH, value="//select[contains(@id, 'requestoff_status_')]")
    not_approved_button = Find(by=By.XPATH, value="//label[@class ='btn btn-danger']")
    approved_button = Find(by=By.XPATH, value="//label[@class ='btn btn-success']")
    tables = Finds(by=By.XPATH, value="//table[@id = 'dtRequestOff']")
