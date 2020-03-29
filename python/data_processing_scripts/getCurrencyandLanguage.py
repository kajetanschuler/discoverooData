# Skript, das zusätzlich Sprache und Währung zu country_data_final hinzufügt
# created 23.03.2020 by Malik
# NOCH in BEARBEITUNG



import requests
import json
import pprint as pp
import pandas as pd
from pandas.io.json import json_normalize
import pprint as pp
from IPython.display import display, HTML




def main():

    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.request("GET", url).json()

    countryCode = []
    capitals =[]
    currency = []

    for country in response:


        countryCode = country['alpha2Code']
        print(countryCode)
        capitals = country['capital']
        print(capitals)
        currency = country['currencies'][0]['name']
        print(currency)

    df = pd.DataFrame()
    df['countryCode'] = countryCode
    df['capitals'] = capitals
    df['currency'] = currency
    

    #df.to_csv("../data_raw/currencyAndLanguage.csv")



if __name__ == '__main__':
        main()