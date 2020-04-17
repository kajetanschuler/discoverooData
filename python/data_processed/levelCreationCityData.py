# Script created 16.04.2020 by Malik
# Script wandelt city_data_final in city_data_level um

import pandas as pd
import numpy as np


def main():

    city_data = pd.read_csv("../data_final/cityData_final.csv")
    max = city_data.max()
    min = city_data.min()
    mean = city_data.mean()
    hMax = city_data['culture_hIndex'].max()

    city_data['culture_hIndex'].values[city_data['culture_hIndex'].values < hMax * 0.2] = 1
    city_data['culture_hIndex'].values[city_data['culture_hIndex'].values < hMax * 0.4 > hMax * 0.6] = 4
    city_data['culture_hIndex'].values[city_data['culture_hIndex'].values < hMax * 0.6] = 3
    city_data['culture_hIndex'].values[city_data['culture_hIndex'].values < hMax * 0.4] = 2
    city_data['culture_hIndex'].values[city_data['culture_hIndex'].values < hMax * 0.2] = 1

    city_data.to_csv("../data_final/city_data_level.csv", index=False)

if __name__ == '__main__':
    main()