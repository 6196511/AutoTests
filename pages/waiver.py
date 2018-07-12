from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds
from selenium.webdriver.remote.webelement import WebElement

# class WaiverEntry(WebElement):
#     # waiver_names1 = Find(by=By.XPATH, value="//*[@id='dtWaivers']/tbody/tr/td[2]/span")
#     waiver_name = Find(by=By.XPATH, value="//*[@id='dtWaivers']/tbody/tr/td[2]/span")
#     edit_button = Find(by=By.XPATH, value="//i[@class='fa fa-edit']")
#     search_button = Find(by=By.XPATH, value="//i[@class='fa fa-eye']")


class WaiverAddPage(BasePage):

    url = 'https://dev.godo.io/waiver.aspx'
    add_waiver_button = Find(by=By.XPATH, value="//button[text()='New Waiver']")
    ok_confirm_button = Find(by=By.XPATH, value="//button[text()='Ok']")
    logo_checkbox = Find(by=By.XPATH, value="//input[@name='chkCompanyLogo']")
    waiver_title = Find(by=By.XPATH, value="//input[@id='waivername']")
    # waiver_header = Find(by=By.XPATH, value="//div[@class='fr-element fr-view']")
    next_button = Find(by=By.XPATH, value="//button[text()='Next >']")
    prev_button = Find(by=By.XPATH, value="//button[text()='< Previous']")
    field_add = Find(by=By.XPATH, value="//select[@id='defFields']")
    insert_button = Find(by=By.XPATH, value="//button[text()=' Insert']")
    # body_field = Find(by=By.XPATH, value="//div[@class='fr-wrapper']")
    refer_field = Find(by=By.XPATH, value="//input[@id='txtCustomerWording']")
    next1_button = Find(by=By.XPATH, value="//button[@ng-click='vm.showParticipants()']")
    save_button = Find(by=By.XPATH, value="//button[@id='btnSaveWaiver']")
    entries_per_page = Find(by=By.XPATH, value="//select[@name='dtWaivers_length']")
    waiver_names = Finds(by=By.XPATH, value="//span[@class='ng-binding']")
    waiver_entries = Finds(by=By.XPATH, value="//tr[@ng-repeat='waiver in vm.companyWaivers']")
    count_value = Finds(by=By.XPATH, value="//span[@ng-bind='waiver.activityCount']")
    waiver_name = Finds(by=By.XPATH, value="//*[@id='dtWaivers']/tbody/tr/td[2]/span")
    preview_buttons = Finds(by=By.XPATH, value="//i[@class='fa fa-eye']")
    edit_buttons = Finds(by=By.XPATH, value="//i[@class='fa fa-edit']")
    text_fields = Finds(by=By.XPATH, value="//div[@class='fr-element fr-view']")
    minors_check = Find(by=By.XPATH, value="//input[@id='includeMinor']")
    guardian_message = Find(by=By.XPATH, value="//textarea[@id='guardianVerbiage']")
    firstname_check = Find(by=By.XPATH, value="//input[@id='contactEmail']")
    lastrstname_check = Find(by=By.XPATH, value="//input[@id='lastNameCheck']")
    date_check = Find(by=By.XPATH, value="//input[@id='dateBirthCheck']")
    email_check = Find(by=By.XPATH, value="//input[@id='contactEmail']")
    gender_check = Find(by=By.XPATH, value="//input[@id='genderCheck']")
    phone_check = Find(by=By.XPATH, value="//input[@id='phoneCheck']")
    waiver_status = Finds(by=By.XPATH, value="//*[@id='dtWaivers']/tbody/tr/td[3]/span")
    waiver_checkbox = Finds(by=By.XPATH, value="//input[@ng-click='vm.displaySelected(waiver);']")
    search_activities_field = Find(by=By.XPATH, value="//input[@type='search']")

    header_view = Find(by=By.XPATH, value="//div[@ng-bind-html='vm.trustAsHtml(vm.waiver.header)']")
    body_view = Find(by=By.XPATH, value="//div[@ng-bind-html='vm.trustAsHtml(vm.waiver.waiverAdult)']")
    first_name_view = Find(by=By.XPATH, value="//input[@ng-model='vm.ticket.firstName']")
    last_name_view = Find(by=By.XPATH, value="//input[@ng-model='vm.ticket.lastName']")
    date_birth_view = Find(by=By.XPATH, value="//input[@ng-model='vm.ticket.birthday']")
    gender_view = Find(by=By.XPATH, value="//select[@id='gender']")
    phone_view = Find(by=By.XPATH, value="//input[@id='phone']")
    emal_view = Find(by=By.XPATH, value="//input[@id='cemail']")
    guard_message_view = Find(by=By.XPATH, value="//div[@ng-bind-html='vm.trustAsHtml(vm.waiver.guardMessage)']")

    adult_button = Find(by=By.XPATH, value="//button[@id='btnAdult']")
    minor_button = Find(by=By.XPATH, value="//button[@id='btnMinor']")

    # adult_button = Find(by=By.XPATH, value="//button[@id = 'btnAdult'and namespace-uri()='http://www.w3.org/1999/xhtml']")
