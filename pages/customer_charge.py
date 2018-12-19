from selenium.webdriver.common.by import By
from webium import BasePage, Find


class CustomerChargePage(BasePage):
    ticket_total = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[1]/td[2]")
    addon = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[2]/td[2]")
    boooking_fee = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[3]/td[2]")
    sub_total = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[4]/td[2]")
    taxes = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[5]/td[2]")
    grand_total = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[6]/td[2]")
    total_charges = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[7]/td[2]")
    total_due = Find(by=By.XPATH, value="//*[@id='customereventchargeinfohtml']/div[2]/table[2]/tbody/tr[8]/td[2]")
