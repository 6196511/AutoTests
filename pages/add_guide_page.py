from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from waiting import wait
from webium import BasePage, Find, Finds


class TextField(WebElement):
    @property
    def text(self):
        return self.get_attribute('value')


class AddGuidePage(BasePage):

    username = Find(TextField, by=By.XPATH, value="//div[label/text()='Username ']/input")
    password = Find(TextField, by=By.XPATH, value="//div[label/text()='Password ']/input")
    first_name = Find(TextField, by=By.XPATH, value="//div[label/text()='First Name ']/input")
    last_name = Find(TextField, by=By.XPATH, value="//div[label/text()='Last Name ']/input")
    email = Find(TextField, by=By.XPATH, value="//div[label/text()='Email ']/input")
    timezone = Find(TextField, by=By.XPATH, value="//select[@ng-model='vm.selectedTimezone']")
    phone_number = Find(TextField, by=By.XPATH, value="//div[label/text()='Phone Number ']/input")
    secondary_phone_number = Find(TextField, by=By.XPATH, value="//div[label/text()='Secondary Contact Phone ']/input")
    emergency_contact = Find(TextField, by=By.XPATH, value="//div[label/text()='Emergency Contact']/input")
    hire_date = Find(TextField, by=By.XPATH, value="//div[label/text()='Hire Date']/input")
    end_date = Find(TextField, by=By.XPATH, value="//div[label/text()='End Date']/input")
    bank_name = Find(TextField, by=By.XPATH, value="//div[label/text()='Bank Name']/input")
    account_type = Find(TextField, by=By.XPATH, value="//div[label/text()='Account Type']/select")
    bank_routing_number = Find(TextField, by=By.XPATH, value="//div[label/text()='Bank Routing Number']/input")
    account_number = Find(TextField, by=By.XPATH, value="//div[label/text()='Account Number']/input")
    pay_rate_type = Find(TextField, by=By.XPATH, value="//div[label/text()='Pay Rate Type ']/select")
    trained_activity = Find(by=By.XPATH, value="//div[@name='itemForm'][1]//select")
    trained_activity_remove = Find(by=By.XPATH, value="//div[@name='itemForm'][1]//button")
    save_button = Find(by=By.XPATH, value="//button[contains(text(),'Save')]")
    cancel_button = Find(by=By.XPATH, value="//button[text()='Cancel']")
    empty_space = Find(by=By.XPATH, value="//label")

    import_guide_button = Find(by=By.XPATH, value="//button[text()='Import Guide']")
    i_username = Find(by=By.XPATH, value="//div[@class='modal-content']//input[@placeholder='Username']")
    i_pay_type = Find(by=By.XPATH, value="//div[@class='modal-content']//select")
    i_rate = Find(by=By.XPATH, value="//div[@class='modal-content']//input[@placeholder='Enter Pay Rate']")
    i_close_button = Find(by=By.XPATH, value="//div[@class='modal-content']//button[text()='Close']")
    i_import_button = Find(by=By.XPATH, value="//div[@class='modal-content']//button[text()='Import']")

    error_messages = Finds(by=By.XPATH, value="//div[@class='formErrorContent']")

    bootstrap_alert = Find(by=By.XPATH, value="//div[contains(@class, 'alert')]/span")

    def verify_alert(self, wording):
        waiting = WebDriverWait(self._driver, 15)
        alert = waiting.until(EC.alert_is_present())
        assert alert.text == wording
        alert.accept()

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def get_selected_value(self, web_element):
        return Select(web_element).first_selected_option.text

    def select_trained_activity(self, activity):
        Select(self.trained_activity).select_by_visible_text(activity)

    def wait_redirection(self):
        old_url = self._driver.current_url
        wait(lambda: self._driver.current_url != old_url)
