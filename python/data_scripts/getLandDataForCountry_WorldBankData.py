# Sckript nutzt die WorldBank, um allgemeine Daten über die Länder zu holen
# Created - 12.01.2020 - by Kajetan

import requests
import json
import country_converter as coco
import csv


def main():
    response_size = requests.request("GET", "http://api.worldbank.org/v2/country/all/indicator/AG.LND.TOTL.K2?format=json&mrnev=1&per_page=10000")
    data_size = json.loads(response_size.text)

    response_population = requests.request("GET", "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&mrnev=1&per_page=10000")
    data_population = json.loads(response_population.text)

    response_rural = requests.request("GET", "http://api.worldbank.org/v2/country/all/indicator/AG.LND.TOTL.RU.K2?format=json&mrnev=1&per_page=10000")
    data_rural = json.loads(response_rural.text)

    response_urban = requests.request("GET", "http://api.worldbank.org/v2/country/all/indicator/AG.LND.TOTL.UR.K2?format=json&mrnev=1&per_page=10000")
    data_urban = json.loads(response_urban.text)

    response_forest = requests.request("GET", "http://api.worldbank.org/v2/country/all/indicator/AG.LND.FRST.K2?format=json&mrnev=1&per_page=10000")
    data_forest = json.loads(response_forest.text)

    with open('../data_raw/landDataForCountry.csv', 'wt') as output:
        fieldnames = ['countryName', 'countryCode', 'population', 'countrySizeKm2', 'urbanSizeKm2', 'ruralSizeKm2', 'forestSizeKm2']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for country in data_size[1]:
            iso3 = country['countryiso3code']
            iso2 = coco.convert(names=iso3, to='ISO2')
            rural_size = 0
            urban_size = 0
            country_size = 0
            forest_size = 0
            country_population = 0

            if iso2 != ('not found' or ''):
                country_size = country['value']
                country_name = country['country']['value']
#                writer.writerow({'country': iso2, 'size': size})
                for population in data_population[1]:
                    if population['countryiso3code'] == iso3:
                        country_population = population['value']

                for rural in data_rural[1]:
                    if rural['countryiso3code'] == iso3:
                        rural_size = rural['value']

                for urban in data_urban[1]:
                    if urban['countryiso3code'] == iso3:
                        urban_size = urban['value']

                for forest in data_forest[1]:
                    if forest['countryiso3code'] == iso3:
                        forest_size = forest['value']

                writer.writerow({'countryName': country_name, 'countryCode': iso2, 'population': country_population, 'countrySizeKm2': country_size, 'urbanSizeKm2': urban_size, 'ruralSizeKm2': rural_size, 'forestSizeKm2': forest_size})


if __name__ == '__main__':
    main()

