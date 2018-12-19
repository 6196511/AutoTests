from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement


class EventTicket(WebElement):
    day_slot_time = Finds(by=By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")



class EventCalendarPage(BasePage):

    url = 'https://ci004.godo.io/event_calendar.aspx'
    activity_name = Find(by=By.XPATH, value="//select[@id='activity_id']")
    hide_events = Find(by=By.XPATH, value="//input[@ng-model='calendar.hideEventsWithoutBooking']")
    date_picker = Find(by=By.XPATH, value="//i[@ng-model='calendar.customDate']")
    date_picker_next = Find(by=By.XPATH, value="//i[@class='glyphicon glyphicon-chevron-right']")
    day_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setDayView()']")
    week_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setWeekView()']")
    month_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setMonthView()']")
    day_date = Find(by=By.XPATH, value="//h3[@class='col-sm-5 col-md-4 cal_header ng-binding']")
    day_slots = Finds(EventTicket, By.XPATH, value="//div[contains(@class,'cal_day_event')]")
    event_tickets = Finds(by=By.XPATH, value="//div[@class='cal_week_event ng-scope']")
    days_date_picker = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    time = Finds(by=By.XPATH, value="//div[@class='cal_event_tickets_avail ng-binding']")
    date_header = Find (by=By.XPATH, value="//span[@class='cal-header-text ng-binding']")
    time_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-sm-3 cal_event_time ng-binding']")
    close_button = Find(by=By.XPATH, value="//i[@class='close-x fa fa-times pull-right visible-md visible-lg visible-xs visible-sm']")
    date_time_title = Find(by=By.XPATH, value="//span[@class='manifest-title-desc ng-binding']")
    activity_name_title = Find(by=By.XPATH, value="//span[@class='manifest-act-title ng-binding']")
    customer_name_link = Find(by=By.XPATH, value="//a[contains(@href,'customer_information.aspx?customer_id')]")
    email_link = Find(by=By.XPATH, value="//a[@ng-if='booking.customerEmail']")
    phone_link = Find(by=By.XPATH, value="//a[contains(@ng-if,'booking.customerPhone1')]")
    guide_list = Find(by=By.XPATH, value="//select[@ng-model='ga.selectedItem']")
    save_guide = Find(by=By.XPATH, value="//button[@ng-click='vm.trySubmit(singleEventGuideAssignmentNoDetailsForm)']")
    paid_link = Find(by=By.XPATH, value="//a[contains(@ng-href,'customerEvent_charge.aspx')]")
    event_status = Find(by=By.XPATH, value="//span[@ng-bind='manifest.getEventStatusName(manifest.selectedEvent.status)']")
    add_booking_button = Find(by=By.XPATH, value="//button[@ng-click='manifest.addBooking(manifest.eventId)']")
    manifest_title = Find(by=By.XPATH, value="//div[@class='manifest-title-desc ng-binding']")
    manifest_tickets = Find(by=By.XPATH, value="/html/body/pageslide[1]/div/div/div/div[2]/div/div[2]")
    info_pop_up = Find(by=By.XPATH, value="//div[@class='modal-body ng-binding']")
    OK_info_pop_up = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")
