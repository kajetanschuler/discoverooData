import pandas as pd

def main():

    # Merge Country and Citie data to delete missing countries/cities
    cities = pd.read_csv("../data_raw/allCitiesOver100k.csv")
    countries = pd.read_csv("../data_raw/costAndSafetyDataForCountry.csv")

    merge = pd.merge(left=cities, right=countries, on="countryCode")

    merge = merge.drop(['cpiRentIndex', 'cpiIndex', 'groceriesIndex', 'purchasingPowerIndex', 'restaurantIndex',
                        'rentIndex', 'safetyIndex', 'crimeIndex'], axis=1)

    header = ['countryCode', 'type', 'cityName', 'cityId', 'regionName', 'population', 'regionCode', 'lat', 'lon', 'elevation', 'timezone']

    merge.to_csv("../data_processed/allCities_clean.csv", columns=header, index=False)

    print("Merge complete!")

    # Delete cities according to merged csv in sightsInCities.csv
    sights = pd.read_csv("../data_raw/sightsInCities.csv")
    cities2 = pd.read_csv("../data_processed/allCities_clean.csv")

    sights = sights.drop("population", axis=1)

    merge_sights_cities = pd.merge(left=cities2, right=sights, on="cityId")

    header.remove("cityId")
    header.remove("population")

    merge_sights_cities = merge_sights_cities.drop(header, axis=1)

    header = ['cityId', 'searchRadius', 'population',
                  'hCountLevel0', 'hCountLevel1', 'hCountLevel2', 'hCountLevel3', 'hCountLevel7',
                  'cCountLevel0', 'cCountLevel1', 'cCountLevel2', 'cCountLevel3', 'cCountLevel7',
                  'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7',
                  'aCountLevel0', 'aCountLevel1', 'aCountLevel2', 'aCountLevel3', 'aCountLevel7',
                  'iCountLevel0', 'iCountLevel1', 'iCountLevel2', 'iCountLevel3', 'iCountLevel7',
                  'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7']

    merge_sights_cities.to_csv("../data_processed/sightsInCities_clean.csv", columns=header, index=False)

    print("merge 2 complete")


if __name__ == '__main__':
    main()