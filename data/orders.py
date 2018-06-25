import datetime

import pandas as pd

from model.orders import Orders


df1 = pd.read_excel("../data/orders.xlsx", "Admin payment types", dtype=str, keep_default_na=False)
df2 = pd.read_excel("../data/orders.xlsx", "Admin declines", dtype=str, keep_default_na=False)
df3 = pd.read_excel("../data/orders.xlsx", "Admin valid discounts", dtype=str, keep_default_na=False)
df4 = pd.read_excel("../data/orders.xlsx", "Admin invalid discounts", dtype=str, keep_default_na=False)
df5 = pd.read_excel("../data/orders.xlsx", "Customer payment types", dtype=str, keep_default_na=False)
df6 = pd.read_excel("../data/orders.xlsx", "Customer declines", dtype=str, keep_default_na=False)
df7 = pd.read_excel("../data/orders.xlsx", "Customer valid discounts", dtype=str, keep_default_na=False)
df8 = pd.read_excel("../data/orders.xlsx", "Customer invalid discounts", dtype=str, keep_default_na=False)
df9 = pd.read_excel("../data/orders.xlsx", "Admin booking with certificates", dtype=str, keep_default_na=False)
df10 = pd.read_excel("../data/orders.xlsx", "Admin certificates", dtype=str, keep_default_na=False)
df11 = pd.read_excel("../data/orders.xlsx", "Admin certificates declines", dtype=str, keep_default_na=False)
df12 = pd.read_excel("../data/orders.xlsx", "Customer certificates", dtype=str, keep_default_na=False)
df13 = pd.read_excel("../data/orders.xlsx", "Customer certificates declines", dtype=str, keep_default_na=False)
df14 = pd.read_excel("../data/orders.xlsx", "Center payment types", dtype=str, keep_default_na=False)
df15 = pd.read_excel("../data/orders.xlsx", "Center certificates", dtype=str, keep_default_na=False)
df16 = pd.read_excel("../data/orders.xlsx", "Center certificates declines", dtype=str, keep_default_na=False)
df17 = pd.read_excel("../data/orders.xlsx", "Admin cert + discount", dtype=str, keep_default_na=False)


excel_dict1 = df1.to_dict(orient='records')
excel_dict2 = df2.to_dict(orient='records')
excel_dict3 = df3.to_dict(orient='records')
excel_dict4 = df4.to_dict(orient='records')
excel_dict5 = df5.to_dict(orient='records')
excel_dict6 = df6.to_dict(orient='records')
excel_dict7 = df7.to_dict(orient='records')
excel_dict8 = df8.to_dict(orient='records')
excel_dict9 = df9.to_dict(orient='records')
excel_dict10 = df10.to_dict(orient='records')
excel_dict11 = df11.to_dict(orient='records')
excel_dict12 = df12.to_dict(orient='records')
excel_dict13 = df13.to_dict(orient='records')
excel_dict14 = df14.to_dict(orient='records')
excel_dict15 = df15.to_dict(orient='records')
excel_dict16 = df16.to_dict(orient='records')
excel_dict17 = df17.to_dict(orient='records')


admin_data = []
admin_declines = []
admin_valid_codes = []
admin_invalid_codes = []
admin_booking_with_certificates = []
customer_data = []
customer_declines = []
customer_valid_codes = []
customer_invalid_codes = []
admin_certificates = []
admin_certificates_declines = []
customer_certificates = []
customer_certificates_declines = []
center_data = []
center_certificates = []
center_certificates_declines = []
admin_cert_discount = []

today = datetime.date.today()
purchase_date = today + datetime.timedelta(days=1)  # Tickets will be booked on tomorrow.


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        if item.get('year') == "":
            item['year'] = str(purchase_date.year)
        if item.get('month') == "":
            item['month'] = str(purchase_date.month)
        if item.get('day') == "":
            item['day'] = str(purchase_date.day)
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Orders(**item))


extract_test_data(admin_data, excel_dict1)
extract_test_data(admin_declines, excel_dict2)
extract_test_data(admin_valid_codes, excel_dict3)
extract_test_data(admin_invalid_codes, excel_dict4)
extract_test_data(customer_data, excel_dict5)
extract_test_data(customer_declines, excel_dict6)
extract_test_data(customer_valid_codes, excel_dict7)
extract_test_data(customer_invalid_codes, excel_dict8)
extract_test_data(admin_booking_with_certificates, excel_dict9)
extract_test_data(admin_certificates, excel_dict10)
extract_test_data(admin_certificates_declines, excel_dict11)
extract_test_data(customer_certificates, excel_dict12)
extract_test_data(customer_certificates_declines, excel_dict13)
extract_test_data(center_data, excel_dict14)
extract_test_data(center_certificates, excel_dict15)
extract_test_data(center_certificates_declines, excel_dict16)
extract_test_data(admin_cert_discount, excel_dict17)
