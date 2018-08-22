from selenium.webdriver.common.by import By
from webium import BasePage, Find


class RainChecksPage(BasePage):

    # First row.

    page_title = Find(by=By.XPATH, value="//div[@class='godo-page-title']//h1")
    event_name = Find(by=By.XPATH, value="//table[@id='DataTables_Table_0']/tbody/tr[1]/td[1]")
    date = Find(by=By.XPATH, value="//table[@id='DataTables_Table_0']/tbody/tr[1]/td[2]")
    guest = Find(by=By.XPATH, value="//table[@id='DataTables_Table_0']/tbody/tr[1]/td[3]")
    email = Find(by=By.XPATH, value="//table[@id='DataTables_Table_0']/tbody/tr[1]/td[4]")
    phone = Find(by=By.XPATH, value="//table[@id='DataTables_Table_0']/tbody/tr[1]/td[5]")
