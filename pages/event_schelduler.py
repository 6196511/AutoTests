from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement



class EventScheldulerPage(BasePage):


    scheldule_type = Find(by=By.XPATH, value="//select[@id='schedule_type']")
    onetime_field = Find(by=By.XPATH, value="//input[@id='onetime_date']")
    next_button_calendar_begin = Find(by=By.XPATH, value="//button[@class='pika-next']")
    next_button_calendar_enddate_rep = Find(by=By.XPATH, value="/html/body/div[5]/div/div/button[2]")
    next_button_calendar_enddate_repmult = Find(by=By.XPATH, value="/html/body/div[7]/div/div/button[2]")
    date_calendar = Finds(by=By.XPATH, value="//button[@class='pika-button pika-day']")
    onetime_hour = Find(by=By.XPATH, value="//select[@id='onetime_time_hour']")
    onetime_minute = Find(by=By.XPATH, value="//select[@id='onetime_time_minute']")
    onetime_ampm = Find(by=By.XPATH, value="//select[@id='onetime_time_ampm']")
    onetime_add = Find(by=By.XPATH, value="//button[@id='addevents_onetime']")
    rep_begin_field = Find(by=By.XPATH, value="//input[@id='dayonce_datebegin']")
    rep_end_field = Find(by=By.XPATH, value="//input[@id='dayonce_dateend']")
    date_calendar_end = Finds(by=By.XPATH, value="//button[@class='pika-button pika-day']")
    rep_hour = Find(by=By.XPATH, value="//select[@id='dayonce_timestart_hour']")
    rep_minute = Find(by=By.XPATH, value="//select[@id='dayonce_timestart_minute']")
    rep_ampm = Find(by=By.XPATH, value="//select[@id='dayonce_timestart_ampm']")
    rep_add = Find(by=By.XPATH, value="//button[@id='addevents_dayonce']")
    rep_mult_begin_field = Find(by=By.XPATH, value="//input[@id='daymultiple_datebegin']")
    rep_mult_end_field = Find(by=By.XPATH, value="//input[@id='daymultiple_dateend']")
    runs_mult_field = Find(by=By.XPATH, value="//input[@id='daymultiple_everyminutes']")
    rep_mult_hours_begin = Find(by=By.XPATH, value="//select[@id='daymultiple_timebegin_hour']")
    rep_mult_min_begin = Find(by=By.XPATH, value="//select[@id='daymultiple_timebegin_minute']")
    rep_mult_appm_begin = Find(by=By.XPATH, value="//select[@id='daymultiple_timebegin_ampm']")
    rep_mult_hours_end = Find(by=By.XPATH, value="//select[@id='daymultiple_timeend_hour']")
    rep_mult_min_end = Find(by=By.XPATH, value="//select[@id='daymultiple_timeend_minute']")
    rep_mult_appm_end = Find(by=By.XPATH, value="//select[@id='daymultiple_timeend_ampm']")
    rep_every_min = Find(by=By.XPATH, value="//input[@id='daymultiple_everyminutes']")
    rep_add_mult = Find(by=By.XPATH, value="//button[@id='addevents_daymultiple']")
    popup_OK = Find(by=By.XPATH, value="//button[@data-bb-handler='ok']")


