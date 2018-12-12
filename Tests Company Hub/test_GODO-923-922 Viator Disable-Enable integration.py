from webium.driver import get_driver
from webium.driver import close_driver
from company_page import EditCompanyPage
from Login import loginpage
import time
from random import choice
from string import digits
from creds import admin_login, admin_password, server, database, username, password
import pyodbc


SupplierIDlist = []

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO923_922(BaseTest):
    def test_923(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = EditCompanyPage()
        page.open()
        time.sleep(5)
        if page.viator_checkbox.is_selected() == False:
            page.viator_checkbox.click()
            page.save_button.click()
            page.open()
        else:
            pass
        assert page.viator_checkbox.is_selected() == True
        SupplierID = page.viator_supplierID.get_attribute('value')
        SupplierIDlist.append(SupplierID)
        page.viator_checkbox.click()
        assert page.viator_checkbox.is_selected() == False
        assert page.is_element_present('viator_supplierID')==False
        page.save_button.click()
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)  # STEP 14
        cursor = cnxn.cursor()
        cursor.execute("SELECT company_viator_useAPI FROM company WHERE company_id = 68")
        row = cursor.fetchone()
        assert row[0]==0

    def test_922(self):
        page = EditCompanyPage()
        page.open()
        time.sleep(5)
        page.viator_checkbox.click()
        assert page.viator_supplierID.is_displayed()
        page.viator_supplierID.clear()
        NewSupplierID = (''.join(choice(digits) for i in range(7)))
        page.viator_supplierID.send_keys(NewSupplierID)
        page.save_button.click()
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)  # STEP 14
        cursor = cnxn.cursor()
        cursor.execute("SELECT company_viator_useAPI, company_viator_supplierid  FROM company WHERE company_id = 68")
        row = cursor.fetchone()
        assert row[0] == 1
        assert row[1] == NewSupplierID
        page = EditCompanyPage()
        page.open()
        time.sleep(5)
        page.viator_supplierID.clear()
        page.viator_supplierID.send_keys(SupplierIDlist[0])
        page.save_button.click()
        cursor.execute("SELECT company_viator_useAPI, company_viator_supplierid  FROM company WHERE company_id = 68")
        row = cursor.fetchone()
        assert row[0] == 1
        assert row[1] == (SupplierIDlist[0])

