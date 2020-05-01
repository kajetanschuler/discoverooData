
import pandas as pd


def main():
    cityData = pd.read_csv('../data_processed/cityData_regionCode.csv')

    cityDataIndexNames = cityData[cityData['cityName'].str.contains('Municipality|Kommun|of|City|city|municipality')].index
    cityData.drop(cityDataIndexNames, inplace=True)

    cityData.to_csv("../data_processed/cityData_clean.csv", index=False, header=True)
    #print(cityData.count(axis=1))


if __name__ == '__main__':
    main()

    # clean city data based on city names
    # indexName = merge_weather_stations_city_country_cultural_formation_beaches_image[merge_weather_stations_city_country_cultural_formation_beaches_image['cityName'].str.contains('Municipality|Kommun|of|City|city|municipality')].index
    # merge_weather_stations_city_country_cultural_formation_beaches_image.drop(indexName, inplace=True)