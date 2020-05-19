# Script to calculate Index based on the beachesInCities.csv
# Created - 17.02.2020 - by Kajetan

# Update by Malik: All beach indices were added to one beach index
# Updates 07.04.2020

import pandas as pd

import pandas as pd


def main():

    beaches = pd.read_csv("../data_raw/beachesInCities.csv")

    beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1", "rCountLevel1", "nCountLevel1",
             "uCountLevel1", "oCountLevel1"]] = beaches[["gCountLevel1", "wCountLevel1", "bCountLevel1", "sCountLevel1",
                                                         "rCountLevel1", "nCountLevel1", "uCountLevel1",
                                                         "oCountLevel1"]].apply(lambda x: x * 2)

    beaches[["gCountLevel2", "wCountLevel2", "bCountLevel2", "sCountLevel2", "rCountLevel2", "nCountLevel2",
             "uCountLevel2", "oCountLevel2"]] = beaches[["gCountLevel2", "wCountLevel2", "bCountLevel2", "sCountLevel2",
                                                         "rCountLevel2", "nCountLevel2", "uCountLevel2",
                                                         "oCountLevel2"]].apply(lambda x: x * 3)

    beaches[["gCountLevel3", "wCountLevel3", "bCountLevel3", "sCountLevel3", "rCountLevel3", "nCountLevel3",
             "uCountLevel3", "oCountLevel3"]] = beaches[["gCountLevel3", "wCountLevel3", "bCountLevel3", "sCountLevel3",
                                                         "rCountLevel3", "nCountLevel3", "uCountLevel3",
                                                         "oCountLevel3"]].apply(lambda x: x * 4)

    beaches[["gCountLevel7", "wCountLevel7", "bCountLevel7", "sCountLevel7", "rCountLevel7", "nCountLevel7",
             "uCountLevel7", "oCountLevel7"]] = beaches[["gCountLevel7", "wCountLevel7", "bCountLevel7", "sCountLevel7",
                                                         "rCountLevel7", "nCountLevel7", "uCountLevel7",
                                                         "oCountLevel7"]].apply(lambda x: x * 6)

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

    beaches['beach_Index'] = beaches.loc[:, [x for x in beaches.columns if x.startswith('beach')]].sum(axis=1)

    header = ['cityId', 'searchRadius', 'beach_Index']

    beaches = beaches[header]

    beaches.to_csv("../data_processed/Indices/beachIndices.csv", columns=header, index=False)


if __name__ == '__main__':
    main()