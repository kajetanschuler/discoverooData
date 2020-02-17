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

    header = ['cityId', 'searchRadius', 'population',
                  'hCountLevel0', 'hCountLevel1', 'hCountLevel2', 'hCountLevel3', 'hCountLevel7',
                  'cCountLevel0', 'cCountLevel1', 'cCountLevel2', 'cCountLevel3', 'cCountLevel7',
                  'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7',
                  'aCountLevel0', 'aCountLevel1', 'aCountLevel2', 'aCountLevel3', 'aCountLevel7',
                  'iCountLevel0', 'iCountLevel1', 'iCountLevel2', 'iCountLevel3', 'iCountLevel7',
                  'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7']

    merge_sights_cities.to_csv("../data_processed/sightsInCities_clean.csv", columns=header, index=False)

    print("merge Cities/Sights complete")

    # Delete missing countries from beachesInCities.csv
    cities = pd.read_csv('../data_processed/allCities_clean.csv')
    beaches = pd.read_csv('../data_raw/beachesInCities.csv')

    drop_list = ['type', 'countryCode', 'cityName', 'regionName', 'regionCode', 'lat', 'lon',	'elevation', 'timezone']
    header = ['cityId', 'gCountLevel0', 'gCountLevel1', 'gCountLevel2', 'gCountLevel3', 'gCountLevel7', 'wCountLevel0',
              'wCountLevel1', 'wCountLevel2', 'wCountLevel3', 'wCountLevel7', 'bCountLevel0', 'bCountLevel1',
              'bCountLevel2', 'bCountLevel3', 'bCountLevel7', 'sCountLevel0', 'sCountLevel1', 'sCountLevel2',
              'sCountLevel3', 'sCountLevel7', 'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3',
              'rCountLevel7', 'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7',
              'uCountLevel0', 'uCountLevel1', 'uCountLevel2', 'uCountLevel3', 'uCountLevel7', 'oCountLevel0',
              'oCountLevel1', 'oCountLevel2', 'oCountLevel3', 'oCountLevel7']

    merge_beaches_cities = pd.merge(left=cities, right=beaches, on="cityId")

    merge_beaches_cities = merge_beaches_cities.drop(drop_list, axis=1)

    merge_beaches_cities.to_csv("../data_processed/beachesInCities_clean.csv", columns=header, index=False)

    print("Merge City/Beaches complete")

    # Delete missing countries from geologicalFormationsInCities.csv
    cities = pd.read_csv('../data_processed/allCities_clean.csv')
    formations = pd.read_csv('../data_raw/geologicalInformationInCities.csv')

    cities = cities.drop('population', axis=1)

    header = ['cityId', 'population', 'mCountLevel0', 'mCountLevel1', 'mCountLevel2', 'mCountLevel3',
              'mCountLevel7', 'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7']

    merge_formations_cities = pd.merge(left=cities, right=formations, on="cityId")

    merge_formations_cities = merge_formations_cities.drop(drop_list, axis=1)

    merge_formations_cities.to_csv("../data_processed/formationsInCities_clean.csv", columns=header, index=False)

    print("Merge City/Formations complete")


if __name__ == '__main__':
    main()