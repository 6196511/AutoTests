from selenium.webdriver.common.by import By
from webium import BasePage, Find


class CustomerListPage(BasePage):
    url = 'https://dev.godo.io/customer_list.aspx'
    add_customer_button = Find(by=By.XPATH, value="//a[@ng-click='vm.openAddCustomerModal()']")
    country_list = Find(by=By.XPATH, value="//select[@id='customer_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='customer_state']")
    customer_zip = Find(by=By.XPATH, value="//input[@id='customer_zipCode']")




