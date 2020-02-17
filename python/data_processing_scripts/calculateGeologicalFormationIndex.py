# Script to calculate Index based on the geologicalInformationInCities.csv
# Created - 17.02.2020 - by Kajetan

import pandas as pd

import pandas as pd

def main():

    formations = pd.read_csv("../data_processed/sightsInCities_clean.csv")

    sights[["hCountLevel1", "cCountLevel1", "rCountLevel1", "aCountLevel1",
            "iCountLevel1", "nCountLevel1"]] = sights[["hCountLevel1", "cCountLevel1", "rCountLevel1", "aCountLevel1",
                                                       "iCountLevel1", "nCountLevel1"]].apply(lambda x: x * 2)

    sights[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
            "iCountLevel2", "nCountLevel2"]] = sights[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
                                                       "iCountLevel2", "nCountLevel2"]].apply(lambda x: x * 3)

    sights[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
            "iCountLevel3", "nCountLevel3"]] = sights[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
                                                       "iCountLevel3", "nCountLevel3"]].apply(lambda x: x * 4)

    sights[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
            "iCountLevel7", "nCountLevel7"]] = sights[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
                                                       "iCountLevel7", "nCountLevel7"]].apply(lambda x: x * 6)

    sights['hIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('hCount')]].sum(axis=1)
    sights['cIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('cCount')]].sum(axis=1)
    sights['rIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('rCount')]].sum(axis=1)
    sights['aIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('aCount')]].sum(axis=1)
    sights['iIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('iCount')]].sum(axis=1)
    sights['nIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('nCount')]].sum(axis=1)

    header = ['cityId', 'searchRadius', 'hIndex', 'cIndex', 'rIndex', 'aIndex', 'iIndex', 'nIndex']

    sights = sights[header]

    sights.to_csv("../data_processed/cultural_indices.csv", columns=header, index=False)


if __name__ == '__main__':
    main()