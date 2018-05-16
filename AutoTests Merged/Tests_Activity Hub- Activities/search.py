from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from Activity_Hub_page import ActivityHubPage
from Activity_page import AddEditActivityPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select

get_driver().maximize_window()
page = loginpage()
page.open()
page.login_field.send_keys('devtester')
page.password_field.send_keys('nf')
page.button.click()
page = ActivityHubPage()
page.open()
page.search_activity_field.send_keys('AutoTest0138')
page.activity_actions.click()
wait = WebDriverWait(get_driver(), 15)
wait.until(lambda driver: page.is_element_present('activity_actions'))
text = page.activity_title.get_attribute("textContent")
print(text)
# assert page.is_element_present('activity_actions')
# page.activity_actions.click()
# wait = WebDriverWait(get_driver(), 15)
# wait.until(lambda driver: page.is_element_present('edit_activity'))