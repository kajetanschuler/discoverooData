import pandas as pd


def main():
    pd.set_option('display.max_columns', 500)
    cost_data = pd.read_csv("../data_raw/costAndSafetyDataForCountry.csv")
    infrastructure_data = pd.read_csv("../data_processed/qualityOfInfrastructure_clean.csv")
    print(infrastructure_data)

    merge = pd.merge(left=cost_data, right=infrastructure_data, on="countryCode")

    # header = ['countryCode', 'countryName', 'infrastructureValue1718', 'cpiRentIndex', 'cpiIndex', 'groceriesIndex',
    #           'purchasingPowerIndex', 'restaurantIndex', 'rentIndex', 'safetyIndex', 'crimeIndex']

    merge.to_csv("../data_processed/costAndQuality_clean.csv", index=False)

    print("Merge complete!")
    #print(merge)


if __name__ == '__main__':
    main()