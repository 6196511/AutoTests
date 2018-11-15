from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds


class GrouponList(WebElement):
    groupon_name = Find(by=By.XPATH, value="./td[2]")
    edit_button = Find(by=By.XPATH, value="td[5]/a")


class CodeList(WebElement):
    code = Find(by=By.XPATH, value="./td[2]")
    redeemed = Find(by=By.XPATH, value="./td[3]")


class GrouponPage(BasePage):

    url = 'https://ci004.godo.io/integration_groupon.aspx'  
    import_codes = Find(by=By.XPATH, value="//div[@name='inputCodeForm']//button")
    groupon_list = Finds(GrouponList, by=By.XPATH, value="//tbody/tr")
    details = Find(by=By.XPATH, value="//a[text()='Details']")
    view_redemptions = Find(by=By.XPATH, value="//a[text()='View Redemptions']")
    view_codes = Find(by=By.XPATH, value="//a[text()='View Codes']")
    code_list_not_redeemed = Finds(CodeList, by=By.XPATH, value="//td[text()=0]/..")
    code_list_redeemed = Finds(CodeList, by=By.XPATH, value="//td[text()=1]/..")

    def select_groupon(self, name):
        for item in self.groupon_list:
            if item.groupon_name.text == name:
                item.edit_button.click()
                break

    def copy_code(self, order):
        for item in self.code_list_not_redeemed:
            if item.redeemed.text == "0":
                print(item.code.text)
                order.promo_code = item.code.text
                break

    def copy_redeemed_code(self, order):
        for item in self.code_list_redeemed:
            if item.redeemed.text == "1":
                print(item.code.text)
                order.promo_code = item.code.text
                break
