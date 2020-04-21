# Skript, das zusätzlich Sprache und Währung zu country_data_final hinzufügt
# created 23.03.2020 by Malik & Kajetan
# NOCH in BEARBEITUNG


import requests
import json
import pprint as pp
import pandas as pd
import pandas.io.json as pd_json
import pprint as pp
from IPython.display import display, HTML




def main():

    currencyList = []
    url = 'https://restcountries.eu/rest/v2/all'
    r = requests.request("GET", url)
    data = json.loads(r.text)
    for country in data:
        countryCode = country['alpha2Code']
        flagLink = country['flag']
        currencies = country['currencies']
        for currency in currencies:

            currencyCode = currency['code']
            currencyName = currency['name']
            currencySymbol = currency['symbol']

            currencyTmp = [countryCode, currencyCode, currencyName, currencySymbol]
            currencyList.append(currencyTmp)

    df = pd.DataFrame(currencyList)
    print(df)
    df = df[df[1] != '(none)']
    print(df)
    header = ['countryCode', 'currencyCode', 'currencyName', 'currencySymbol']
    df.to_csv("../data_raw/currencyDataForCountry.csv", header=header, index=False)



if __name__ == '__main__':
        main()