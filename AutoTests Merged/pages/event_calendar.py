from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement


class EventTicket(WebElement):
    day_slot_time = Finds(by=By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")



class EventCalendarPage(BasePage):

    url = 'https://dev.godo.io/event_calendar.aspx'
    activity_name = Find(by=By.XPATH, value="//select[@id='activity_id']")
    hide_events = Find(by=By.XPATH, value="//input[@ng-model='calendar.hideEventsWithoutBooking']")
    date_picker = Find(by=By.XPATH, value="//i[@ng-model='calendar.customDate']")
    day_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setDayView()']")
    day_date = Find(by=By.XPATH, value="//h3[@class='col-sm-5 col-md-4 cal_header ng-binding']")
    day_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")
    days_date_picker = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    time = Finds(by=By.XPATH, value="//div[@class='cal_event_tickets_avail ng-binding']")






