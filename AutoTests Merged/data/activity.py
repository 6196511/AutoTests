import pandas as pd

from model.activity import Activity


df1 = pd.read_excel("../data/activity.xlsx", "Activities", dtype=str, keep_default_na=False)

excel_dict1 = df1.to_dict(orient='records')

testdata1 = []


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Activity(**item))


extract_test_data(testdata1, excel_dict1)
