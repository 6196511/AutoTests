from selenium.webdriver.common.by import By
from webium import BasePage, Find


class CustomerListPage(BasePage):
    url = 'https://ci004.godo.io/customer_list.aspx'
    add_customer_button = Find(by=By.XPATH, value="//a[@ng-click='vm.openAddCustomerModal()']")
    first_name_field = Find(by=By.XPATH, value="//input[@id='customer_firstname']")
    last_name_field = Find(by=By.XPATH, value="//input[@id='customer_lastname']")
    address1_field = Find(by=By.XPATH, value="//input[@id='customer_address_1']")
    address2_field = Find(by=By.XPATH, value="//input[@id='customer_address_2']")
    country_list = Find(by=By.XPATH, value="//select[@id='customer_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='customer_state']")
    customer_zip = Find(by=By.XPATH, value="//input[@id='customer_zipCode']")
    phone_field = Find(by=By.XPATH, value="//input[@id='customer_phone_1']")
    email_field = Find(by=By.XPATH, value="//input[@id='customer_email']")
    city_field = Find(by=By.XPATH, value="//input[@id='customer_city']")
    save_button = Find(by=By.XPATH, value="//button[@ng-click='vm.save()']")
    cancel_button = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")
    search_field = Find(by=By.XPATH, value="//input[@id='sSearchWords']")
    search_button = Find(by=By.XPATH, value="//div[@id='dosearch']")
    customer_name_in_list = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[2]/a")
    customer_name_in_list2 = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[2]/a")
    activity_name_in_list = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[5]")
    activity_name_in_list2 = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[5]")
    email_in_list = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/a")
    phone_in_list = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[4]")
    no_matches_list = Find(by=By.XPATH, value="//td[@colspan='8']")
    edit_button = Find(by=By.XPATH, value="//i[@class='md md-edit']")
    customer_name_info = Find(by=By.XPATH, value="//span[@class='ng-binding']")
    email_info = Find(by=By.XPATH, value="//a[@editable-email='vm.customer.email']")
    phone_info = Find(by=By.XPATH, value="//a[@editable-tel='vm.customer.phone']")
    address_info = Find(by=By.XPATH, value="//a[@editable-text='vm.customer.address']")
    city_info = Find(by=By.XPATH, value="//a[@editable-text='vm.customer.city']")
    state_info = Find(by=By.XPATH, value="//a[@editable-text='vm.customer.state']")
    zip_info = Find(by=By.XPATH, value="//a[@editable-text='vm.customer.zipcode']")
    timeline_tickets_title = Find(by=By.XPATH, value="//*[@id='actions']/section/div[1]/div/h5")
    timeline_event = Find(by=By.XPATH, value="//a[@class='dateLinkStyle']")
    timeline_tickets = Find(by=By.XPATH, value="//a[contains(@href,'customerEvent_charge.aspx?customerEvent_id')]")
    timeline_email_title = Find(by=By.XPATH, value="//*[@id='actions']/section/div[2]/div/h5")
    activities_tab_link = Find(by=By.XPATH, value="//a[@href='#activities']")
    activities_tab_title = Find(by=By.XPATH, value="//*[@id='activities']/div/h5/a")
    activities_tickets = Find(by=By.XPATH, value="//p[@class='tab-pane-desc']")




