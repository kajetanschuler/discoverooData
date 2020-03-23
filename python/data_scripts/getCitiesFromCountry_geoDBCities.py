# Skript holt allgemeine Städte und deren Daten über die GeoDBCities API
# Created - 27.12.2019 - by Kajetan

import requests
import json
import time
import csv


def main():
    #country_list = ["IT", "ES", "TH", "IN", "SE", "DK", "BR", "AR", "CA", "ZA", "EG", "JP", "AU", "PL", "ME"]

    more_data = True
    total_count = 0
    count = 0
    offset = 0
    csv_file_name = "../data_raw/allCitiesBelow100k" + ".csv"
    with open(csv_file_name, mode='a') as file:
        z = csv.reader(file, delimiter='\t')

    with open(csv_file_name, mode='w') as csv_file:
        fieldnames = ['countryCode', 'type', 'cityName', 'cityId', 'regionName', 'regionCode', 'lat', 'lon', 'population', 'elevation', 'timezone']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        try:

            while more_data:
                url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
                querystring = {"limit": "100", "minPopulation": 100000, "offset": offset}
                headers = {
                    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
                    'x-rapidapi-key': "e1f6061817mshb6a5d107db1f20fp1b58cejsn545de208fcf6"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                data = json.loads(response.text)


                if total_count == 0:
                    total_count = data['metadata']['totalCount']

                country_code = ""
                city_name = ""
                city_id = ""
                region_name = ""
                region_code = ""
                latitude = ""
                longitude = ""
                type = ""

                if 'data' in data:

                    for x in data['data']:

                        if 'countryCode' in x:
                            country_code = x['countryCode']

                        if 'name' in x:
                            city_name = x['name']

                        if 'id' in x:
                            city_id = x['id']

                        if 'region' in x:
                            region_name = x['region']

                        if 'regionCode' in x:
                            region_code = x['regionCode']

                        if 'latitude' in x:
                            latitude = x['latitude']

                        if 'longitude' in x:
                            longitude = x['longitude']

                        if 'type' in x:
                            type = x['type']

                        count += 1

                        url = "https://wft-geo-db.p.mashape.com/v1/geo/cities/" + str(city_id)
                        headers = {
                            'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
                            'x-rapidapi-key': "e1f6061817mshb6a5d107db1f20fp1b58cejsn545de208fcf6"
                        }
                        response = requests.request("GET", url, headers=headers, params=querystring)
                        pop_data = json.loads(response.text)
                        pop_data = pop_data['data']

                        population = ""
                        elevation = ""
                        timezone = ""

                        if 'population' in pop_data:
                            population = pop_data['population']

                        if 'elevationMeters' in pop_data:
                            elevation = pop_data['elevationMeters']

                        if 'timezone' in pop_data:
                            timezone = pop_data['timezone']

                        if type != "ADM2":
                            writer.writerow({'countryCode': country_code, 'type': type, 'cityName': city_name, 'cityId': city_id,
                                             'regionName': region_name, 'regionCode': region_code, 'lat': latitude,
                                             'lon': longitude, 'population': population, 'elevation': elevation, 'timezone': timezone})

                            print("City - " + str(count) + " of " + str(total_count) + " - inserted!")

                        time.sleep(0.1)

                print(str(count) + " of " + str(total_count))
                offset += 100

                if count == total_count:
                    more_data = False
                    print( csv_file_name + ": Completed!")

        except requests.exceptions.RequestException as e:
            print(e)


if __name__ == '__main__':
    main()
