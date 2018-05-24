from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webium import BasePage, Find
from webium.wait import wait


class TextField(WebElement):
    @property
    def text(self):
        return self.get_attribute('value')


class CustomerCertPage(BasePage):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    certificate_type = Find(by=By.XPATH, value="//select[@id='giftType']")
    email = Find(by=By.XPATH, value="//input[@id='giftEmail']")
    first_name = Find(by=By.XPATH, value="//input[@id='giftFirstName']")
    last_name = Find(by=By.XPATH, value="//input[@id='giftLastName']")
    activity = Find(by=By.XPATH, value="//select[@id='ddlActivity']")
    first_tickets_type = Find(by=By.XPATH, value="//div[@id='divActivityDetials']/div[1]//input")
    second_tickets_type = Find(by=By.XPATH, value="//div[@id='divActivityDetials']/div[2]//input")
    third_tickets_type = Find(by=By.XPATH, value="//div[@id='divActivityDetials']/div[3]//input")
    initial_amount = Find(TextField, by=By.XPATH, value="//input[@id='giftInitialAmount']")
    booking_fee = Find(TextField, by=By.XPATH, value="//div[@id='divamountSummary']/div[1]//input")
    total_amount = Find(TextField, by=By.XPATH, value="//div[@id='divamountSummary']/div[2]//input")
    empty_space = Find(by=By.XPATH, value="//h4[text()='Step 1/2: Gift Type and Initial Amount ']")

    next_step_button = Find(by=By.XPATH, value="//div[@id='giftinforbtnDiv']/input")

    # Payment page

    full_charge = Find(TextField, by=By.XPATH, value="//input[@id='charge_full_amount']")
    stripe = Find(by=By.XPATH, value="//iframe[@name='__privateStripeFrame3']")
    card_number_input = Find(by=By.XPATH, value="//input[@name='cardnumber']")
    card_date_input = Find(by=By.XPATH, value="//input[@name='exp-date']")
    card_cvc_input = Find(by=By.XPATH, value="//input[@name='cvc']")
    card_zip_input = Find(by=By.XPATH, value="//input[@name='postal']")
    payment_notification = Find(by=By.XPATH, value="//span[@id='CcErrorMsg']")
    pay_button = Find(by=By.XPATH, value="//button[@id='giftCardPay_Btn']")

    # Summary Details page

    customer = Find(by=By.XPATH, value="//span[@id='summarynamelbl']")
    email_sd = Find(by=By.XPATH, value="//span[@id='summaryEmaillbl']")
    amount = Find(by=By.XPATH, value="//span[@id='summaryAmount']")
    gift_code = Find(by=By.XPATH, value="//span[@id='summaryGiftPurchaseCode']")

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def enter_cc_info(self, card_number, card_date, card_cvc, card_zip):
        wait(lambda: self.stripe.is_enabled(), timeout_seconds=15)
        self._driver.switch_to.frame(self.stripe)
        wait(lambda: self.card_number_input.is_displayed())
        self.card_number_input.clear()
        self.card_number_input.send_keys(card_number)
        self.card_date_input.send_keys(card_date)
        self.card_cvc_input.send_keys(card_cvc)
        if card_zip is not None:
            self.card_zip_input.send_keys(card_zip)
        self._driver.switch_to.default_content()

    def close_final_alert(self):
        waiting = WebDriverWait(self._driver, 30)
        alert = waiting.until(EC.alert_is_present())
        assert alert.text == "Gift Certificate Code has been sent to your EmailID."
        alert.accept()

    def close_alert(self):
        alert = EC.alert_is_present()
        if alert(self._driver):
            self._driver.switch_to_alert().accept()
