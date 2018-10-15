from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from waiting import wait
from webium import BasePage, Find, Finds


class Event(WebElement):
    activity_name = Find(by=By.XPATH, value=".//div[@class='cal_event_header ng-binding']")
    time = Find(by=By.XPATH, value=".//div[@class='cal_event_tickets_avail ng-binding']")


class Day(WebElement):
    date = Find(by=By.XPATH, value="./div[@class='cal_month_day_date ng-binding']")
    events_list = Finds(Event, by=By.XPATH, value=".//div[@class='cal_week_event ng-scope']")
    view_all = Find(by=By.XPATH, value=".//a[text()='[View All]']")


class CalendarPage(BasePage):

    days_list = Finds(Day, by=By.XPATH, value="//div[@class='cal_month_day ng-scope']")
    without_booking = Find(by=By.XPATH, value="//input[@id='hide-without-booking']")


######  Event manifest drawer.  ######

# class Tickets(WebElement):
#     tickets = Finds(by=By.XPATH, value="./li")


class Guest(WebElement):
    name = Find(by=By.XPATH, value="./td[2]/a")
    tickets = Finds(by=By.XPATH, value=".//span[@ng-repeat='ticket in booking.tickets']")
    addons = Finds(by=By.XPATH, value=".//span[@ng-repeat='addon in booking.addons']")
    amount_due = Find(by=By.XPATH, value="./td[3]/a")
    phone = Find(by=By.XPATH, value="./td[2]/div[2]/a")
    email = Find(by=By.XPATH, value="./td[2]/div[1]/a")
    actions = Find(by=By.XPATH, value="./td[8]//button")
    refund = Find(by=By.XPATH, value=".//li/a[text()='Refund']")
    cancel = Find(by=By.XPATH, value=".//li/a[text()='Cancel Guest']")
    rain_check = Find(by=By.XPATH, value=".//li/a[text()='Rain Check']")


class EventManifest(BasePage):
    event_title = Find(by=By.XPATH, value="//span[@class='manifest-act-title ng-binding']")
    event_date = Find(by=By.XPATH, value="//span[@class='manifest-title-desc ng-binding'][1]")
    event_status = Find(by=By.XPATH, value="//span[@class='manifest-title-desc']/span")

    actions_button = Find(by=By.XPATH, value="//button[contains(text(), 'Actions')]")
    edit_event = Find(by=By.XPATH, value="//a[text()='Edit Event']")
    re_open_bookings = Find(by=By.XPATH, value="//a[text()='Re-Open Bookings']")
    close_bookings = Find(by=By.XPATH, value="//a[text()='Close Bookings']")
    cancel_event = Find(by=By.XPATH, value="//a[text()='Cancel Event']")
    add_booking = Find(by=By.XPATH, value="//button[contains(text(), 'Add Booking')]")
    print = Find(by=By.XPATH, value="//button[contains(text(), 'Print')]")

    close_button = Find(by=By.XPATH, value="//div[@ng-if='manifest.isLoaded']//i[contains(@class, 'close-x')]")
    no_bookings = Find(by=By.XPATH, value="//event-booking-list//tbody/tr")
    guests_list = Finds(Guest, by=By.XPATH, value="//event-booking-list//tbody/tr")
    pop_up = Find(by=By.XPATH, value="//div[@class='modal-body ng-binding']")
    pop_up_refund = Find(by=By.XPATH, value="//div[@class='tab-content']//div[@class='col-sm-12 ng-binding']")
    pop_up_ok_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()!='Cancel']")
    pop_up_cancel_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='Cancel']")
    process_refund = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[contains(text(), 'Process Refund')]")

    # Add booking pop-up.
    activity_cart = Find(by=By.XPATH, value="//div[@class='cart-title ng-binding']")

# Customer Event Charges ###

class TicketsTable(WebElement):
    type = Find(by=By.XPATH, value="./td[1]")
    price = Find(by=By.XPATH, value="./td[2]")
    quantity = Find(by=By.XPATH, value="./td[3]")
    total = Find(by=By.XPATH, value="./td[4]")


class CustomerEventPage(BasePage):
    name = Find(by=By.XPATH, value="//div[@id='customereventchargeinfohtml']/div[1]/a")
    tickets_table = Finds(TicketsTable, by=By.XPATH, value="//h4[text()='Ticket Information']/../table[1]/tbody/tr")
    ticket_total = Find(by=By.XPATH, value="//td[text()='Ticket Total:']/../td[2]")
    addon = Find(by=By.XPATH, value="//td[text()='Add On(s) Price:']/../td[2]")
    discount = Find(by=By.XPATH, value="//td[text()='Discount:']/../td[2]")
    gift_certificate = Find(by=By.XPATH, value="//td[text()='Gift certificate applied:']/../td[2]")
    booking_fee = Find(by=By.XPATH, value="//td[text()='Booking Fee']/../td[2]")
    tax = Find(by=By.XPATH, value="//td[contains(text(), 'Tax')]/../td[2]")
    grand_total = Find(by=By.XPATH, value="//td[text()='Grand Total:']/../td[2]")
    total_charges = Find(by=By.XPATH, value="//td[text()='Total Charges:']/../td[2]")
    total_due = Find(by=By.XPATH, value="//td[text()='Total Due:']/../td[2]")

    # Booking Charge and Reservation

    amount_options = Find(by=By.XPATH, value="//select[@id='chargehtml_prefill']")
    charge_type = Find(by=By.XPATH, value="//select[@id='charge_type']")
    cash_received = Find(by=By.XPATH, value="//input[@id='chargehtml_cashreceived']")
    check_input = Find(by=By.XPATH, value="//input[@id='charge_checknumbner']")
    final_button = Find(by=By.XPATH, value="//button[@id='chargehtml_dobooking']")
    status = Find(by=By.XPATH, value="//div[@id='statusarea']")
    charge_history_amount = Find(by=By.XPATH, value="//tbody/tr[1]/td[5]")
    charge_history_status = Find(by=By.XPATH, value="//tbody/tr[1]/td[6]")

    stripe = Find(by=By.XPATH, value="//iframe[@name='__privateStripeFrame4']")
    card_number_input = Find(by=By.XPATH, value="//input[@name='cardnumber']")
    card_date_input = Find(by=By.XPATH, value="//input[@name='exp-date']")
    card_cvc_input = Find(by=By.XPATH, value="//input[@name='cvc']")
    card_zip_input = Find(by=By.XPATH, value="//input[@name='postal']")

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
        wait(lambda: self.stripe.is_enabled())
        self._driver.switch_to.frame(self.stripe)
        wait(lambda: self.card_number_input.is_enabled())
        self.card_number_input.clear()
        self.card_number_input.send_keys(card_number)
        self.card_date_input.send_keys(card_date)
        self.card_cvc_input.send_keys(card_cvc)
        self.card_zip_input.send_keys(card_zip)
        self._driver.switch_to.default_content()
