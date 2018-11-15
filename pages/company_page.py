from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class EditCompanyPage(BasePage):
    url = 'https://ci004.godo.io/company_information.aspx'
    internal_pwd_field = Find(by=By.XPATH, value="//input[@name='internal_password']")
    company_name_field = Find(by=By.XPATH, value="//input[@id='company_name']")
    company_email = Find(by=By.XPATH, value="//input[@id='branch_master_email']")
    username_field = Find(by=By.XPATH, value="//input[@id='administrator_username']")
    pwd_field = Find(by=By.XPATH, value="//input[@id='administrator_password']")
    phone_field = Find(by=By.XPATH, value="//input[@id='branch_master_phone_1']")
    city_field = Find(by=By.XPATH, value="//input[@id='branch_master_city']")
    country_list = Find(by=By.XPATH, value="//select[@id='branch_master_country']")
    zip_field = Find(by=By.XPATH, value="//input[@id='branch_master_zipcode']")
    time_zone_list = Find(by=By.XPATH, value="//select[@id='branch_master_timezone']")
    state_list = Find(by=By.XPATH, value="//select[@id='branch_master_state']")
    address1_field = Find(by=By.XPATH, value="//input[@id='branch_master_address_1']")
    addcompany_button = Find(by=By.XPATH, value="//button[@id='id_submit']")

class AddCompanyPage(BasePage):
    url = 'https://ci004.godo.io/sa_addNewCompany.aspx'
    internal_pwd_field = Find(by=By.XPATH, value="//input[@name='internal_password']")
    company_name_field = Find(by=By.XPATH, value="//input[@id='company_name']")
    company_email = Find(by=By.XPATH, value="//input[@id='branch_master_email']")
    username_field = Find(by=By.XPATH, value="//input[@id='administrator_username']")
    pwd_field = Find(by=By.XPATH, value="//input[@id='administrator_password']")
    phone_field = Find(by=By.XPATH, value="//input[@id='branch_master_phone_1']")
    city_field = Find(by=By.XPATH, value="//input[@id='branch_master_city']")
    country_list = Find(by=By.XPATH, value="//select[@id='branch_master_country']")
    zip_field = Find(by=By.XPATH, value="//input[@id='branch_master_zipcode']")
    time_zone_list = Find(by=By.XPATH, value="//select[@id='branch_master_timezone']")
    state_list = Find(by=By.XPATH, value="//select[@id='branch_master_state']")
    address1_field = Find(by=By.XPATH, value="//input[@id='branch_master_address_1']")
    addcompany_button = Find(by=By.XPATH, value="//button[@id='id_submit']")
