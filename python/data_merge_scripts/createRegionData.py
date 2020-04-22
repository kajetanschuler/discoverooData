#Script creates Region Data as avergae from City Data
#created by Svenja on 31.05.20

import pandas as pd

def main():


    regionIndex = pd.read_csv("../data_processed/city_data_clean.csv")
    regionIndex = regionIndex.drop(['stationId', 'cityId', 'cityName', 'type','lat','lon','population','elevation','timezone','image_links'],axis=1)


    regionIndexModified=regionIndex.groupby(['regionCode','regionName','countryCode'], as_index=False).agg(['mean','min','max']).round().reset_index()
    regionIndexModified.fillna('')

    regionIndexModified.columns = regionIndexModified.columns.map(''.join).str.strip()

    regionIndexModified.columns = regionIndexModified.columns.str.replace('min','Min')
    regionIndexModified.columns = regionIndexModified.columns.str.replace('max', 'Max')
    regionIndexModified.columns = regionIndexModified.columns.str.replace('mean', 'Mean')


    regionIndexModified.to_csv("../data_final/regionData_final.csv", index=False, header=True)

if __name__ == '__main__':
     main()

    #Check how many unique regions we have
    #print(regionIndex["regionCode"].nunique())


