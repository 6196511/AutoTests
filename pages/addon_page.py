from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from waiting import wait
from webium import BasePage, Find, Finds


class TypesList(WebElement):
    name = Find(by=By.XPATH, value="./td[1]")
    price = Find(by=By.XPATH, value="./td[2]")
    status = Find(by=By.XPATH, value="./td[3]")
    edit = Find(by=By.XPATH, value="./td[4]/a")
    delete = Find(by=By.XPATH, value="./td[5]/a")


class ActivityList(WebElement):
    activity = Find(by=By.XPATH, value="./td[1]")
    addon = Find(by=By.XPATH, value="./td[2]")
    delete = Find(by=By.XPATH, value="./td[3]/a")


class AddonPage(BasePage):

    # Create or Edit add-on.

    addon_name = Find(by=By.XPATH, value="//input[@id='addon_name']")
    addon_price = Find(by=By.XPATH, value="//input[@id='addon_price']")
    addon_description = Find(by=By.XPATH, value="//textarea[@id='addon_description']")
    addon_status = Find(by=By.XPATH, value="//select[@id='addon_status']")
    save_addon = Find(by=By.XPATH, value="//button[@id='submitaddon']")
    cancel_addon = Find(by=By.XPATH, value="//a[text()='Cancel']")

    # Add addon type.

    add_type_button = Find(by=By.XPATH, value="//button[@id='addAddonExt']")
    addon_select = Find(by=By.XPATH, value="//select[@id='addon_id']")
    type_name = Find(by=By.XPATH, value="//input[@id='addon_ex_name']")
    type_price = Find(by=By.XPATH, value="//input[@id='addon_ex_price']")
    type_status = Find(by=By.XPATH, value="//input[@id='addon_ex_status']")
    save_type = Find(by=By.XPATH, value="//button[@id='submitaddonex']")
    cancel_type = Find(by=By.XPATH, value="//button[@id='canceladdonex']")

    addon_types_table = Finds(TypesList, by=By.XPATH, value="//table[@id='dtAddonEx']/tbody/tr")

    # Add activity.

    add_activity = Find(by=By.XPATH, value="//button[@id='addAddonToActivity']")
    select_activity = Find(by=By.XPATH, value="//select[@id='activity_id']")
    save_activity = Find(by=By.XPATH, value="//button[@id='submitaddonactivity']")
    cancel_activity = Find(by=By.XPATH, value="//button[@id='canceladdonactivity']")

    activity_table = Finds(ActivityList, by=By.XPATH, value="//div[@id='addonsactivitylist']//tbody/tr")

    pop_up = Find(by=By.XPATH, value="//div[@class='bootbox-body']")
    pop_up_ok_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='OK']")
    pop_up_cancel_button = Find(by=By.XPATH, value="//div[@class='modal-footer']/button[text()='Cancel']")

    def select(self, web_element, option):
        Select(web_element).select_by_visible_text(option)

    def wait_redirection(self):
        old_url = self._driver.current_url
        wait(lambda: self._driver.current_url != old_url)

