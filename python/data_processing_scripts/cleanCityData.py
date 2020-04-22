
import pandas as pd


def main():
    cityData = pd.read_csv('../data_processed/city_data_clean.csv')

    cityDataIndexNames = cityData[cityData['cityName'].str.contains('Municipality|Kommun|of|City|city|municipality')].index
    cityData.drop(cityDataIndexNames, inplace=True)

    cityData.to_csv("../data_final/cityData_final_clean.csv", index=False, header=True)
    #print(cityData.count(axis=1))

if __name__ == '__main__':
    main()