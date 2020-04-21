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

    languageList = []
    url = 'https://restcountries.eu/rest/v2/all'
    r = requests.request("GET", url)
    data = json.loads(r.text)
    for country in data:
        countryCode = country['alpha2Code']
        flagLink = country['flag']
        languages = country['languages']
        for language in languages:

            languageCode = language['iso639_2']
            languageName = language['name']
            languageTmp = [countryCode, languageCode, languageName]
            languageList.append(languageTmp)

    df = pd.DataFrame(languageList)
    print(df)
    df = df[df[1] != '(none)']
    print(df)
    header = ['countryCode', 'languageCode', 'languageName']
    df.to_csv("../data_raw/languageForCountry.csv", header=header, index=False)


if __name__ == '__main__':
        main()