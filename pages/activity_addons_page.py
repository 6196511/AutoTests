from selenium.webdriver.common.by import By
from webium import BasePage, Find


class ActivityAddonsPage(BasePage):

    create_addon = Find(by=By.XPATH, value="//button[text()='Create New Add-On']")

    search_feild = Find(by=By.XPATH, value="//input[@id='searchA']")

    # First row of the add-ons table.

    name = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[1]")
    description = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[2]")
    price = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[3]")
    status = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[4]")
    edit_button = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[5]/a")
    delete_button = Find(by=By.XPATH, value="//table[@id='addontbl']/tbody/tr[1]/td[6]/a")

    pop_up = Find(by=By.XPATH, value="//div[@class='bootbox-body']")
    pop_up_ok_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='OK']")
    pop_up_cancel_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='Cancel']")
