from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
from selenium.webdriver.support.wait import WebDriverWait
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains
from creds import admin_login, admin_password,server, database, username, password
import pyodbc

ActivityNameList = []
ActivityIDList =[]
Activity1 = 'Linked Activity A'
Activity2 = 'Linked Activity B'
Activity3 = 'Linked Activity C'
Activity4 = 'Linked Activity D'

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO510_512(BaseTest):
    def test_510(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys(Activity1)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
        time.sleep(7)
        select = Select(page.first_linked_activity)
        time.sleep(5)
        select.select_by_visible_text(Activity2)
        page.save_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity1)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        page.cancel_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity2)
        time.sleep(5)
        text = page.activity_title.get_attribute("textContent")
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1

    def test_512(self):
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys(Activity3)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
            page.save_button.click()
        page=ActivityHubPage()
        page.open()
        page.search_activity_field.send_keys(Activity4)
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        if page.is_element_present('remove_fourth_linked_activity')==True:
            page.remove_fourth_linked_activity.click()
        if page.is_element_present('remove_third_linked_activity') == True:
            page.remove_third_linked_activity.click()
        if page.is_element_present('remove_second_linked_activity') == True:
            page.remove_second_linked_activity.click()
        if page.is_element_present('remove_first_linked_activity') == True:
            page.remove_first_linked_activity.click()
            page.save_button.click()
        page=ActivityHubPage()#STEP1
        page.open()
        page.search_activity_field.send_keys(Activity3)#STEP2
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        time.sleep(5)
        select.select_by_visible_text(Activity4)#STEP3
        page.save_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity1)#STEP4
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.second_linked_activity)# STEP5
        time.sleep(5)
        select.select_by_visible_text(Activity4)
        #TOOLTIP TO ADD
        actions = ActionChains(get_driver())
        actions.move_to_element(page.tooltip_linked_activity).perform()
        time.sleep(3)
        assert page.tooltip_linked_activity_msg.get_attribute('textContent') ==\
               "Activity '"+''.join(Activity4)+"' is linked with 1 other activity. After saving changes your activity will be linked to all activities already linked with '"+''.join(Activity4)+"'."
        page.save_button.click()# STEP6
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity1)# STEP7
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity3
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP8
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity2)# STEP9
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity3
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP10
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity3)# STEP11
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity4
        page.cancel_button.click()# STEP12
        page = ActivityHubPage()
        page.search_activity_field.send_keys(Activity4)# STEP13
        time.sleep(5)
        page.activity_actions.click()
        page.edit_activity.click()
        page = AddEditActivityPage()
        time.sleep(15)
        select = Select(page.first_linked_activity)
        assert select.first_selected_option.text == Activity1
        select = Select(page.second_linked_activity)
        assert select.first_selected_option.text == Activity2
        select = Select(page.third_linked_activity)
        assert select.first_selected_option.text == Activity3