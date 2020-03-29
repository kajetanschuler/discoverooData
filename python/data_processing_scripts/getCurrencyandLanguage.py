# Skript, das zusätzlich Sprache und Währung zu country_data_final hinzufügt
# created 23.03.2020 by Malik
# NOCH in BEARBEITUNG



import requests
import json
import pprint as pp
import pandas as pd
from pandas.io.json import json_normalize
import pprint as pp




def main():

    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.request("GET", url)
    r = pd.read_json(response.text)
    print(r)
    df = pd.io.json.json_normalize(r)
    print(df)
    df.columns = df.columns.map(lambda x: x.split(".")[-1])
    print(df.columns)






    #df.to_csv("../data_raw/currencyAndLanguage.csv")



if __name__ == '__main__':
        main()