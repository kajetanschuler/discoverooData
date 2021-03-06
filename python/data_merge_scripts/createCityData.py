# Skript führt alle processed Daten zu einer Datei zusammen
# Created - 20.02.2020 - by Kajetan & Malik

import pandas as pd


def main():

    weather_data = pd.read_csv('../data_final/weatherData_final.csv')
    weather_data = weather_data['stationId']

    weather_stations = pd.read_csv('../data_raw/weatherStationsByCity_50km.csv')
    weather_stations = weather_stations[['cityId', 'stationId']]
    merge_weather_stations_data = pd.merge(left=weather_stations, right=weather_data, on='stationId')
    #print("Merge Weather complete")

    city_data = pd.read_csv('../data_processed/cityData_clean.csv')
    merge_weather_stations_city = pd.merge(left=merge_weather_stations_data, right=city_data, on='cityId')
    #print("Merge City & Weather complete")

    country_data = pd.read_csv('../data_final/countryData_final.csv')
    country_data = country_data['countryCode']
    merge_weather_stations_city_country = pd.merge(left=merge_weather_stations_city, right=country_data,
                                                   on='countryCode')
    #print("Merge City & Weather & Country complete")

    cultural = pd.read_csv('../data_processed/Indices/culturalIndices.csv')
    cultural = cultural.drop('searchRadius', axis=1)
    merge_weather_stations_city_country_cultural = pd.merge(left=merge_weather_stations_city_country, right=cultural,
                                                            on='cityId')
    #print("Merge City & Country & Country & Culture complete")

    formation = pd.read_csv('../data_processed/Indices/formationIndices.csv')
    formation = formation.drop('searchRadius', axis=1)
    merge_weather_stations_city_country_cultural_formation = pd.merge(left=merge_weather_stations_city_country_cultural,
                                                                      right=formation, on='cityId')
    #print("Merge City & Country & Country & Culture & Formations complete")


    beaches = pd.read_csv('../data_processed/Indices/beachIndices.csv')
    beaches = beaches.drop('searchRadius', axis=1)
    merge_weather_stations_city_country_cultural_formation_beaches = \
        pd.merge(left=merge_weather_stations_city_country_cultural_formation, right=beaches, on='cityId')
    #print("Merge City & Country & Country & Culture & Formations & Beaches complete")

    imageLinks = pd.read_csv("../data_processed/cityImagePath.csv")
    merge_weather_stations_city_country_cultural_formation_beaches_image = pd.merge\
        (left=merge_weather_stations_city_country_cultural_formation_beaches, right=imageLinks, on='cityId')
    #print("Merge City & Country & Country & Culture & Formations & Beaches & image complete")

    merge_weather_stations_city_country_cultural_formation_beaches_image.to_csv("../data_final/cityData_final.csv", encoding='utf-8', index=False)

if __name__ == '__main__':
    main()