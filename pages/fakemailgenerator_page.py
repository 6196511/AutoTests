from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class FakeMailGeneratorPage(BasePage):
    url = 'http://www.fakemailgenerator.com'
    inbox_field = Find(by=By.XPATH, value="//input[@id='home-email']")
    domain_list = Find(by=By.XPATH, value="//button[@id='domain-select']")
    cuvox_domain = Find(by=By.XPATH, value="//*[@id='home-email-group']/div/div/ul/li/a[2]")
    from_field = Find(by=By.XPATH, value="//*[@id='email-list']/li/div/dl/dd[2]")
    to_field =  Find(by=By.XPATH, value="//*[@id='email-list']/li/div/dl/dd[1]")
    subject_field = Find(by=By.XPATH, value="//*[@id='email-list']/li/div/dl/dd[3]")
    body_field = Find(by=By.XPATH, value="/html/body/center/table/tbody/tr/td/table[2]/tbody/tr[2]/td/table/tbody")








