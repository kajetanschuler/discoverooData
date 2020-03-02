#
import pandas as pd


def main():
    pd.set_option('display.max_columns', 500)
    cost_data = pd.read_csv("../data_raw/costAndSafetyDataForCountry.csv")
    infrastructure_data = pd.read_csv("../data_temporary/qualityOfInfrastructure_temp.csv")
    infrastructure_data = infrastructure_data.drop('countryName', axis=1)
    country_data = pd.read_csv("../data_raw/countryData.csv")

    merge1 = pd.merge(left=infrastructure_data, right=cost_data, on="countryCode")

    merge2 = pd.merge(left=merge1, right=country_data, on="countryCode")

    merge2 = merge2.round(1)

    merge2.to_csv("../data_processed/countryData_clean.csv", index=False)
    merge2.to_csv("../data_final/countryData_final.csv", index=False)

    print("Merge Countries complete")


if __name__ == '__main__':
    main()