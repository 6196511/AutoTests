from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage

import time
from creds import admin_login, admin_password


FirstTicketType = "Adult"
SecondTicketType  = "Child"
ThirdTicketType = "Senior"
FourthTicketType = "General"
ActivityName='Price test'
NewActivitySecondTicketPrice = '9.99'
NewActivityThirdTicketPrice ='1.11'
NewActivityFourthTicketPrice ='0.91'



class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO115(BaseTest):

    def test_115(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys(ActivityName)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.first_ticket_type.get_attribute('value')!=FirstTicketType:
            page.first_ticket_type.clear()
            page.first_ticket_type.send_keys(FirstTicketType)
        if  page.is_element_present('second_ticket_type') == False:
            page.add_ticket_type.click()
            page.second_ticket_type.send_keys(SecondTicketType)
            page.second_ticket_price.send_keys(NewActivitySecondTicketPrice)
        else:
            if page.second_ticket_type.get_attribute('value')!=SecondTicketType:
                page.second_ticket_type.clear()
                page.second_ticket_type.send_keys(SecondTicketType)
                page.second_ticket_price.clear()
                page.second_ticket_price.send_keys(NewActivitySecondTicketPrice)
        if  page.is_element_present('third_ticket_type') == False:
            page.add_ticket_type.click()
            page.third_ticket_type.send_keys(ThirdTicketType)
            page.third_ticket_price.send_keys(NewActivityThirdTicketPrice)
        else:
            if page.third_ticket_type.get_attribute('value')!=ThirdTicketType:
                page.third_ticket_type.clear()
                page.third_ticket_type.send_keys(ThirdTicketType)
                page.third_ticket_price.clear()
                page.third_ticket_price.send_keys(NewActivityThirdTicketPrice)
        if  page.is_element_present('fourth_ticket_type') == False:
            page.add_ticket_type.click()
            page.fourth_ticket_type.send_keys(FourthTicketType)
            page.fourth_ticket_price.send_keys(NewActivityFourthTicketPrice)
        else:
            if page.fourth_ticket_type.get_attribute('value')!=FourthTicketType:
                page.fourth_ticket_type.clear()
                page.fourth_ticket_type.send_keys(FourthTicketType)
                page.fourth_ticket_price.clear()
                page.fourth_ticket_price.send_keys(NewActivityFourthTicketPrice)
        FirstTicketPrice = page.first_ticket_price.get_attribute('value')
        SecondTicketPrice = page.second_ticket_price.get_attribute('value')
        ThirdTicketPrice = page.third_ticket_price.get_attribute('value')
        FourthTicketPrice = page.fourth_ticket_price.get_attribute('value')
        page.delete_fourth_ticket_type.click() #STEP3
        assert page.is_element_present('fourth_ticket_type') == False
        page.save_button.click()#STEP4
        time.sleep(5)
        page = ActivityHubPage()
        page.search_activity_field.send_keys(ActivityName)#STEP5
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.is_element_present('fourth_ticket_type') == False
        assert page.first_ticket_type.get_attribute('value')==FirstTicketType
        assert page.second_ticket_type.get_attribute('value')==SecondTicketType
        assert page.third_ticket_type.get_attribute('value')==ThirdTicketType
        assert page.first_ticket_price.get_attribute('value')==FirstTicketPrice
        assert page.second_ticket_price.get_attribute('value')==SecondTicketPrice
        assert page.third_ticket_price.get_attribute('value')==ThirdTicketPrice
        page.delete_third_ticket_type.click()#STEP6
        page.delete_first_ticket_type.click()
        assert page.is_element_present('third_ticket_type') == False
        assert page.is_element_present('second_ticket_type') == False
        assert page.first_ticket_type.get_attribute('value')==SecondTicketType
        assert page.first_ticket_price.get_attribute('value') == SecondTicketPrice
        page.save_button.click()  # STEP7
        time.sleep(5)
        page = ActivityHubPage()
        page.search_activity_field.send_keys(ActivityName)  # STEP8
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.is_element_present('fourth_ticket_type') == False
        assert page.is_element_present('third_ticket_type') == False
        assert page.is_element_present('second_ticket_type') == False
        assert page.first_ticket_type.get_attribute('value')==SecondTicketType
        assert page.first_ticket_price.get_attribute('value') == SecondTicketPrice
        page.first_ticket_type.clear() #STEP9
        page.first_ticket_price.clear()
        assert page.first_ticket_type.get_attribute('value')==''
        assert page.first_ticket_price.get_attribute('value') == ''
        page.save_button.click() #STEP10
        time.sleep(10)
        assert page.ticket_type_alert.is_displayed()
        assert page.ticket_price_alert.is_displayed()