import pandas as pd

from model.certificate import Certificate

df1 = pd.read_excel("../data/certificates.xlsx", "Successful", dtype=str, keep_default_na=False)
df2 = pd.read_excel("../data/certificates.xlsx", "Declined", dtype=str, keep_default_na=False)
df3 = pd.read_excel("../data/certificates.xlsx", "Customer Successful", dtype=str, keep_default_na=False)
df4 = pd.read_excel("../data/certificates.xlsx", "Customer Declined", dtype=str, keep_default_na=False)

excel_dict1 = df1.to_dict(orient='records')
excel_dict2 = df2.to_dict(orient='records')
excel_dict3 = df3.to_dict(orient='records')
excel_dict4 = df4.to_dict(orient='records')

testdata1 = []
testdata2 = []
testdata_cus1 = []
testdata_cus2 = []


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Certificate(**item))


extract_test_data(testdata1, excel_dict1)
extract_test_data(testdata2, excel_dict2)
extract_test_data(testdata_cus1, excel_dict3)
extract_test_data(testdata_cus2, excel_dict4)
