from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from waiver import WaiverAddPage
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO595(BaseTest):
    def test_595(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=WaiverAddPage()
        page.open()
        page.add_waiver_button.click()
        page.ok_confirm_button.click()
        time.sleep(7)
        page.logo_checkbox.click()
        NewWaiverName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.waiver_title.send_keys(NewWaiverName)
        NewWaiverHeader = "TestHeader"
        page.text_fields[0].send_keys(NewWaiverHeader)
        page.next_button.click()
        # select = Select(page.field_add)
        # NewFieldAdd = "Date of Signing"
        # select.select_by_visible_text(NewFieldAdd)
        # page.insert_button.click()
        time.sleep(8)
        page.text_fields[1].send_keys ('By signing this waiver agreement, _________________ agrees to the following terms: Assumption of Risk. PandaTip: This waiver agreement template protects you by ensuring that your client understands that they are participating in your event at their own risk, and that all risk and liability rests with them. The Client agrees that their participation in [Event.Name] is voluntary. Furthermore, the Client agrees to assume any risk associated with participating in the event, and releases [Sender.Company] from any and all claims of loss or damage that may arise during the Client’s participation. Such releases are without limitation, and include attorneys’ fees, personal injury, property damage, and any other losses or damages suffered by the Client.')
        page.next1_button.click()
        NewWaiverRefer = "Dear Friends"
        page.refer_field.send_keys(NewWaiverRefer)
        page.save_button.click()
        time.sleep(10)
        select = Select(page.entries_per_page)
        select.select_by_visible_text('100')
        time.sleep(2)
        L=[]
        for i in range(0, len(page.waiver_names)):
            L.append(page.waiver_names[i].get_attribute("textContent"))
        assert (NewWaiverName+' ') in L
        for i in range (0, len(page.waiver_entries)):
            if (NewWaiverName+' ') in page.waiver_name[i].get_attribute("textContent"):
                assert page.count_value[i].get_attribute("textContent") == '0'

