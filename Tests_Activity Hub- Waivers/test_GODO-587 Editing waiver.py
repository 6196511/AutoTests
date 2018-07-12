from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from waiver import WaiverAddPage
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
from selenium.webdriver.support.wait import WebDriverWait
from time import localtime, strftime

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO587(BaseTest):
    def test_587(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=WaiverAddPage()
        page.open()
        time.sleep(5)
        select = Select(page.entries_per_page)
        select.select_by_visible_text('100')
        time.sleep(2)
        WaiverOld = []
        for i in range (0, len(page.waiver_entries)):
            if ('AutoTest_' in page.waiver_name[i].get_attribute("textContent")):
                print(page.waiver_name[i].get_attribute("textContent"))
                WaiverOld.append(page.waiver_name[i].get_attribute("textContent"))
                page.preview_buttons[i].click()
                break
        print(WaiverOld)
        WebDriverWait(get_driver(), 10).until(lambda d: len(d.window_handles) == 2)
        get_driver().switch_to_window(get_driver().window_handles[1])
        time.sleep(5)
        OldHeader = page.header_view.get_attribute("textContent")
        print(OldHeader)
        OldBody = page.body_view.get_attribute("textContent")
        print(OldBody)
        page.adult_button.click()
        time.sleep(5)
        get_driver().switch_to_window(get_driver().window_handles[0])
        select = Select(page.entries_per_page)
        select.select_by_visible_text('100')
        time.sleep(2)
        for i in range (0, len(page.waiver_entries)):
            if ('AutoTest_' in page.waiver_name[i].get_attribute("textContent")):
                page.edit_buttons[i].click()
                break
        time.sleep(5)
        assert page.waiver_title.get_attribute("value")+' '==WaiverOld[0]
        assert page.text_fields[0].get_attribute("textContent")==OldHeader
        page.next_button.click()
        time.sleep(5)
        assert page.text_fields[1].get_attribute("textContent")==OldBody
        page.prev_button.click()
        NewWaiverName = ("TestEdit_" + ''.join(choice(digits) for i in range(4)))
        page.waiver_title.clear()
        page.waiver_title.send_keys(NewWaiverName)
        NewWaiverHeader = "EditedHeader"
        page.text_fields[0].clear()
        page.text_fields[0].send_keys(NewWaiverHeader)
        page.next_button.click()
        time.sleep(8)
        page.text_fields[1].clear()
        NewWaiverBody = 'EDITED WAIVER BODY'
        page.text_fields[1].send_keys(NewWaiverBody)
        select = Select(page.field_add)
        NewFieldAdd = "Date of Signing"
        select.select_by_visible_text(NewFieldAdd)
        page.insert_button.click()
        page.next1_button.click()
        NewWaiverRefer = "Dear Sir/Madam"
        page.refer_field.clear()
        page.refer_field.send_keys(NewWaiverRefer)
        page.minors_check.click()
        page.guardian_message.clear()
        NewGuardianMessage = 'EDITED Parent(s) or court-appointed legal guardian(s) must sign for any participating minor (those under 18 years of age) and agree that they and the minor are subject to all the terms of this document, as set forth above. EDITED'
        page.guardian_message.send_keys(NewGuardianMessage)
        page.date_check.click()
        page.email_check.click()
        page.gender_check.click()
        page.phone_check.click()
        page.save_button.click()
        time.sleep(10)
        select = Select(page.entries_per_page)
        select.select_by_visible_text('100')
        time.sleep(2)
        WaiverEdited = []
        for i in range (0, len(page.waiver_entries)):
            if (NewWaiverName in page.waiver_name[i].get_attribute("textContent")):
                print(page.waiver_name[i].get_attribute("textContent"))
                WaiverEdited.append(page.waiver_name[i].get_attribute("textContent"))
                page.preview_buttons[i].click()
                break
        time.sleep(5)
        WebDriverWait(get_driver(), 10).until(lambda d: len(d.window_handles) == 3)
        get_driver().switch_to_window(get_driver().window_handles[2])
        time.sleep(5)
        assert NewWaiverHeader == page.header_view.get_attribute("textContent")
        print(OldHeader)
        datetime = strftime("%m/%d/%Y, %#I:%M:", localtime())
        assert NewWaiverBody+datetime in page.body_view.get_attribute("textContent")
        page.adult_button.click()
        time.sleep(5)
        assert page.is_element_present('first_name_view') == True
        assert page.is_element_present('last_name_view') == True
        assert page.is_element_present('date_birth_view') == True
        assert page.is_element_present('gender_view') == True
        assert page.is_element_present('phone_view') == True
        assert page.is_element_present('emal_view') == True
        page.minor_button.click()
        assert page.is_element_present('first_name_view') == True
        assert page.is_element_present('last_name_view') == True
        assert page.is_element_present('date_birth_view') == True
        assert page.is_element_present('gender_view') == True
        assert page.is_element_present('phone_view') == True
        assert page.is_element_present('emal_view') == True
        assert page.guard_message_view.get_attribute("textContent") == NewGuardianMessage


