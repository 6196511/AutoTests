from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webium import BasePage, Find
from webium.wait import wait


class AdminBookingPage(BasePage):

    # First tab.

    activity_list = Find(by=By.XPATH, value="//select[@id='activity'][@ng-model='vm.selectedActivity']")
    first_tickets_type = Find(by=By.XPATH, value="//tbody/tr[1]//input")
    second_tickets_type = Find(by=By.XPATH, value="//tbody/tr[2]//input")
    third_tickets_type = Find(by=By.XPATH, value="//tbody/tr[3]//input")
    fourth_tickets_type = Find(by=By.XPATH, value="//tbody/tr[4]//input")
    empty_space_first_tab = Find(by=By.XPATH, value="//h1[text()='Add Booking']")
    name_first_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[1]/td[1]")
    name_second_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[2]/td[1]")
    name_third_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[3]/td[1]")
    name_fourth_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[4]/td[1]")
    datepicker = Find(by=By.ID, value="datepicker_1")
    time = Find(by=By.XPATH, value="//select[@ng-options='item as item.time for item in vm.times']")
    enter_customer_information_button = Find(by=By.XPATH, value="//div[contains(text(), 'Enter Customer Information')]")

    # Customer Info tab.

    first_name = Find(by=By.XPATH, value="//input[@placeholder='First Name']")
    last_name = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.lastName']")
    email_address = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.email']")
    phone_number = Find(by=By.XPATH, value="//input[@placeholder='Phone Number']")
    zip_code = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.zipcode']")
    empty_space = Find(by=By.XPATH, value="//label[text()='Zip Code ']")
    complete_booking_button = Find(by=By.XPATH, value="//button[contains(text(), 'Complete Booking')]")

    # Payment tab.

    payment_type_list = Find(by=By.XPATH, value="//select[@ng-model='bookingdrawer.paymentType']")
    credit_card_list = Find(by=By.XPATH, value="//select[@ng-model='bookingdrawer.preselectedCard']")
    stripe = Find(by=By.XPATH, value="//iframe[@name='__privateStripeFrame4']")
    card_number_input = Find(by=By.XPATH, value="//input[@name='cardnumber']")
    card_date_input = Find(by=By.XPATH, value="//input[@name='exp-date']")
    card_cvc_input = Find(by=By.XPATH, value="//input[@name='cvc']")
    card_zip_input = Find(by=By.XPATH, value="//input[@name='postal']")
    cash_recieved = Find(by=By.XPATH, value="//input[@type='checkbox']")
    submit_booking_button = Find(by=By.XPATH, value="//div[contains(text(), 'Submit Booking')]")
    final_alert = Find(by=By.XPATH, value="//div[@class='modal-body ng-binding']")
    final_alert_ok_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='Ok']")

    # Charge (payment) table.

    ticket_total = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'ticketTotal')]/td[2]")
    discount = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'totalDiscount')]/td[2]")
    giftcertificate = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'totalGiftCertificate')]/td[2]")
    taxes = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'tax')]/td[2]")
    booking_fee = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'bookingfee')]/td[2]")
    grand_total = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'grandTotal')]/td[2]")


    def select_activity(self, activity):
        sleep(2)
        Select(self.activity_list).select_by_visible_text(activity)
        sleep(2)

    def select_date(self, year, month, day, total):
        wait(lambda: self.grand_total.text == total, timeout_seconds=30, waiting_for="Waiting until the pricing table is updated.")
        sleep(2)
        self._driver.execute_script(
            "$('#datepicker_1').datepicker('setDate', new Date(%s, %s-1, %s));" % (year, month, day))

    def select_time(self, time):
        Select(self.time).select_by_visible_text(time)

    def click_enter_customer_information(self):
        self._driver.execute_script("$('pageslide').animate({ scrollTop: '200px' })")
        wait(lambda: self.enter_customer_information_button.is_displayed())
        self.enter_customer_information_button.click()

    def select_payment_type(self, payment_type):
        wait(lambda: self.payment_type_list.is_displayed())
        Select(self.payment_type_list).select_by_visible_text(payment_type)

    def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
        Select(self.credit_card_list).select_by_visible_text("New Card")
        wait(lambda: self.stripe.is_enabled())
        self._driver.switch_to.frame(self.stripe)
        wait(lambda: self.card_number_input.is_enabled())
        self.card_number_input.clear()
        # wait(lambda: self.card_number_input.is_enabled())
        # sleep(1)
        self.card_number_input.send_keys(card_number)
        self.card_date_input.send_keys(card_date)
        self.card_cvc_input.send_keys(card_cvc)
        if card_zip is not None:
            self.card_zip_input.send_keys(card_zip)
        self._driver.switch_to.default_content()

    def select_saved_card(self, saved_card):
        Select(self.credit_card_list).select_by_visible_text(saved_card)
