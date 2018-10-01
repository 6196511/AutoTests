from selenium.webdriver.common.by import By
from webium import BasePage, Find


class TaxesReportPage(BasePage):
    url = 'https://dev.godo.io/taxes_report.aspx'