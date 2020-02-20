# Skript führt alle processed Daten zu einer Datei zusammen
# Created - 20.02.2020 - by Kajetan & Malik

import pandas as pd

def main():

    weather_data = pd.read_csv('../data_processed/weatherData_clean.csv')
    weather_data = weather_data['stationId']

    weather_stations = pd.read_csv('../data_raw/weatherDataPerStation/weatherStationsByCity.csv')
    merge_weather_stations_data = pd.merge(left=weather_data, right=weather_stations, on='stationId')

    city_data = pd.read_csv('../data_raw/allCitiesOver100k.csv')
    merge_weather_stations_city = pd.merge(left=merge_weather_stations_data, right=city_data, on='cityId')

    country_data = pd.read_csv('../data_processed/countryData_clean.csv')
    merge_weather_stations_city_country = pd.merge(left=merge_weather_stations_city, right=country_data,
                                                   on='countryCode')

    cultural = pd.read_csv('../data_processed/cultural_indices.csv')
    merge_weather_stations_city_country_cultural = pd.merge(left=merge_weather_stations_city_country, right=cultural,
                                                            on='cityId')

    formation = pd.read_csv('../data_processed/formation_indices.csv')
    merge_weather_stations_city_country_cultural_formation = pd.merge(left=merge_weather_stations_city_country_cultural,
                                                                      right=formation, on='cityId')

    beaches = pd.read_csv('../data_processed/beach_indices.csv')
    merge_weather_stations_city_country_cultural_formation_beaches = \
        pd.merge(left=merge_weather_stations_city_country_cultural_formation, right=formation, on='cityId')


if __name__ == '__main__':
    main()