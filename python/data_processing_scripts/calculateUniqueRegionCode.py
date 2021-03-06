#script created unique region code and replaces old region Code
#created by Svenja on 22.04.20

import pandas as pd


def main():

     CityData = pd.read_csv("../data_raw/allCitiesOver100k.csv")
     CityData['uniqueRegionCode'] = CityData["countryCode"] + "_" + CityData["regionCode"]
     CityData = CityData.drop('regionCode', axis=1)

     CityData = CityData.rename(columns={"uniqueRegionCode": "regionCode"})

     CityData = CityData[['countryCode','type','cityId','cityName', 'regionCode','regionName','lat','lon','population','elevation','timezone']]

     CityData.to_csv("../data_processed/cityData_regionCode.csv", index=False, header=True)


if __name__ == '__main__':
     main()