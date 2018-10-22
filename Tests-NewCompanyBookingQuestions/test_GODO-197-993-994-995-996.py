from webium.driver import get_driver
from webium.driver import close_driver
from selenium.webdriver.support.ui import Select
import time
from booking_questions import BookingQuestionsPage
from company_page import AddCompanyPage, EditCompanyPage
from creds import internal_pwd
import random
from random import choice
from string import digits
from selenium.webdriver.common.keys import Keys

username_list = []
pwd_list = []
question1_text = 'What is your favourite meal?'
question2_text = 'What is your job?'
question3_text = 'How are you?'
question1edited_text = 'Where are you from?'
question2edited_text = 'What is your favourite drink?'
question3edited_text = 'What is your profession?'

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO197_993_994_995_996(BaseTest):
    def test_197(self):
        get_driver().maximize_window()
        page = AddCompanyPage()
        page.open()
        time.sleep(3)
        page.internal_pwd_field.send_keys(internal_pwd)
        NewCompanyName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.company_name_field.send_keys(NewCompanyName)
        NewCompanyEmail = (NewCompanyName + '@mailinator.com')
        page.company_email.send_keys(NewCompanyEmail)
        NewUserName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        username_list.append(NewUserName)
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        pwd_list.append(NewUserPassword)
        page.pwd_field.send_keys(NewUserPassword)
        NewPhone = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone_field.send_keys(NewPhone)
        city_values = ('Washington','New York','Miami','Los Angeles','Chicago','Dallas')
        NewCity = random.choice(city_values)
        page.city_field.send_keys(NewCity)
        select = Select(page.country_list)
        select.select_by_visible_text('United States')
        select = Select(page.state_list)
        state_values = ('Washington','New York','Florida','Texas','California','Utah')
        NewState = random.choice(state_values )
        select.select_by_visible_text(NewState)
        NewZipCode = ('' + ''.join(choice(digits) for i in range(5)))
        page.zip_field.send_keys(NewZipCode)
        timezone_values = ('Atlantic', 'Eastern', 'Central', 'Mountain', 'Mountain (No DST)', 'Pacific', 'Alaska', 'Hawaii','Hawaii (No DST)')
        NewTimeZone = random.choice(timezone_values)
        select = Select(page.time_zone_list)
        select.select_by_visible_text(NewTimeZone)
        NewAddress ='test123456'
        page.address1_field.send_keys(NewAddress)
        page.addcompany_button.click()
        time.sleep(5)
        page = EditCompanyPage()
        page.open()
        time.sleep(3)
        assert page.company_name_field.get_attribute('value') == NewCompanyName
        assert page.company_email.get_attribute('value') == NewCompanyEmail
        assert page.phone_field.get_attribute('value') == NewPhone
        assert page.city_field.get_attribute('value') == NewCity
        assert page.address1_field.get_attribute('value') == NewAddress
        assert page.zip_field.get_attribute('value') == NewZipCode
        select = Select(page.country_list)
        assert select.first_selected_option.text == 'United States'
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewState
        select = Select(page.time_zone_list)
        assert select.first_selected_option.text == NewTimeZone

    def test_993(self):
        page = BookingQuestionsPage()#STEP2
        page.open()
        page.add_question_plus_button.click()#STEP3
        assert page.question1_title.get_attribute('textContent') == 'Question 1'
        assert page.is_element_present('remove_button') == True
        assert page.question_text[0].get_attribute('value') == ''
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == ''
        assert page.is_element_present('add_option_button') == True
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_question_plus_button') == True
        page.question_text[0].send_keys(question1_text)#STEP4
        select = Select(page.answer_type[0])#STEP5
        select.select_by_visible_text('Text Input')
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[0].get_attribute('textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[0])#STEP6
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will be asked of each ticket buyer.'
        page.add_question_plus_button.click()#STEP7
        assert page.question2_title.get_attribute('textContent') == 'Question 2'
        assert len(page.remove_button)==2
        assert len(page.question_text) == 2
        assert page.question_text[1].get_attribute('value') == ''
        assert len(page.answer_type) == 2
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == ''
        assert len(page.add_option_button) == 2
        assert page.is_element_present('add_option_button') == False
        assert page.add_option_button[1].is_displayed()
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_question_plus_button') == True
        page.question_text[1].send_keys(question2_text)# STEP8
        select = Select(page.answer_type[1])  # STEP9
        select.select_by_visible_text('Dropdown')
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[1].get_attribute('textContent') == 'Guests will only select one of the options below.'
        assert len(page.dropdown_fields) ==4
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        page.dropdown_fields[2].send_keys('QA')# STEP10
        page.dropdown_fields[3].send_keys('DEV')
        page.add_option_button[1].click()# STEP11
        assert len(page.dropdown_fields) ==5
        assert page.dropdown_fields[4].is_displayed()
        page.dropdown_fields[4].send_keys('PM')# STEP12
        select = Select(page.applies_to[1])  # STEP13
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will be asked of each ticket buyer.'
        page.add_question_plus_button.click()# STEP14
        assert page.question3_title.get_attribute('textContent') == 'Question 3'
        assert len(page.remove_button) == 3
        assert len(page.question_text) == 3
        assert page.question_text[2].get_attribute('value') == ''
        assert len(page.answer_type) == 3
        select = Select(page.answer_type[2])
        assert select.first_selected_option.text == ''
        assert len(page.add_option_button) == 3
        assert page.is_element_present('add_option_button') == False
        assert page.add_option_button[2].is_displayed()
        select = Select(page.applies_to[2])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_question_plus_button') == True
        page.question_text[2].send_keys(question3_text)# STEP15
        select = Select(page.answer_type[2])  # STEP16
        select.select_by_visible_text('Checklist')
        assert page.add_option_button[2].is_displayed()
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[2].get_attribute('textContent') == 'Guests may select one or several options below.'
        assert len(page.dropdown_fields) == 7
        assert page.dropdown_fields[5].is_displayed()
        assert page.dropdown_fields[6].is_displayed()
        page.dropdown_fields[5].send_keys('Good')# STEP17
        page.dropdown_fields[6].send_keys('Not Bad')
        select = Select(page.applies_to[2])  # STEP18
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will be asked of each ticket buyer.'
        page.save_changes_button.click()#STEP19
        time.sleep(3)
        assert page.my_questions_msg.get_attribute('textContent') == 'Guests will answer these questions while booking for all activities.'
        assert len(page.my_questions_question) == 3
        assert page.my_questions_question[0].get_attribute('textContent') == question1_text
        assert page.my_questions_question[1].get_attribute('textContent') == question2_text
        assert page.my_questions_question[2].get_attribute('textContent') == question3_text

    def test_994(self):
        page = BookingQuestionsPage()  # STEP2
        page.open()
        page.my_questions_edit_button.click()  # STEP3
        time.sleep(2)
        assert page.question1_title.get_attribute('textContent') == 'Question 1'
        assert page.question2_title.get_attribute('textContent') == 'Question 2'
        assert page.question3_title.get_attribute('textContent') == 'Question 3'
        assert page.is_element_present('add_question_plus_button') == True
        assert page.is_element_present('remove_button') == True
        assert len(page.remove_button) == 3
        assert page.question_text[0].get_attribute('value') == question1_text
        assert page.question_text[1].get_attribute('value') == question2_text
        assert page.question_text[2].get_attribute('value') == question3_text
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == 'Text Input'
        assert page.answer_type_msg[0].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[0].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[1].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[1].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        assert page.is_element_present('add_option_button') == False
        assert len(page.add_option_button) == 3
        assert page.add_option_button[1].is_displayed()
        assert page.add_option_button[2].is_displayed()
        assert page.is_element_present('dropdown_fields') == False
        assert len(page.dropdown_fields) == 7
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        assert page.dropdown_fields[4].is_displayed()
        assert page.dropdown_fields[5].is_displayed()
        assert page.dropdown_fields[6].is_displayed()
        select = Select(page.answer_type[2])
        assert select.first_selected_option.text == 'Checklist'
        assert page.answer_type_msg[2].get_attribute('textContent') == 'Guests may select one or several options below.'
        select = Select(page.applies_to[2])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[2].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[4].get_attribute('value') == 'PM'
        assert page.dropdown_fields[5].get_attribute('value') == 'Good'
        assert page.dropdown_fields[6].get_attribute('value') == 'Not Bad'
        page.question_text[0].clear()  # STEP4
        page.question_text[0].send_keys('New question number ONE')
        select = Select(page.answer_type[0])  # STEP5
        select.select_by_visible_text('Checklist')
        assert page.add_option_button[0].is_displayed()
        assert page.is_element_present('add_option_button') == True
        assert page.answer_type_msg[0].get_attribute('textContent') == 'Guests may select one or several options below.'
        assert page.dropdown_fields[0].is_displayed()
        assert page.dropdown_fields[1].is_displayed()
        page.dropdown_fields[0].send_keys('First Answer for 1st question')  # STEP6
        page.dropdown_fields[1].send_keys('2nd Answer for question nubmer 1')
        select = Select(page.applies_to[0])  # STEP7
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.question_text[1].clear()  # STEP8
        page.question_text[1].send_keys('2nd NEW question')
        select = Select(page.answer_type[1])  # STEP9
        select.select_by_visible_text('Text Input')
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[1].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[1])  # STEP10
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.question_text[2].clear()  # STEP11
        page.question_text[2].send_keys('NEW QUESTION #3')
        select = Select(page.answer_type[2])  # STEP12
        select.select_by_visible_text('Dropdown')
        assert page.add_option_button[2].is_displayed()
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[2].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        assert len(page.dropdown_fields) == 7
        assert page.dropdown_fields[5].is_displayed()
        assert page.dropdown_fields[6].is_displayed()
        page.dropdown_fields[5].clear()
        page.dropdown_fields[6].clear()
        page.dropdown_fields[5].send_keys('3rd question - 1st answer')  # STEP13
        page.dropdown_fields[6].send_keys('2nd Answer for question nubmer 3')
        select = Select(page.applies_to[2])  # STEP14
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.remove_button[2].click()  # STEP15
        assert page.is_element_present('question3_title') == False
        assert len(page.dropdown_fields) == 5
        assert len(page.answer_type) == 2
        assert len(page.answer_type_msg) == 2
        page.cancel_button.click()  # STEP 16
        time.sleep(3)
        assert page.my_questions_msg.get_attribute(
            'textContent') == 'Guests will answer these questions while booking for all activities.'
        assert len(page.my_questions_question) == 3
        assert page.my_questions_question[0].get_attribute('textContent') == question1_text
        assert page.my_questions_question[1].get_attribute('textContent') == question2_text
        assert page.my_questions_question[2].get_attribute('textContent') == question3_text

    def test_995(self):
        page = BookingQuestionsPage()  # STEP2
        page.open()
        page.my_questions_edit_button.click()  # STEP3
        time.sleep(2)
        assert page.question1_title.get_attribute('textContent') == 'Question 1'
        assert page.question2_title.get_attribute('textContent') == 'Question 2'
        assert page.question3_title.get_attribute('textContent') == 'Question 3'
        assert page.is_element_present('add_question_plus_button') == True
        assert page.is_element_present('remove_button') == True
        assert len(page.remove_button) == 3
        assert page.question_text[0].get_attribute('value') == question1_text
        assert page.question_text[1].get_attribute('value') == question2_text
        assert page.question_text[2].get_attribute('value') == question3_text
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == 'Text Input'
        assert page.answer_type_msg[0].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[0].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[1].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[1].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        assert page.is_element_present('add_option_button') == False
        assert len(page.add_option_button) == 3
        assert page.add_option_button[1].is_displayed()
        assert page.add_option_button[2].is_displayed()
        assert page.is_element_present('dropdown_fields') == False
        assert len(page.dropdown_fields) == 7
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        assert page.dropdown_fields[4].is_displayed()
        assert page.dropdown_fields[5].is_displayed()
        assert page.dropdown_fields[6].is_displayed()
        select = Select(page.answer_type[2])
        assert select.first_selected_option.text == 'Checklist'
        assert page.answer_type_msg[2].get_attribute('textContent') == 'Guests may select one or several options below.'
        select = Select(page.applies_to[2])
        assert select.first_selected_option.text == 'Each Ticket'
        assert page.applies_to_msg[2].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[4].get_attribute('value') == 'PM'
        assert page.dropdown_fields[5].get_attribute('value') == 'Good'
        assert page.dropdown_fields[6].get_attribute('value') == 'Not Bad'
        page.question_text[0].clear()  # STEP4
        page.question_text[0].send_keys(question1edited_text)
        select = Select(page.answer_type[0])  # STEP5
        select.select_by_visible_text('Dropdown')
        assert page.add_option_button[0].is_displayed()
        assert page.is_element_present('add_option_button') == True
        assert page.answer_type_msg[0].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        assert page.dropdown_fields[0].is_displayed()
        assert page.dropdown_fields[1].is_displayed()
        page.dropdown_fields[0].send_keys('US')  # STEP6
        page.dropdown_fields[1].send_keys('Belarus')
        select = Select(page.applies_to[0])  # STEP7
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.question_text[1].clear()  # STEP8
        page.question_text[1].send_keys(question2edited_text)
        select = Select(page.answer_type[1])  # STEP9
        select.select_by_visible_text('Checklist')
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('add_option_button') == True
        assert page.answer_type_msg[1].get_attribute('textContent') == 'Guests may select one or several options below.'
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        assert page.dropdown_fields[4].is_displayed()
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[4].get_attribute('value') == 'PM'
        page.remove_answer_button[2].click()  # STEP 10
        assert len(page.dropdown_fields) == 6
        assert page.dropdown_fields[2].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[3].get_attribute('value') == 'PM'
        assert page.dropdown_fields[4].get_attribute('value') == 'Good'
        assert page.dropdown_fields[5].get_attribute('value') == 'Not Bad'
        page.dropdown_fields[2].clear()  # STEP 11
        page.dropdown_fields[2].send_keys('Beer')
        page.dropdown_fields[3].clear()
        page.dropdown_fields[3].send_keys('Milk')
        select = Select(page.applies_to[1])  # STEP12
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.question_text[2].clear()  # STEP13
        page.question_text[2].send_keys(question3edited_text)
        select = Select(page.answer_type[2])  # STEP14
        select.select_by_visible_text('Text Input')
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[2].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[2])  # STEP15
        select.select_by_visible_text('Entire Booking')
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.save_changes_button.click()  # STEP16
        time.sleep(3)
        assert page.my_questions_msg.get_attribute(
            'textContent') == 'Guests will answer these questions while booking for all activities.'
        assert len(page.my_questions_question) == 3
        page.my_questions_edit_button.click()  # STEP17
        assert page.question1_title.get_attribute('textContent') == 'Question 1'
        assert page.question2_title.get_attribute('textContent') == 'Question 2'
        assert page.question3_title.get_attribute('textContent') == 'Question 3'
        assert page.is_element_present('add_question_plus_button') == True
        assert page.is_element_present('remove_button') == True
        assert len(page.remove_button) == 3
        assert page.question_text[0].get_attribute('value') == question1edited_text
        assert page.question_text[1].get_attribute('value') == question2edited_text
        assert page.question_text[2].get_attribute('value') == question3edited_text
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[0].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Checklist'
        assert page.answer_type_msg[1].get_attribute(
            'textContent') == 'Guests may select one or several options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_option_button') == False
        assert len(page.add_option_button) == 3
        assert page.add_option_button[0].is_displayed()
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('dropdown_fields') == False
        assert len(page.dropdown_fields) == 6
        assert page.dropdown_fields[0].is_displayed()
        assert page.dropdown_fields[1].is_displayed()
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        select = Select(page.answer_type[2])
        assert select.first_selected_option.text == 'Text Input'
        assert page.answer_type_msg[2].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[2])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
        assert page.dropdown_fields[0].get_attribute('value') == 'US'
        assert page.dropdown_fields[1].get_attribute('value') == 'Belarus'
        assert page.dropdown_fields[2].get_attribute('value') == 'Beer'
        assert page.dropdown_fields[3].get_attribute('value') == 'Milk'

    def test_996(self):
        page = BookingQuestionsPage()  # STEP2
        page.open()
        time.sleep(3)
        assert page.my_questions_question[0].get_attribute('textContent') == question1edited_text
        assert page.my_questions_question[1].get_attribute('textContent') == question2edited_text
        assert page.my_questions_question[2].get_attribute('textContent') == question3edited_text
        page.my_questions_edit_button.click()  # STEP3
        assert page.question1_title.get_attribute('textContent') == 'Question 1'
        assert page.question2_title.get_attribute('textContent') == 'Question 2'
        assert page.question3_title.get_attribute('textContent') == 'Question 3'
        assert page.is_element_present('add_question_plus_button') == True
        assert page.is_element_present('remove_button') == True
        assert len(page.remove_button) == 3
        assert page.question_text[0].get_attribute('value') == question1edited_text
        assert page.question_text[1].get_attribute('value') == question2edited_text
        assert page.question_text[2].get_attribute('value') == question3edited_text
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[0].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Checklist'
        assert page.answer_type_msg[1].get_attribute('textContent') == 'Guests may select one or several options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_option_button') == False
        assert len(page.add_option_button) == 3
        assert page.add_option_button[0].is_displayed()
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('dropdown_fields') == False
        assert len(page.dropdown_fields) == 6
        assert page.dropdown_fields[0].is_displayed()
        assert page.dropdown_fields[1].is_displayed()
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        select = Select(page.answer_type[2])
        assert select.first_selected_option.text == 'Text Input'
        assert page.answer_type_msg[2].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[2])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.dropdown_fields[0].get_attribute('value') == 'US'
        assert page.dropdown_fields[1].get_attribute('value') == 'Belarus'
        assert page.dropdown_fields[2].get_attribute('value') == 'Beer'
        assert page.dropdown_fields[3].get_attribute('value') == 'Milk'
        page.remove_button[2].click()  # STEP4
        time.sleep(2)
        assert page.is_element_present('question3_title') == False
        assert len(page.dropdown_fields) == 4
        assert len(page.answer_type) == 2
        assert len(page.answer_type_msg) == 2
        page.remove_button[1].click()  # STEP5
        time.sleep(2)
        assert page.is_element_present('question2_title') == False
        assert len(page.dropdown_fields) == 2
        assert len(page.answer_type) == 1
        assert len(page.answer_type_msg) == 1
        page.question_text[0].send_keys(Keys.CONTROL + Keys.HOME)
        page.remove_button[0].click()  # STEP6
        time.sleep(2)
        assert page.is_element_present('question1_title') == False
        assert len(page.dropdown_fields) == 0
        assert len(page.answer_type) == 0
        assert len(page.answer_type_msg) == 0
        assert page.add_question_plus_button.is_displayed()
        page.save_changes_button.click()  # STEP7
        time.sleep(3)
        assert page.my_questions_no_questions_msg.get_attribute(
            'innerText') == "You don't have any questions added! Click Edit below to add some."
        assert len(page.my_questions_question) == 0
        page.my_questions_edit_button.click()  # STEP8
        time.sleep(2)
        assert page.add_question_plus_button.is_displayed()
