# Script to calculate Index based on the geologicalInformationInCities.csv
# Created - 17.02.2020 - by Kajetan


import pandas as pd

import pandas as pd

def main():

    formations = pd.read_csv("../data_raw/geologicalInformationInCities.csv")

    formations[["mCountLevel0", "rCountLevel0"]] = formations[["mCountLevel0", "rCountLevel0"]].apply(lambda x: x * 0)

    formations[["mCountLevel1", "rCountLevel1"]] = formations[["mCountLevel1", "rCountLevel1"]].apply(lambda x: x * 2)

    formations[["mCountLevel2", "rCountLevel2"]] = formations[["mCountLevel2", "rCountLevel2"]].apply(lambda x: x * 3)

    formations[["mCountLevel3", "rCountLevel3"]] = formations[["mCountLevel3", "rCountLevel3"]].apply(lambda x: x * 4)

    formations[["mCountLevel7", "rCountLevel7"]] = formations[["mCountLevel7", "rCountLevel7"]].apply(lambda x: x * 6)

    formations['formations_mIndex'] = formations.loc[:, [x for x in formations.columns if x.startswith('mCount')]].sum(axis=1)

    formations['formations_rIndex'] = formations.loc[:, [x for x in formations.columns if x.startswith('rCount')]].sum(axis=1)
    header = ['cityId', 'searchRadius', 'formations_mIndex', 'formations_rIndex']

    formations = formations[header]

    formations.to_csv("../data_processed/formation_indices.csv", columns=header, index=False)


if __name__ == '__main__':
    main()