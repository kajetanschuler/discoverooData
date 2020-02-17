# Script to calculate Index based on the beachesInCities.csv
# Created - 17.02.2020 - by Kajetan

import pandas as pd

import pandas as pd


def main():

    beaches = pd.read_csv("../data_processed/beachesInCities_clean.csv")

    beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1", "rCountLevel1", "nCountLevel1",
             "uCountLevel1", "oCountLevel1"]] = beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1",
                                                         "rCountLevel1", "nCountLevel1", "uCountLevel1",
                                                         "oCountLevel1"]].apply(lambda x: x * 2)

    beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1", "rCountLevel1", "nCountLevel1",
             "uCountLevel1", "oCountLevel1"]] = beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1",
                                                         "rCountLevel1", "nCountLevel1", "uCountLevel1",
                                                         "oCountLevel1"]].apply(lambda x: x * 3)

    beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1", "rCountLevel1", "nCountLevel1",
             "uCountLevel1", "oCountLevel1"]] = beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1",
                                                         "rCountLevel1", "nCountLevel1", "uCountLevel1",
                                                         "oCountLevel1"]].apply(lambda x: x * 4)

    beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1", "rCountLevel1", "nCountLevel1",
             "uCountLevel1", "oCountLevel1"]] = beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1",
                                                         "rCountLevel1", "nCountLevel1", "uCountLevel1",
                                                         "oCountLevel1"]].apply(lambda x: x * 6)

    beaches[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
            "iCountLevel2", "nCountLevel2"]] = beaches[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
                                                       "iCountLevel2", "nCountLevel2"]].apply(lambda x: x * 3)

    beaches[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
            "iCountLevel3", "nCountLevel3"]] = beaches[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
                                                       "iCountLevel3", "nCountLevel3"]].apply(lambda x: x * 4)

    beaches[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
            "iCountLevel7", "nCountLevel7"]] = beaches[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
                                                       "iCountLevel7", "nCountLevel7"]].apply(lambda x: x * 6)

    beaches['beach_gIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('gCount')]].sum(axis=1)
    beaches['beach_wIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('wCount')]].sum(axis=1)
    beaches['beach_bIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('bCount')]].sum(axis=1)
    beaches['beach_sIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('sCount')]].sum(axis=1)
    beaches['beach_rIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('rCount')]].sum(axis=1)
    beaches['beach_nIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('nCount')]].sum(axis=1)
    beaches['beach_uIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('uCount')]].sum(axis=1)
    beaches['beach_oIndex'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('oCount')]].sum(axis=1)

    header = ['cityId', 'searchRadius', 'beach_gIndex', 'beach_wIndex', 'beach_bIndex', 'beach_sIndex', 'beach_rIndex',
              'beach_nIndex', 'beach_uIndex', 'beach_oIndex']

    beaches = beaches[header]

    beaches.to_csv("../data_processed/beach_indices.csv", columns=header, index=False)


if __name__ == '__main__':
    main()