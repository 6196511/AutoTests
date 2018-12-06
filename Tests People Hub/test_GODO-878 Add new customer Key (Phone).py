from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from customer_list import CustomerListPage
import time
import random
from random import choice
from string import digits
from creds import admin_login, admin_password, server, database, username, password
import pyodbc


class BaseTest(object):
    def teardown_class(self):
         close_driver()


class Test_GODO878(BaseTest):
    def test_878(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = CustomerListPage()
        page.open()
        page.add_customer_button.click()
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James', 'Bob', 'Ivan', 'Tim', 'Chris', 'Jim', 'Pahom', 'Vlad', 'Paul')
        NewFirstName = random.choice(first_names)
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff', 'Green', 'Clinton', 'Jameson', 'Last', 'Sergeff', 'Madison')
        NewLastName = random.choice(last_names)
        NewFullName = NewFirstName+' '+''.join(NewLastName)
        page.last_name_field.send_keys(NewLastName)
        NewPhone= (''.join(choice(digits) for i in range(15)))
        page.phone_field.send_keys(NewPhone)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewFullName)
        page.search_button.click()
        time.sleep(5)
        assert page.customer_name_in_list.get_attribute('textContent')==NewFullName
        assert page.phone_in_list.get_attribute('textContent')==NewPhone
        page.edit_button.click()
        assert page.customer_name_info.get_attribute('textContent')==NewFullName+"'s"
        assert page.phone_info.get_attribute('innerText')==NewPhone
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM customer ORDER BY customer_id DESC")
        row = cursor.fetchone()
        assert row[1]==68 #company ID
        assert row[2]==NewFirstName
        assert row[3]==NewLastName
        assert row[10]==NewPhone
        assert row[17] == NewPhone #CustomerKey