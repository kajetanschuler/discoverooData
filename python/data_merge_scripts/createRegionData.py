import pandas as pd

def main():


    regionIndex = pd.read_csv("../data_final/cityData_final.csv")
    regionIndex = regionIndex.drop(['stationId', 'cityId', 'cityName', 'type','lat','lon','population','elevation','timezone','image_links'],axis=1)

    regionIndex.loc[:, [x for x in regionIndex.columns if x.startswith('c')]]


    regionIndexModified=regionIndex.groupby(['regionCode','regionName','countryCode'], as_index=False).agg(['mean','min','max']).round().reset_index()
    regionIndexModified.fillna('')

    regionIndexModified.columns = regionIndexModified.columns.map(''.join).str.strip()

    regionIndexModified.columns = regionIndexModified.columns.str.replace('min','Min')
    regionIndexModified.columns = regionIndexModified.columns.str.replace('max', 'Max')
    regionIndexModified.columns = regionIndexModified.columns.str.replace('mean', 'Mean')


    regionIndexModified['uniqueRegionCode'] = regionIndexModified["countryCode"] + "_" + regionIndexModified["regionCode"]
    #regionIndexModified.loc[:,[x for x in regionIndex.columns if x.endswith('Index')]].round(0)

    columns = regionIndexModified.columns.tolist()
    columns = columns[-1:] + columns [:-1]
    regionIndexModified = regionIndexModified[columns]

    regionIndexModified.to_csv("../data_final/regionData_final.csv", index=False, header=True)

if __name__ == '__main__':
     main()

    #Check how many unique regions we have
    #print(regionIndex["regionCode"].nunique())


