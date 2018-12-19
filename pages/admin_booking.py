from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage, Find, Finds
from webium.wait import wait
from selenium.webdriver.support import expected_conditions as EC


class AddonsList(WebElement):
    name = Find(by=By.XPATH, value="./label")
    checkbox = Find(by=By.XPATH, value=".//input")
    type_list = Find(by=By.XPATH, value=".//select")


class AdminBookingPage(BasePage):

    # First tab.

    datepicker_next_month = Find(by=By.XPATH, value="//th[@class = 'next']")
    dates = Finds(by=By.XPATH, value="//td[@class = 'day available']")
    activity_list = Find(by=By.XPATH, value="//select[@id='activity'][@ng-model='vm.selectedActivity']")
    activities_in_list = Finds(by=By.XPATH, value="//option")
    first_tickets_type = Find(by=By.XPATH, value="//div[@name='tickets']//tr[1]//input")
    second_tickets_type = Find(by=By.XPATH, value="//div[@name='tickets']//tr[2]//input")
    third_tickets_type = Find(by=By.XPATH, value="//div[@name='tickets']//tr[3]//input")
    fourth_tickets_type = Find(by=By.XPATH, value="//div[@name='tickets']//tr[4]//input")
    empty_space_first_tab = Find(by=By.XPATH, value="//h1[text()='Add Booking']")
    name_first_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[1]/td[1]")
    name_second_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[2]/td[1]")
    name_third_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[3]/td[1]")
    name_fourth_tickets_type = Find(by=By.XPATH, value="//div[@class='form-group']//tbody/tr[4]/td[1]")
    datepicker = Find(by=By.ID, value="datepicker_1")
    available_days = Finds(by=By.XPATH, value="//*[@id='datepicker_1']//*[contains(@class, 'available')]")
    time = Find(by=By.XPATH, value="//select[@ng-options='item as item.time for item in vm.times']")
    custom_price = Find(by=By.XPATH, value="//input[@name='custom-price']")
    promo_code_input = Find(by=By.XPATH, value="//input[@name='promo-code']")
    gift_certificate_input = Find(by=By.XPATH, value="//input[@name='gift-certificate']")
    apply_discount = Find(by=By.XPATH, value="//div[text()='Apply Discount']")
    discount_pop_up = Find(by=By.XPATH, value="//div[@class='modal-content']//div[@class='modal-body ng-binding']")
    discount_pop_up_ok_button = Find(by=By.XPATH, value="//div[@class='modal-content']//button[text()='Ok']")
    enter_customer_information_button = Find(by=By.XPATH, value="//div[contains(text(), 'Enter Customer Information')]")
    addons_link = Find(by=By.XPATH, value="//button[@name='addons']")
    addons_list = Finds(AddonsList, by=By.XPATH, value="//div[@name='addonSelectionForm']//li")
    add_to_cart = Find(by=By.XPATH, value="//div[@name='addonSelectionForm']//button[text()='Add To Cart']")
    cancel_addon = Find(by=By.XPATH, value="//div[@name='addonSelectionForm']//button[text()='Cancel']")
    order_cart = Find(by=By.XPATH, value="//div[@class='cart-eventbox']")

    # Customer Info tab.

    first_name = Find(by=By.XPATH, value="//input[@placeholder='First Name']")
    last_name = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.lastName']")
    email_address = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.email']")
    phone_number = Find(by=By.XPATH, value="//input[@placeholder='Phone Number']")
    zip_code = Find(by=By.XPATH, value="//input[@ng-model='bookingdrawer.customer.zipcode']")
    empty_space = Find(by=By.XPATH, value="//label[text()='Zip Code ']")
    complete_booking_button = Find(by=By.XPATH, value="//button[contains(text(), 'Complete Booking')]")

    # Payment tab.

    channel_list = Find(by=By.XPATH, value="//select[@name='channel']")
    payment_type_list = Find(by=By.XPATH, value="//select[@ng-model='bookingdrawer.paymentType']")
    credit_card_list = Find(by=By.XPATH, value="//select[@ng-model='bookingdrawer.preselectedCard']")
    stripe = Find(by=By.XPATH, value="//iframe[@name='__privateStripeFrame4']")
    card_number_input = Find(by=By.XPATH, value="//input[@name='cardnumber']")
    card_date_input = Find(by=By.XPATH, value="//input[@name='exp-date']")
    card_cvc_input = Find(by=By.XPATH, value="//input[@name='cvc']")
    card_zip_input = Find(by=By.XPATH, value="//input[@name='postal']")
    cash_recieved = Find(by=By.XPATH, value="//input[@name='money-in-hand']")
    submit_booking_button = Find(by=By.XPATH, value="//div[contains(text(), 'Submit Booking')]")
    final_alert = Find(by=By.XPATH, value="//div[@class='modal-body ng-binding']")
    final_alert_ok_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='Ok']")

    # Charge (payment) table.

    ticket_total = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'ticketTotal')]/td[2]")
    discount = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'totalDiscount')]/td[2]")
    giftcertificate = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'totalGiftCertificate')]/td[2]")
    addons = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'addons')]/td[2]")
    taxes = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'tax')]/td[2]")
    booking_fee = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'bookingfee')]/td[2]")
    grand_total = Find(by=By.XPATH, value="//tr[contains(@ng-show, 'grandTotal')]/td[2]")

    def select_activity(self, activity):
        Select(self.activity_list).select_by_visible_text(activity)
        sleep(2)  # Added because of bug #2545.

    def select_date(self, year, month, day):
        wait(lambda: len(self.available_days) > 0, timeout_seconds=10,
             waiting_for="Waiting for available days appears.")
        self._driver.execute_script(
            "$('#datepicker_1').datepicker('setDate', new Date(%s, %s-1, %s));" % (year, month, day))

    def select_time(self, time):
        Select(self.time).select_by_visible_text(time)

    def get_time_list(self):
        return Select(self.time).options

    def click_enter_customer_information(self):
        self._driver.execute_script("arguments[0].scrollIntoView();", self.enter_customer_information_button)
        self.enter_customer_information_button.click()

    def select_payment_type(self, payment_type):
        wait(lambda: self.payment_type_list.is_displayed())
        Select(self.payment_type_list).select_by_visible_text(payment_type)

    def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
        Select(self.credit_card_list).select_by_visible_text("New Card")
        wait(lambda: self.stripe.is_enabled())
        self._driver.switch_to.frame(self.stripe)
        wait(lambda: self.card_number_input.is_enabled())
        attempts = 50
        card_number_size = 16
        for attempt in range(0, attempts):
            for number in range(0, card_number_size):
                self.card_number_input.send_keys(Keys.BACK_SPACE)
            self.card_number_input.send_keys(card_number)
            self.card_date_input.send_keys(card_date)
            actual_value_card = self.card_number_input.get_attribute('value')
            actual_value_card = actual_value_card.replace(" ", "")
            actual_value_date = self.card_date_input.get_attribute('value')
            actual_value_date = actual_value_date.replace(" / ", "")
            if actual_value_card == card_number and actual_value_date == card_date:
                break
            else:
                print("%s attempt failed. Entered: %s and %s but expected: %s and %s" %
                      (attempt, actual_value_card, actual_value_date, card_number, card_date))
        else:
            print("Correct value hasn't been entered.")
            exit()
        self.card_cvc_input.send_keys(card_cvc)
        if card_zip is not None:
            self.card_zip_input.send_keys(card_zip)
        self._driver.switch_to.default_content()

    #   Commented due to the bug https://stackoverflow.com/questions/52608566/selenium-send-keys-incorrect-order-in-stripe-credit-card-input
    #
    # def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
    #     Select(self.credit_card_list).select_by_visible_text("New Card")
    #     wait(lambda: self.stripe.is_enabled())
    #     self._driver.switch_to.frame(self.stripe)
    #     wait(lambda: self.card_number_input.is_enabled())
    #     self.card_number_input.clear()
    #     wait(lambda: self.card_number_input.is_enabled())
    #     sleep(2)
    #     self.card_number_input.send_keys(card_number)
    #     self.card_date_input.send_keys(card_date)
    #     self.card_cvc_input.send_keys(card_cvc)
    #     if card_zip is not None:
    #         self.card_zip_input.send_keys(card_zip)
    #     self._driver.switch_to.default_content()

    def select_saved_card(self, saved_card):
        Select(self.credit_card_list).select_by_visible_text(saved_card)

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def get_options(self, web_element):
        return Select(web_element).options

    def wait_pop_up_closed(self):
        WebDriverWait(self._driver, 10).until(EC.staleness_of(self.discount_pop_up))
