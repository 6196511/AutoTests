from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement



class EventScheldulerPage(BasePage):


    scheldule_type = Find(by=By.XPATH, value="//select[@id='schedule_type']")
    onetime_field = Find(by=By.XPATH, value="//input[@id='onetime_date']")
    date_calendar = Finds(by=By.XPATH, value="//button[@class='pika-button pika-day']")
    onetime_hour = Find(by=By.XPATH, value="//select[@id='onetime_time_hour']")
    onetime_minute = Find(by=By.XPATH, value="//select[@id='onetime_time_minute']")
    onetime_ampm = Find(by=By.XPATH, value="//select[@id='onetime_time_ampm']")
    onetime_add = Find(by=By.XPATH, value="//button[@id='addevents_onetime']")



    popup_OK = Find(by=By.XPATH, value="//button[@data-bb-handler='ok']")


