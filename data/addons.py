import pandas as pd

from model.addons import Addons


df1 = pd.read_excel("../data/addons.xlsx", "Addons", dtype=str, keep_default_na=False)

excel_dict1 = df1.to_dict(orient='records')

addons = []


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Addons(**item))


extract_test_data(addons, excel_dict1)
