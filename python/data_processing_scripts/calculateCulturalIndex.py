import pandas as pd

def main():

    sights = pd.read_csv("../data_raw/sightsInCities.csv")

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

    sights['culture_hIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('hCount')]].sum(axis=1)
    sights['culture_cIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('cCount')]].sum(axis=1)
    sights['culture_rIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('rCount')]].sum(axis=1)
    sights['culture_aIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('aCount')]].sum(axis=1)
    sights['culture_iIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('iCount')]].sum(axis=1)
    sights['culture_nIndex'] = sights.loc[:, [x for x in sights.columns if x.startswith('nCount')]].sum(axis=1)

    header = ['cityId', 'searchRadius', 'culture_hIndex', 'culture_cIndex', 'culture_rIndex', 'culture_aIndex',
              'culture_iIndex', 'culture_nIndex']

    sights = sights[header]

    sights.to_csv("../data_processed/cultural_indices.csv", columns=header, index=False)


if __name__ == '__main__':
    main()