# Script converts region_final to region_level
import pandas as pd
import numpy as np


def main():
    city = pd.read_csv("../data_final/regionData_final.csv")
    max = city.max()
    min = city.min()
    mean = city.mean()
    hMax = city['culture_hIndexMean'].max()
    cMax = city['culture_cIndexMean'].max()
    rMax = city['culture_rIndexMean'].max()
    aMax = city['culture_aIndexMean'].max()
    iMax = city['culture_iIndexMean'].max()
    nMax = city['culture_nIndexMean'].max()

    fmMax = city['formations_mIndexMean'].max()
    frMax = city['formations_rIndexMean'].max()
    bMax = city['beach_IndexMean'].max()

    #cIndex
    city.loc[np.logical_and(city['culture_hIndexMean'] > hMax*0, city['culture_hIndexMean'] <= hMax * 0.2), 'culture_hIndexMean'] = 1
    city.loc[np.logical_and(city['culture_hIndexMean'] > hMax*0.2, city['culture_hIndexMean'] <= hMax * 0.4), 'culture_hIndexMean'] = 2
    city.loc[np.logical_and(city['culture_hIndexMean'] > hMax*0.4, city['culture_hIndexMean'] <= hMax * 0.6), 'culture_hIndexMean'] = 3
    city.loc[np.logical_and(city['culture_hIndexMean'] > hMax*0.6, city['culture_hIndexMean'] <= hMax * 0.8), 'culture_hIndexMean'] = 4
    city.loc[np.logical_and(city['culture_hIndexMean'] > hMax*0.8, city['culture_hIndexMean'] <= hMax), 'culture_hIndexMean'] = 5

    #hIndex
    city.loc[
        np.logical_and(city['culture_cIndexMean'] > cMax * 0, city['culture_cIndexMean'] <= cMax * 0.2), 'culture_cIndexMean'] = 1
    city.loc[
        np.logical_and(city['culture_cIndexMean'] > cMax * 0.2, city['culture_cIndexMean'] <= cMax * 0.4), 'culture_cIndexMean'] = 2
    city.loc[
        np.logical_and(city['culture_cIndexMean'] > cMax * 0.4, city['culture_cIndexMean'] <= cMax * 0.6), 'culture_cIndexMean'] = 3
    city.loc[
        np.logical_and(city['culture_cIndexMean'] > cMax * 0.6, city['culture_cIndexMean'] <= cMax * 0.8), 'culture_cIndexMean'] = 4
    city.loc[np.logical_and(city['culture_cIndexMean'] > cMax * 0.8, city['culture_cIndexMean'] <= cMax), 'culture_cIndexMean'] = 5

    # rIndex
    city.loc[
        np.logical_and(city['culture_rIndexMean'] > rMax * 0, city['culture_rIndexMean'] <= rMax * 0.2), 'culture_rIndexMean'] = 1
    city.loc[
        np.logical_and(city['culture_rIndexMean'] > rMax * 0.2, city['culture_rIndexMean'] <= rMax * 0.4), 'culture_rIndexMean'] = 2
    city.loc[
        np.logical_and(city['culture_rIndexMean'] > rMax * 0.4, city['culture_rIndexMean'] <= rMax * 0.6), 'culture_rIndexMean'] = 3
    city.loc[
        np.logical_and(city['culture_rIndexMean'] > rMax * 0.6, city['culture_rIndexMean'] <= rMax * 0.8), 'culture_rIndexMean'] = 4
    city.loc[np.logical_and(city['culture_rIndexMean'] > rMax * 0.8, city['culture_rIndexMean'] <= rMax), 'culture_rIndexMean'] = 5

    # aIndexMean
    city.loc[
        np.logical_and(city['culture_aIndexMean'] > aMax * 0, city['culture_aIndexMean'] <= aMax * 0.2), 'culture_aIndexMean'] = 1
    city.loc[
        np.logical_and(city['culture_aIndexMean'] > aMax * 0.2, city['culture_aIndexMean'] <= aMax * 0.4), 'culture_aIndexMean'] = 2
    city.loc[
        np.logical_and(city['culture_aIndexMean'] > aMax * 0.4, city['culture_aIndexMean'] <= aMax * 0.6), 'culture_aIndexMean'] = 3
    city.loc[
        np.logical_and(city['culture_aIndexMean'] > aMax * 0.6, city['culture_aIndexMean'] <= aMax * 0.8), 'culture_aIndexMean'] = 4
    city.loc[np.logical_and(city['culture_aIndexMean'] > aMax * 0.8, city['culture_aIndexMean'] <= aMax), 'culture_aIndexMean'] = 5

    # iIndexMean
    city.loc[
        np.logical_and(city['culture_iIndexMean'] > iMax * 0, city['culture_iIndexMean'] <= iMax * 0.2), 'culture_iIndexMean'] = 1
    city.loc[
        np.logical_and(city['culture_iIndexMean'] > iMax * 0.2, city['culture_iIndexMean'] <= iMax * 0.4), 'culture_iIndexMean'] = 2
    city.loc[
        np.logical_and(city['culture_iIndexMean'] > iMax * 0.4, city['culture_iIndexMean'] <= iMax * 0.6), 'culture_iIndexMean'] = 3
    city.loc[
        np.logical_and(city['culture_iIndexMean'] > iMax * 0.6, city['culture_iIndexMean'] <= iMax * 0.8), 'culture_iIndexMean'] = 4
    city.loc[np.logical_and(city['culture_iIndexMean'] > iMax * 0.8, city['culture_iIndexMean'] <= iMax), 'culture_iIndexMean'] = 5

    # nIndexMean
    city.loc[
        np.logical_and(city['culture_nIndexMean'] > nMax * 0, city['culture_nIndexMean'] <= nMax * 0.2), 'culture_nIndexMean'] = 1
    city.loc[
        np.logical_and(city['culture_nIndexMean'] > nMax * 0.2, city['culture_nIndexMean'] <= nMax * 0.4), 'culture_nIndexMean'] = 2
    city.loc[
        np.logical_and(city['culture_nIndexMean'] > nMax * 0.4, city['culture_nIndexMean'] <= nMax * 0.6), 'culture_nIndexMean'] = 3
    city.loc[
        np.logical_and(city['culture_nIndexMean'] > nMax * 0.6, city['culture_nIndexMean'] <= nMax * 0.8), 'culture_nIndexMean'] = 4
    city.loc[np.logical_and(city['culture_nIndexMean'] > nMax * 0.8, city['culture_nIndexMean'] <= nMax), 'culture_nIndexMean'] = 5

    # fmIndexMean
    city.loc[
        np.logical_and(city['formations_mIndexMean'] > fmMax * 0, city['formations_mIndexMean'] <= fmMax * 0.2), 'formations_mIndexMean'] = 1
    city.loc[
        np.logical_and(city['formations_mIndexMean'] > fmMax * 0.2, city['formations_mIndexMean'] <= fmMax * 0.4), 'formations_mIndexMean'] = 2
    city.loc[
        np.logical_and(city['formations_mIndexMean'] > fmMax * 0.4, city['formations_mIndexMean'] <= fmMax * 0.6), 'formations_mIndexMean'] = 3
    city.loc[
        np.logical_and(city['formations_mIndexMean'] > fmMax * 0.6, city['formations_mIndexMean'] <= fmMax * 0.8), 'formations_mIndexMean'] = 4
    city.loc[np.logical_and(city['formations_mIndexMean'] > fmMax * 0.8, city['formations_mIndexMean'] <= fmMax), 'formations_mIndexMean'] = 5

    # frIndexMean
    city.loc[
        np.logical_and(city['formations_rIndexMean'] > frMax * 0,
                       city['formations_rIndexMean'] <= frMax * 0.2), 'formations_rIndexMean'] = 1
    city.loc[
        np.logical_and(city['formations_rIndexMean'] > frMax * 0.2,
                       city['formations_rIndexMean'] <= frMax * 0.4), 'formations_rIndexMean'] = 2
    city.loc[
        np.logical_and(city['formations_rIndexMean'] > frMax * 0.4,
                       city['formations_rIndexMean'] <= frMax * 0.6), 'formations_rIndexMean'] = 3
    city.loc[
        np.logical_and(city['formations_rIndexMean'] > frMax * 0.6,
                       city['formations_rIndexMean'] <= frMax * 0.8), 'formations_rIndexMean'] = 4
    city.loc[np.logical_and(city['formations_rIndexMean'] > frMax * 0.8,
                            city['formations_rIndexMean'] <= frMax), 'formations_rIndexMean'] = 5

    #beachIndexMean
    city.loc[
        np.logical_and(city['beach_IndexMean'] > 0 ,
                       city['beach_IndexMean'] <= 4), 'beach_IndexMean'] = 1
    city.loc[
        np.logical_and(city['beach_IndexMean'] > 4,
                       city['beach_IndexMean'] <= 30), 'beach_IndexMean'] = 2
    city.loc[
        np.logical_and(city['beach_IndexMean'] > 30,
                       city['beach_IndexMean'] <= bMax ), 'beach_IndexMean'] = 3

    city.to_csv("../data_final/regionData_level.csv", index=False, header=True)

if __name__ == '__main__':
    main()