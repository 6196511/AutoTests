from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class BranchPage(BasePage):
    url = 'https://dev.godo.io/branch.aspx'
    add_branch_button = Find(by=By.XPATH, value="//button[@id='addBranch']")
    branch_name_field = Find(by=By.XPATH, value="//input[@id='branch_name']")
    timezone_list = Find(by=By.XPATH, value="//select[@id='timezone_id']")
    branch_address1 = Find(by=By.XPATH, value="//input[@id='branch_address_1']")
    branch_address2 = Find(by=By.XPATH, value="//input[@id='branch_address_2']")
    country_list = Find(by=By.XPATH, value="//select[@id='branch_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='branch_state']")
    branch_city = Find(by=By.XPATH, value="//input[@id='branch_city']")
    branch_zip = Find(by=By.XPATH, value="//input[@id='branch_zipcode']")
    branch_email = Find(by=By.XPATH, value="//input[@id='branch_email']")
    branch_phone1 = Find(by=By.XPATH, value="//input[@id='branch_phone_1']")
    branch_phone2 = Find(by=By.XPATH, value="//input[@id='branch_phone_2']")
    save_button = Find(by=By.XPATH, value="//button[@id='submitbranch']")
    branch_names = Finds (by=By.XPATH, value="//*[@id='dtBranch']/tbody/tr/td[1]")
    branch_edit_buttons = Finds(by=By.XPATH, value="//i[@class='fa fa-edit']")
    delete_buttons = Finds(by=By.XPATH, value="//i[@class='fa fa-remove']")
    alert_message = Find(by=By.XPATH, value="//label[@id='errormsg']")

class CustomerBranchPage(BasePage):
    url = 'https://dev.godo.io/customer_facing.aspx?Company=98365f3f-357e-43ff-be86-d113ea4aa624'
    branch_tickets = Finds(by=By.XPATH, value="//div[contains(@class, 'activityBox companybranch')]")