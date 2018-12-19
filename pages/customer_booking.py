from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from webium.wait import wait
from webium import BasePage, Find, Finds


class TimeList(WebElement):
    available_time = Find(by=By.CLASS_NAME, value="timePill-left")
    button = Find(by=By.CLASS_NAME, value="timePill-right")


class CustomerBookingPage(BasePage):

    def __init__(self, **kwargs):
        super(CustomerBookingPage, self).__init__(**kwargs)

    # Step 1/5: Pick Tickets inputs.

    first_plus_button = Find(by=By.XPATH,
                             value="//div[@class='row content'][1]//button[@class='upButton']")
    second_plus_button = Find(by=By.XPATH,
                             value="//div[@class='row content'][2]//button[@class='upButton']")
    third_plus_button = Find(by=By.XPATH,
                             value="//div[@class='row content'][3]//button[@class='upButton']")
    fourth_plus_button = Find(by=By.XPATH,
                             value="//div[@class='row content'][4]//button[@class='upButton']")

    # Titles under the pictures.
    first_tickets_name = Find(by=By.XPATH, value="//div[@class='row content'][1]//div[@class='ticket-name']")
    second_tickets_name = Find(by=By.XPATH, value="//div[@class='row content'][2]//div[@class='ticket-name']")
    third_tickets_name = Find(by=By.XPATH, value="//div[@class='row content'][3]//div[@class='ticket-name']")
    fourth_tickets_name = Find(by=By.XPATH, value="//div[@class='row content'][4]//div[@class='ticket-name']")

    # Current tickets table.
    current_tickets_first_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[1]")
    current_tickets_second_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[2]")
    current_tickets_third_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[3]")
    current_tickets_fourth_row = Find(by=By.XPATH, value="//div[@class='ticketDetails']/p[4]")
    next_button_1 = Find(by=By.XPATH, value="//button[@id='ticketBookbtn']")

    # Step 2/5: Choose Date.

    calendar = Find(by=By.ID, value="datepicker")
    datepicker = Finds(by=By.XPATH, value="//div[@class='ui-datepicker-group ui-datepicker-group-first']//td" +
                                          "[contains(@class, 'undefined') and not(contains(@class, 'disabled'))]")
    next_button_2 = Find(by=By.XPATH, value="//button[@id='calenderbtn']")

    # Step 3/5: Choose Time.

    available_time_list = Finds(TimeList, by=By.XPATH, value="//div[@class='timePill']")
    next_button_3 = Find(by=By.XPATH, value="//button[@id='btneventSelect']")

    # Step 4/5: Your Info.

    first_name_input = Find(by=By.XPATH, value="//input[@id='contactFirstName']")
    last_name_input = Find(by=By.XPATH, value="//input[@id='contactLastName']")
    phone_input = Find(by=By.XPATH, value="//input[@id='contactPhone']")
    email_input = Find(by=By.XPATH, value="//input[@id='contactEmail']")
    zip_input = Find(by=By.XPATH, value="//input[@id='contactZipCode']")
    empty_space_fourth_page = Find(by=By.XPATH, value="//h4[text()='Step 4: Your Info']")
    question_inputs = Finds(by=By.XPATH, value="//input[contains(@class,'question-input')]")
    next_button_4 = Find(by=By.XPATH, value="//button[@id='contact-info-btn']")

    # Step 5: Add-ons

    addons_page = Find(by=By.XPATH, value="//div[@id='addons']")
    next_button_5 = Find(by=By.XPATH, value="//button[@id='addon-btn']")

    # Final Step: Checkout

    promo_code_input = Find(by=By.XPATH, value="//input[@id='discount_code']")
    promo_code_button = Find(by=By.XPATH, value="//input[@id='discountBtnCode']")
    gift_certificate_input = Find(by=By.XPATH, value="//input[@id='gift_certificate']")
    gift_certificate_button = Find(by=By.XPATH, value="//input[@id='redeemBtnCode']")
    discount_pop_up = Find(by=By.XPATH, value="//div[@class='bootbox-body']")
    discount_pop_up_ok_button = Find(by=By.XPATH, value="//button[@class='btn btn-primary']")
    stripe = Find(by=By.XPATH, value="//iframe[@name='__privateStripeFrame3']")
    card_number_input = Find(by=By.XPATH, value="//input[@name='cardnumber']")
    card_date_input = Find(by=By.XPATH, value="//input[@name='exp-date']")
    card_cvc_input = Find(by=By.XPATH, value="//input[@name='cvc']")
    card_zip_input = Find(by=By.XPATH, value="//input[@name='postal']")
    payment_notification = Find(by=By.XPATH, value="//span[@id='CcErrorMsg']")
    next_button_6 = Find(by=By.XPATH, value="//button[@id='submit-button']")

    # Information on the page.

    checkout_activity = Find(by=By.XPATH, value="//div[@class='row lowBlue']//h2")
    checkout_date = Find(by=By.XPATH, value="//p[@class='tourDate']")
    checkout_time = Find(by=By.XPATH, value="//p[@class='tourTime']")
    checkout_first_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[1]")
    checkout_second_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[2]")
    checkout_third_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[3]")
    checkout_fourth_tickets = Find(by=By.XPATH, value="//div[@id='tckTypes']/p[4]")
    tickets_cost = Find(by=By.XPATH, value="//div[@id='ticketbaseprice']")
    tax = Find(by=By.XPATH, value="//div[@id='taxesandfees']")
    checkout_discount = Find(by=By.XPATH, value="//div[@id='payDiscount-amount']")
    total_price = Find(by=By.XPATH, value="//div[@id='tickettotalprice']")

    # Summary Details.

    customer_information = Find(by=By.XPATH, value="//div[@id='summarynamelbl']")
    zip_information = Find(by=By.XPATH, value="//div[@id='summaryAddresslbl']")
    phone_information = Find(by=By.XPATH, value="//div[@id='summaryPhonelbl']")
    email_information = Find(by=By.XPATH, value="//div[@id='summaryEmaillbl']")
    ticket_total = Find(by=By.XPATH, value="//div[@id='ticketTotallbl']")
    booking_fee = Find(by=By.XPATH, value="//div[@id='bookingFeeslbl']")
    discount = Find(by=By.XPATH, value="//div[@id='discountlbl']")
    tax_information = Find(by=By.XPATH, value="//div[@id='taxlbl']")
    grand_total = Find(by=By.XPATH, value="//div[@id='subTotallbl']")

    def click_tickets(self, button, number):
        for item in range(int(number)):
            button.click()

    def pick_this_time(self, time):
        wait(lambda: len(self.available_time_list) > 0)
        for item in self.available_time_list:
            label = item.available_time.text
            if label.startswith(time):
                item.button.click()
                break

    def get_time_list(self):
        wait(lambda: len(self.available_time_list) > 0)
        time_list = []
        for item in self.available_time_list:
            time_list.append(item.available_time.text)
        return time_list

    def click_date(self, day):
        for item in self.datepicker:
            if item.text == day:
                item.click()
                break

    def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
        wait(lambda: self.stripe.is_enabled())
        self._driver.switch_to.frame(self.stripe)
        wait(lambda: self.card_number_input.is_enabled())
        attempts = 20
        card_number_size = 16
        for attempt in range(1, attempts):
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
    #     wait(lambda: self.stripe.is_enabled())
    #     self._driver.switch_to.frame(self.stripe)
    #     wait(lambda: self.card_number_input.is_displayed())
    #     self.card_number_input.clear()
    #     self.card_number_input.send_keys(card_number)
    #     self.card_date_input.send_keys(card_date)
    #     self.card_cvc_input.send_keys(card_cvc)
    #     if card_zip is not None:
    #         self.card_zip_input.send_keys(card_zip)
    #     self._driver.switch_to.default_content()

    def scroll_down(self):
        self._driver.execute_script("$('html,body').animate({scrollTop: document.body.scrollHeight},\"fast\");")

    def addons_present(self):
        style = self.addons_page.get_attribute("style")
        if style == "display: none;":
            return False
        else:
            return True

    def close_alert(self):
        alert = EC.alert_is_present()
        if alert(self._driver):
            self._driver.switch_to_alert().accept()
