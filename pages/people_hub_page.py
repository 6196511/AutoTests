from selenium.webdriver.common.by import By
from webium import BasePage, Find


class PeopleHubPage(BasePage):
    url = 'https://dev.godo.io/user_hub.aspx'
    add_guide_button = Find(by=By.XPATH, value="//h2[text()='Add Guide']")
    your_customer_button = Find(by=By.XPATH, value="//h2[text()='Your Customers']")

    search_input = Find(by=By.XPATH, value="//input[@placeholder='Start typing to search']")
    name = Find(by=By.XPATH, value="//div[@ng-controller='GuideCompanyExController as vm']//tr[1]/td[1]")
    pay_rate = Find(by=By.XPATH, value="//div[@ng-controller='GuideCompanyExController as vm']//tr[1]/td[2]")
    phone_number = Find(by=By.XPATH, value="//div[@ng-controller='GuideCompanyExController as vm']//tr[1]/td[3]")
    email = Find(by=By.XPATH, value="//div[@ng-controller='GuideCompanyExController as vm']//tr[1]/td[4]")
    view = Find(by=By.XPATH, value="//tr[1]//i[contains(@class, 'fa-eye')]")
    edit = Find(by=By.XPATH, value="//tr[1]//i[contains(@class, 'fa-edit')]")
    key = Find(by=By.XPATH, value="//tr[1]//i[contains(@class, 'fa-key')]")
    delete = Find(by=By.XPATH, value="//tr[1]//i[contains(@class, 'fa-trash')]")

    pop_up = Find(by=By.XPATH, value="//div[contains(@class, 'modal-body')]")
    pop_up_ok_button = Find(by=By.XPATH, value="//div[contains(@class, 'modal-footer')]/button[text()='Ok']")
    pop_up_cancel_button = Find(by=By.XPATH, value="//div[contains(@class, 'modal-footer')]/button[text()='Cancel']")
