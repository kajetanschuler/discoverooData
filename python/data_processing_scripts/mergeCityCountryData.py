# Script welches Country und City Daten zusammenführt
# Created - 07.02.2020 - by Kajetan & Malik

import pandas as pd


def main():
    pd.set_option('display.max_columns', 500)

    # Merge Country and Citie data to delete missing countries/cities
    cities = pd.read_csv("../data_raw/allCitiesOver100k.csv")
    countries = pd.read_csv("../data_processed/costAndQuality_clean.csv")

    merge = pd.merge(left=cities, right=countries, on="countryCode")

    merge = merge.drop(['cpiRentIndex', 'cpiIndex', 'groceriesIndex', 'purchasingPowerIndex', 'restaurantIndex',
                        'rentIndex', 'safetyIndex', 'crimeIndex', 'infrastructureValue1718'], axis=1)

    header = ['countryCode', 'type', 'cityName', 'cityId', 'regionName', 'population', 'regionCode', 'lat', 'lon', 'elevation', 'timezone']

    merge.to_csv("../data_processed/allCities_clean.csv", columns=header, index=False)

    print("Merge Country/Cities complete!")

    # Delete cities according to merged csv in sightsInCities.csv
    sights = pd.read_csv("../data_raw/sightsInCities.csv")
    cities2 = pd.read_csv("../data_processed/allCities_clean.csv")

    sights = sights.drop("population", axis=1)

    merge_sights_cities = pd.merge(left=cities2, right=sights, on="cityId")

    header.remove("cityId")
    header.remove("population")

    merge_sights_cities = merge_sights_cities.drop(header, axis=1)

    merge_sights_cities.to_csv("../data_processed/sightsInCities_clean.csv", index=False)

    print("Merge Cities/Sights complete")

    # Delete missing countries from beachesInCities.csv
    cities = pd.read_csv('../data_processed/allCities_clean.csv')
    beaches = pd.read_csv('../data_raw/beachesInCities.csv')

    drop_list = ['type', 'countryCode', 'cityName', 'regionName', 'regionCode', 'lat', 'lon',	'elevation', 'timezone']

    merge_beaches_cities = pd.merge(left=cities, right=beaches, on="cityId")

    merge_beaches_cities = merge_beaches_cities.drop(drop_list, axis=1)

    merge_beaches_cities.to_csv("../data_processed/beachesInCities_clean.csv", index=False)

    print("Merge City/Beaches complete")

    # Delete missing countries from geologicalFormationsInCities.csv
    cities = pd.read_csv('../data_processed/allCities_clean.csv')
    formations = pd.read_csv('../data_raw/geologicalInformationInCities.csv')

    cities = cities.drop('population', axis=1)

    merge_formations_cities = pd.merge(left=cities, right=formations, on="cityId")

    merge_formations_cities = merge_formations_cities.drop(drop_list, axis=1)

    merge_formations_cities.to_csv("../data_processed/formationsInCities_clean.csv", index=False)

    print("Merge City/Formations complete")


if __name__ == '__main__':
    main()