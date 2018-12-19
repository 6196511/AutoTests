from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement


class EventTicket(WebElement):
    day_slot_time = Finds(by=By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")


class GuidePage(BasePage):

    url = 'https://ci004.godo.io/g_calendar.aspx'
    activity_name = Find(by=By.XPATH, value="//select[@id='activity_id']")
    hide_events = Find(by=By.XPATH, value="//input[@ng-model='calendar.hideEventsWithoutBooking']")
    date_picker = Find(by=By.XPATH, value="//i[@ng-model='calendar.customDate']")
    date_picker_next = Find(by=By.XPATH, value="//i[@class='glyphicon glyphicon-chevron-right']")
    day_button = Find(by=By.XPATH, value="//a[@ng-click='$event.preventDefault(); calendar.setDayView()']")
    day_date = Find(by=By.XPATH, value="//h3[@class='col-sm-5 col-md-4 cal_header ng-binding']")
    day_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-xs-12 cal_day_event']")
    days_date_picker = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    time = Finds(by=By.XPATH, value="//div[@class='cal_event_tickets_avail ng-binding']")
    date_header = Find (by=By.XPATH, value="//span[@class='cal-header-text ng-binding']")
    time_slots = Finds(EventTicket, By.XPATH, value="//div[@class='col-sm-3 cal_event_time ng-binding']")
    close_button = Find(by=By.XPATH, value="//i[@class='close-x fa fa-times pull-right visible-md visible-lg hidden-xs hidden-sm']")
    date_time_title = Find(by=By.XPATH, value="//span[@id='startTime']")
    activity_name_title = Find(by=By.XPATH, value="//span[@id='activityName']")
    check_in = Find(by=By.XPATH, value="//input[@data-checkincheckbox]")
    event_complete = Find(by=By.XPATH, value="//button[@id='markeventcomplete']")
    next_month = Find(by=By.XPATH, value="//button[@class='btn btn-default btn-sm pull-right uib-right']")
    profile_dropdown = Find(by=By.XPATH, value='//a[@data-toggle="dropdown"]')
    logout_button = Find(by=By.XPATH, value='//*[@id="wrapper"]/div[2]/div[2]/div/div/ul/li[3]/ul/li[5]/a')
    add_booking = Find(by=By.XPATH, value="//button[contains(@ng-click,'drawer.open')]")
    event_tickets = Finds(by=By.XPATH, value="//div[@class='cal_week_event ng-scope']")
    search_field = Find(by=By.XPATH, value='//input[@ng-change="calendar.search()"]')
    customer_tickets = Find(by=By.XPATH, value='//*[@id="dtEventDetails"]/tbody/tr[1]/td[2]/b')

class GuideRequestOffPage (BasePage):
    url = 'https://ci004.godo.io/g_requestOff.aspx'
    company_drop_down = Find(by=By.XPATH, value="//select[@id='guideCompany_id']")
    start_date = Find(by=By.XPATH, value="//input[@id='start']")
    calendar_next_month = Finds(by=By.XPATH, value="//th[@class='next']")
    dates_calendar_start = Finds(by=By.XPATH, value="//td[@class='day']")
    end_date = Find(by=By.XPATH, value="//input[@id='end']")
    dates_calendar_end = Finds(by=By.XPATH, value="//td[@class='day']")
    reason_field = Find(by=By.XPATH, value="//textarea[@id='requestoff_reason']")
    I_aknowledge_checkbox = Find(by=By.XPATH, value="//input[@id='requestoffhtml_accept']")
    submit_request_button =  Find(by=By.XPATH, value="//button[@id='submitrequestoff']")
    pop_up_notification = Find(by=By.XPATH, value="//div[@class='bootbox-body']")
    pop_up_OK = Find(by=By.XPATH, value="/html/body/div[5]/div/div/div[2]/button")
    request_entry = Finds(by=By.XPATH, value="//tr[@class='gradeX']")


