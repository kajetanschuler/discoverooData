import pandas as pd


def main():

    costData = pd.read_csv("../data_raw/costAndSafetyDataForCountry.csv")
    infrastructureData = pd.read_csv("../data_processed/qualityOfInfrastructure_clean.csv")

    merge = pd.merge(left=costData, right=infrastructureData, on="countryCode")

    # header = ['countryCode', 'countryName', 'infrastructureValue1718', 'cpiRentIndex', 'cpiIndex', 'groceriesIndex',
    #           'purchasingPowerIndex', 'restaurantIndex', 'rentIndex', 'safetyIndex', 'crimeIndex']

    merge.to_csv("../data_processed/costAndQuality_clean.csv", index=False)

    print("Merge complete!")
    print(merge)


if __name__ == '__main__':
    main()