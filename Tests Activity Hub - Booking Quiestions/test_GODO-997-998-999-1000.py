from webium.driver import get_driver
from webium.driver import close_driver
from selenium.webdriver.support.ui import Select
import time
from booking_questions import BookingQuestionsPage
from Login import loginpage
from creds import admin_login, admin_password

question_set1_name = 'Test_997'
question_set2_name = 'AutoTest_998'
question_set3_name = 'Godo test #999'
activity_name = 'Test ET Time'
activity2_name = 'Xmas Tour'
activity3_name = 'Dresden Tour'
activity4_name = 'AlertTest1'
question1_text = 'What is your favourite meal?'
question2_text = 'What is your job?'
question3_text = 'How are you?'
question1edited_text = 'Where are you from?'
question2edited_text = 'What is your favourite drink?'
question3edited_text = 'What is your profession?'


class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_997_998_999_1000(BaseTest):
    def test_997(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = BookingQuestionsPage()#STEP1
        page.open()
        time.sleep(12)
        page.custom_questions_add_question_set_plus_button.click()#STEP2
        time.sleep(2)
        assert page.is_element_present('question_set_name') == True
        assert page.is_element_present('selected_activities_list') == True
        assert page.is_element_present('add_question_plus_button') == True
        page.question_set_name.send_keys(question_set1_name)#STEP3
        select = Select(page.selected_activities_list)#STEP4
        select.select_by_visible_text(activity_name)
        assert len(page.selected_activities_lists) == 2
        page.add_question_plus_button.click()#STEP5
        time.sleep(2)
        assert page.question1_custom_title.get_attribute('textContent') == 'Question 1'
        assert page.is_element_present('remove_button') == True
        assert page.question_text[0].get_attribute('value') == ''
        select = Select(page.answer_type[0])
        assert select.first_selected_option.text == ''
        assert page.is_element_present('add_option_button') == True
        select = Select(page.applies_to[0])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        assert page.is_element_present('add_question_plus_button') == True
        page.question_text[0].send_keys(question1_text)  # STEP6
        select = Select(page.answer_type[0])#STEP7
        select.select_by_visible_text('Text Input')
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[0].get_attribute('textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[0])#STEP8
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.add_question_plus_button.click()#STEP9
        assert page.question2_custom_title.get_attribute('textContent') == 'Question 2'
        assert len(page.remove_button) == 2
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
        page.question_text[1].send_keys(question2_text) #STEP10
        select = Select(page.answer_type[1])  # STEP11
        select.select_by_visible_text('Dropdown')
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[1].get_attribute('textContent') == 'Guests will only select one of the options below.'
        assert len(page.dropdown_fields) == 4
        assert page.dropdown_fields[2].is_displayed()
        assert page.dropdown_fields[3].is_displayed()
        page.dropdown_fields[2].send_keys('QA')  # STEP12
        page.dropdown_fields[3].send_keys('DEV')
        select = Select(page.applies_to[1])  # STEP13
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.add_question_plus_button.click()  # STEP14
        assert page.question3_custom_title.get_attribute('textContent') == 'Question 3'
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
        page.question_text[2].send_keys(question3_text)  # STEP15
        select = Select(page.answer_type[2])  # STEP16
        select.select_by_visible_text('Checklist')
        assert page.add_option_button[2].is_displayed()
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[2].get_attribute('textContent') == 'Guests may select one or several options below.'
        assert len(page.dropdown_fields) == 6
        assert page.dropdown_fields[4].is_displayed()
        assert page.dropdown_fields[5].is_displayed()
        page.add_option_button[2].click()# STEP17
        assert len(page.dropdown_fields) == 7
        assert page.dropdown_fields[6].is_displayed()
        page.dropdown_fields[4].send_keys('Good')  # STEP18
        page.dropdown_fields[5].send_keys('Not bad')
        page.dropdown_fields[6].send_keys('Fine, thanks')
        select = Select(page.applies_to[2])  # STEP19
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute('textContent') == 'This question will relate to the whole booking.'
        page.save_changes_button.click()# STEP20
        time.sleep(3)
        get_driver().refresh()
        time.sleep(15)
        assert page.custom_questions_msg.get_attribute('textContent') == 'Create an additional set of questions that can be asked for selected activities.'
        assert page.custom_questions_titles[-1].get_attribute('textContent') == question_set1_name
        assert page.my_questions_question[-3].get_attribute('textContent') == question1_text
        assert page.my_questions_question[-2].get_attribute('textContent') == question2_text
        assert page.my_questions_question[-1].get_attribute('textContent') == question3_text

    def test_998(self):
        page = BookingQuestionsPage()  # STEP2
        page.open()
        time.sleep(7)
        page.custom_questions_edit_buttons[-1].click()# STEP3
        time.sleep(2)
        assert page.question_set_name.get_attribute('value') == question_set1_name
        select = Select(page.selected_activities_list)
        assert select.first_selected_option.text == activity_name
        assert page.edit_custom_questions_titles[-3].get_attribute('textContent') == 'Question 1'
        assert page.edit_custom_questions_titles[-2].get_attribute('textContent') == 'Question 2'
        assert page.edit_custom_questions_titles[-1].get_attribute('textContent') == 'Question 3'
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
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute(
             'textContent') == 'This question will relate to the whole booking.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[1].get_attribute(
             'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute(
             'textContent') == 'This question will relate to the whole booking.'
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
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute(
             'textContent') == 'This question will relate to the whole booking.'
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[4].get_attribute('value') == 'Good'
        assert page.dropdown_fields[5].get_attribute('value') == 'Not bad'
        assert page.dropdown_fields[6].get_attribute('value') == 'Fine, thanks'
        page.question_set_name.clear()  # STEP4
        page.question_set_name.send_keys(question_set2_name)
        select = Select(page.selected_activities_list)#STEP5
        select.select_by_visible_text(activity2_name)
        assert len(page.selected_activities_lists) == 2
        time.sleep(10)
        page.question_text[0].clear()  # STEP6
        page.question_text[0].send_keys('New question number ONE')
        select = Select(page.answer_type[0]) # STEP7
        select.select_by_visible_text('Dropdown')
        assert page.add_option_button[0].is_displayed()
        assert page.is_element_present('add_option_button') == True
        assert page.answer_type_msg[0].get_attribute('textContent') == 'Guests will only select one of the options below.'
        assert page.dropdown_fields[0].is_displayed()
        assert page.dropdown_fields[1].is_displayed()
        page.dropdown_fields[0].send_keys('First Answer for 1st question')  # STEP8
        page.dropdown_fields[1].send_keys('2nd Answer for question nubmer 1')
        select = Select(page.applies_to[0])  # STEP9
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[0].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        page.question_text[1].clear()  # STEP10
        page.question_text[1].send_keys('2nd NEW question')
        select = Select(page.answer_type[1])  # STEP11
        select.select_by_visible_text('Checklist')
        assert page.add_option_button[1].is_displayed()
        assert page.is_element_present('add_option_button') == True
        assert page.answer_type_msg[1].get_attribute('textContent') == 'Guests may select one or several options below.'
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        page.dropdown_fields[2].clear()# STEP12
        page.dropdown_fields[2].send_keys('PM')
        page.dropdown_fields[3].clear()
        page.dropdown_fields[3].send_keys('CEO')
        select = Select(page.applies_to[1])  # STEP13
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[1].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        page.question_text[2].clear()  # STEP14
        page.question_text[2].send_keys('NEW QUESTION #3')
        select = Select(page.answer_type[2])  # STEP15
        select.select_by_visible_text('Text Input')
        assert page.is_element_present('add_option_button') == False
        assert page.answer_type_msg[2].get_attribute(
            'textContent') == 'Guests will write out their own answer to this question.'
        select = Select(page.applies_to[2])  # STEP16
        select.select_by_visible_text('Each Ticket')
        assert page.applies_to_msg[2].get_attribute(
            'textContent') == 'This question will be asked of each ticket buyer.'
        page.remove_button[2].click()  # STEP17
        time.sleep(7)
        assert page.is_element_present('edit_custom_questions_titles') == False
        assert len(page.dropdown_fields) == 4
        assert len(page.answer_type) == 2
        assert len(page.answer_type_msg) == 2
        page.cancel_button.click()  # STEP 18
        time.sleep(5)
        get_driver().refresh()
        time.sleep(15)
        assert page.custom_questions_msg.get_attribute('textContent') == 'Create an additional set of questions that can be asked for selected activities.'
        assert page.custom_questions_titles[-1].get_attribute('textContent') == question_set1_name
        assert page.my_questions_question[-3].get_attribute('textContent') == question1_text
        assert page.my_questions_question[-2].get_attribute('textContent') == question2_text
        assert page.my_questions_question[-1].get_attribute('textContent') == question3_text
        page.custom_questions_edit_buttons[-1].click()  # STEP19
        time.sleep(2)
        assert page.question_set_name.get_attribute('value') == question_set1_name
        select = Select(page.selected_activities_list)
        assert select.first_selected_option.text == activity_name
        assert page.edit_custom_questions_titles[-3].get_attribute('textContent') == 'Question 1'
        assert page.edit_custom_questions_titles[-2].get_attribute('textContent') == 'Question 2'
        assert page.edit_custom_questions_titles[-1].get_attribute('textContent') == 'Question 3'
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
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[0].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
        select = Select(page.answer_type[1])
        assert select.first_selected_option.text == 'Dropdown'
        assert page.answer_type_msg[1].get_attribute(
            'textContent') == 'Guests will only select one of the options below.'
        select = Select(page.applies_to[1])
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[1].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
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
        assert select.first_selected_option.text == 'Entire Booking'
        assert page.applies_to_msg[2].get_attribute(
            'textContent') == 'This question will relate to the whole booking.'
        assert page.dropdown_fields[2].get_attribute('value') == 'QA'
        assert page.dropdown_fields[3].get_attribute('value') == 'DEV'
        assert page.dropdown_fields[4].get_attribute('value') == 'Good'
        assert page.dropdown_fields[5].get_attribute('value') == 'Not bad'
        assert page.dropdown_fields[6].get_attribute('value') == 'Fine, thanks'
