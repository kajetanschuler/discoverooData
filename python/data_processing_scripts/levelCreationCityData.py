# Script created 16.04.2020 by Malik
# Script wandelt city_final in city_level um

import pandas as pd
import numpy as np


def main():

    city = pd.read_csv("../data_final/cityData_final.csv")
    max = city.max()
    min = city.min()
    mean = city.mean()
    hMax = city['culture_hIndex'].max()
    cMax = city['culture_cIndex'].max()
    rMax = city['culture_aIndex'].max()
    aMax = city['culture_aIndex'].max()
    iMax = city['culture_aIndex'].max()
    nMax = city['culture_aIndex'].max()

    fmMax = city['formations_mIndex'].max()
    frMax = city['formations_rIndex'].max()
    bMax = city['beach_Index'].max()




    #cIndex
    city.loc[np.logical_and(city['culture_hIndex'] > hMax*0, city['culture_hIndex'] <= hMax * 0.2), 'culture_hIndex'] = 1
    city.loc[np.logical_and(city['culture_hIndex'] > hMax*0.2, city['culture_hIndex'] <= hMax * 0.4), 'culture_hIndex'] = 2
    city.loc[np.logical_and(city['culture_hIndex'] > hMax*0.4, city['culture_hIndex'] <= hMax * 0.6), 'culture_hIndex'] = 3
    city.loc[np.logical_and(city['culture_hIndex'] > hMax*0.6, city['culture_hIndex'] <= hMax * 0.8), 'culture_hIndex'] = 4
    city.loc[np.logical_and(city['culture_hIndex'] > hMax*0.8, city['culture_hIndex'] <= hMax), 'culture_hIndex'] = 5

    #hIndex
    city.loc[
        np.logical_and(city['culture_cIndex'] > cMax * 0, city['culture_cIndex'] <= cMax * 0.2), 'culture_cIndex'] = 1
    city.loc[
        np.logical_and(city['culture_cIndex'] > cMax * 0.2, city['culture_cIndex'] <= cMax * 0.4), 'culture_cIndex'] = 2
    city.loc[
        np.logical_and(city['culture_cIndex'] > cMax * 0.4, city['culture_cIndex'] <= cMax * 0.6), 'culture_cIndex'] = 3
    city.loc[
        np.logical_and(city['culture_cIndex'] > cMax * 0.6, city['culture_cIndex'] <= cMax * 0.8), 'culture_cIndex'] = 4
    city.loc[np.logical_and(city['culture_cIndex'] > cMax * 0.8, city['culture_cIndex'] <= cMax), 'culture_cIndex'] = 5

    # rIndex
    city.loc[
        np.logical_and(city['culture_rIndex'] > rMax * 0, city['culture_rIndex'] <= rMax * 0.2), 'culture_rIndex'] = 1
    city.loc[
        np.logical_and(city['culture_rIndex'] > rMax * 0.2, city['culture_rIndex'] <= rMax * 0.4), 'culture_rIndex'] = 2
    city.loc[
        np.logical_and(city['culture_rIndex'] > rMax * 0.4, city['culture_rIndex'] <= rMax * 0.6), 'culture_rIndex'] = 3
    city.loc[
        np.logical_and(city['culture_rIndex'] > rMax * 0.6, city['culture_rIndex'] <= rMax * 0.8), 'culture_rIndex'] = 4
    city.loc[np.logical_and(city['culture_rIndex'] > rMax * 0.8, city['culture_rIndex'] <= rMax), 'culture_rIndex'] = 5

    # aIndex
    city.loc[
        np.logical_and(city['culture_aIndex'] > aMax * 0, city['culture_aIndex'] <= aMax * 0.2), 'culture_aIndex'] = 1
    city.loc[
        np.logical_and(city['culture_aIndex'] > aMax * 0.2, city['culture_aIndex'] <= aMax * 0.4), 'culture_aIndex'] = 2
    city.loc[
        np.logical_and(city['culture_aIndex'] > aMax * 0.4, city['culture_aIndex'] <= aMax * 0.6), 'culture_aIndex'] = 3
    city.loc[
        np.logical_and(city['culture_aIndex'] > aMax * 0.6, city['culture_aIndex'] <= aMax * 0.8), 'culture_aIndex'] = 4
    city.loc[np.logical_and(city['culture_aIndex'] > aMax * 0.8, city['culture_aIndex'] <= aMax), 'culture_aIndex'] = 5

    # iIndex
    city.loc[
        np.logical_and(city['culture_iIndex'] > iMax * 0, city['culture_iIndex'] <= iMax * 0.2), 'culture_iIndex'] = 1
    city.loc[
        np.logical_and(city['culture_iIndex'] > iMax * 0.2, city['culture_iIndex'] <= iMax * 0.4), 'culture_iIndex'] = 2
    city.loc[
        np.logical_and(city['culture_iIndex'] > iMax * 0.4, city['culture_iIndex'] <= iMax * 0.6), 'culture_iIndex'] = 3
    city.loc[
        np.logical_and(city['culture_iIndex'] > iMax * 0.6, city['culture_iIndex'] <= iMax * 0.8), 'culture_iIndex'] = 4
    city.loc[np.logical_and(city['culture_iIndex'] > iMax * 0.8, city['culture_iIndex'] <= iMax), 'culture_iIndex'] = 5

    # nIndex
    city.loc[
        np.logical_and(city['culture_nIndex'] > nMax * 0, city['culture_nIndex'] <= nMax * 0.2), 'culture_nIndex'] = 1
    city.loc[
        np.logical_and(city['culture_nIndex'] > nMax * 0.2, city['culture_nIndex'] <= nMax * 0.4), 'culture_nIndex'] = 2
    city.loc[
        np.logical_and(city['culture_nIndex'] > nMax * 0.4, city['culture_nIndex'] <= nMax * 0.6), 'culture_nIndex'] = 3
    city.loc[
        np.logical_and(city['culture_nIndex'] > nMax * 0.6, city['culture_nIndex'] <= nMax * 0.8), 'culture_nIndex'] = 4
    city.loc[np.logical_and(city['culture_nIndex'] > nMax * 0.8, city['culture_nIndex'] <= nMax), 'culture_nIndex'] = 5

    # fmIndex
    city.loc[
        np.logical_and(city['formations_mIndex'] > fmMax * 0, city['formations_mIndex'] <= fmMax * 0.2), 'formations_mIndex'] = 1
    city.loc[
        np.logical_and(city['formations_mIndex'] > fmMax * 0.2, city['formations_mIndex'] <= fmMax * 0.4), 'formations_mIndex'] = 2
    city.loc[
        np.logical_and(city['formations_mIndex'] > fmMax * 0.4, city['formations_mIndex'] <= fmMax * 0.6), 'formations_mIndex'] = 3
    city.loc[
        np.logical_and(city['formations_mIndex'] > fmMax * 0.6, city['formations_mIndex'] <= fmMax * 0.8), 'formations_mIndex'] = 4
    city.loc[np.logical_and(city['formations_mIndex'] > fmMax * 0.8, city['formations_mIndex'] <= fmMax), 'formations_mIndex'] = 5

    # frIndex
    city.loc[
        np.logical_and(city['formations_rIndex'] > frMax * 0,
                       city['formations_rIndex'] <= frMax * 0.2), 'formations_rIndex'] = 1
    city.loc[
        np.logical_and(city['formations_rIndex'] > frMax * 0.2,
                       city['formations_rIndex'] <= frMax * 0.4), 'formations_rIndex'] = 2
    city.loc[
        np.logical_and(city['formations_rIndex'] > frMax * 0.4,
                       city['formations_rIndex'] <= frMax * 0.6), 'formations_rIndex'] = 3
    city.loc[
        np.logical_and(city['formations_rIndex'] > frMax * 0.6,
                       city['formations_rIndex'] <= frMax * 0.8), 'formations_rIndex'] = 4
    city.loc[np.logical_and(city['formations_rIndex'] > frMax * 0.8,
                            city['formations_rIndex'] <= frMax), 'formations_rIndex'] = 5

    #beachIndex
    city.loc[
        np.logical_and(city['beach_Index'] > 0 ,
                       city['beach_Index'] <= 4), 'beach_Index'] = 1
    city.loc[
        np.logical_and(city['beach_Index'] > 4,
                       city['beach_Index'] <= 30), 'beach_Index'] = 2
    city.loc[
        np.logical_and(city['beach_Index'] > 30,
                       city['beach_Index'] <= bMax ), 'beach_Index'] = 3



    city.to_csv("../data_final/city_data_level.csv", index=False)

if __name__ == '__main__':
    main()