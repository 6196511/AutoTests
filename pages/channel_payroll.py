from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class ChannelPayrollPage(BasePage):
    url = 'https://dev.godo.io/channel_payroll.aspx'
    channel_payment_due = Find(by=By.XPATH, value="//a[@id='payrolldetailplus_']")
    channel_paid = Find(by=By.XPATH, value="//a[@id='paymentPaidChannel']")
    channel_entries = Finds(by=By.XPATH, value="//tbody[@ng-repeat='payment in vm.channelPaymentDue track by $index']")
    channel_names = Finds(by=By.XPATH, value="//tbody[@ng-repeat='payment in vm.channelPaymentDue track by $index']")
    channel_paid_entries = Finds(by=By.XPATH, value="//tr[@ng-repeat='payment in vm.channelPaid track by $index']")
    channel_paid_amounts = Finds(by=By.XPATH, value="//*[@id='dtChannelPaid']/tbody/tr/td[4]")
    channel_detail = Finds(by=By.XPATH, value="//a[@ng-click='vm.showDetails(payment.channelId)']")
    direct_deposit = Finds(by=By.XPATH, value="//input[@value='directdeposit']")
    cash = Finds(by=By.XPATH, value="//input[@value='cash']")
    check = Finds(by=By.XPATH, value="//input[@value='check']")
    check_number = Finds(by=By.XPATH, value="//input[@type='text']")
    pay_button = Finds(by=By.XPATH, value="//button[@ng-click='vm.commitChannelPayment(payment)']")
    OK_button = Find(by=By.XPATH, value="//button[@ng-click='vm.cancel()']")




    guide_list = Find(by=By.XPATH, value="//select[@id='selectGuides']")
    event_due = Finds(by=By.XPATH, value ="//*[contains(@id,'guidePayroll')]/tbody/tr[1]/td[6]")
    activity_timedate = Finds(by=By.XPATH, value ="//a[contains(@ng-click,'vm.openManifest')]")

    show_entries = Find(by=By.XPATH, value="//select[@name='guidePayrollAll_length']")
    payment_entry = Finds(by=By.XPATH, value="//tr[@class='row']|//tr[@class='odd']|//tr[@class='even']")