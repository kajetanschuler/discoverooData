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

    flagList = []
    url = 'https://restcountries.eu/rest/v2/all'
    r = requests.request("GET", url)
    data = json.loads(r.text)
    for country in data:
        countryCode = country['alpha2Code']
        flagLink = country['flag']

        flagTmp = [countryCode, flagLink]
        flagList.append(flagTmp)


    df = pd.DataFrame(flagList)
    print(df)
    df = df[df[1] != '(none)']
    print(df)
    header = ['countryCode', 'flagLink']
    df.to_csv("../data_processed/flagLinksForCountry.csv", header=header, index=False)



if __name__ == '__main__':
        main()