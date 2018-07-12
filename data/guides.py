import pandas as pd

from model.guides import Guides


df1 = pd.read_excel("../data/guides.xlsx", "Guides", dtype=str, keep_default_na=False)

excel_dict1 = df1.to_dict(orient='records')

guides = []


def extract_test_data(testdata, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        testdata.append(Guides(**item))


extract_test_data(guides, excel_dict1)
