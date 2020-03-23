# Skript, das zusätzlich Sprache und Währung zu country_data_final hinzufügt
# created 23.03.2020 by Malik
# NOCH in BEARBEITUNG



import requests
import json
import pprint as pp
import pandas as pd




def main():
    country_data = pd.read_csv("../data_final/countryData_final.csv")
    print(country_data['countryCode'])

    url = 'https://restcountries.eu/rest/v2/all'
    response = requests.request("GET", url)
    data = json.loads(response.text)
    x = 0
    x = int(x)
    for country in data:
        country_id1 = country['alpha2Code']
        print(country_id1)
        # country_id2 = country_data['countryCode']
        # if country_id1 == country_id2:
        #     print('yes')



if __name__ == '__main__':
        main()