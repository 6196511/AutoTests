from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class BookingQuestionsPage(BasePage):
    url = 'https://dev.godo.io/booking_questions.aspx'
    add_question_plus_button = Find(by=By.XPATH, value="//div[@ng-click='vm.addQuestion()']")
    question1_title = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/popup-content-loader/ng-transclude/div[1]/div/div/gd-question-set/div/div/div[2]/div/div/gd-question/div/div/div[1]/div/h4")
    question2_title = Find(by=By.XPATH,value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/popup-content-loader/ng-transclude/div[1]/div/div/gd-question-set/div/div/div[2]/div/div[2]/gd-question/div/div/div[1]/div/h4")
    question3_title = Find(by=By.XPATH,value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/popup-content-loader/ng-transclude/div[1]/div/div/gd-question-set/div/div/div[2]/div/div[3]/gd-question/div/div/div[1]/div/h4")
    remove_button = Finds(by=By.XPATH, value="//div[@ng-click='vm.remove()']")
    question_text = Finds(by=By.XPATH, value="//textarea[@name='question-text']")
    answer_type = Finds(by=By.XPATH, value="//select[@name='question-type']")
    answer_type_msg = Finds(by=By.XPATH, value="//p[@ng-bind='vm.getTypeDescription(vm.question.type)']")
    add_option_button = Finds(by=By.XPATH, value="//div[@ng-click='vm.addOption()']")
    applies_to = Finds(by=By.XPATH, value="//select[@name='question-perticket']")
    applies_to_msg = Finds(by=By.XPATH, value="//p[@ng-bind='vm.getPerTicketDescription(vm.question.perTicket)']")
    dropdown_fields = Finds(by=By.XPATH, value="//input[@placeholder='Add a selectable answer for your question']")
    save_changes_button = Find(by=By.XPATH, value="//div[@ng-click='vm.save()']")
    cancel_button = Find(by=By.XPATH, value="//div[@ng-click='vm.cancel()']")
    my_questions_msg = Find(by=By.XPATH, value="//*[@id='wrapper']/div[6]/div/div/div[2]/div/popup-content-loader/ng-transclude/div[1]/div/div/div")
    my_questions_question = Finds(by=By.XPATH, value="//span[@ng-bind='vm.question.text']")
    my_questions_edit_button = Find(by=By.XPATH, value="//div[@ng-click='vm.toggleEdit()']")
    remove_answer_button = Finds(by=By.XPATH, value="//div[@ng-click='vm.removeItem($index)']")
    my_questions_no_questions_msg = Find(by=By.XPATH, value="//div[@ng-if='!vm.questionSet.questions.length']")
