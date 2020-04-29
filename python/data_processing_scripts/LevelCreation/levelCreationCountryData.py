# Script created 19.04.2020 by Malik
# Script wandelt city_final in city_level um

import pandas as pd
import numpy as np


def main():
    country = pd.read_csv("../../data_final/countryData_final.csv")

    cpiRMax = country['cpiRentIndex'].max()
    cpiMax = country['cpiIndex'].max()
    groMax = country['groceriesIndex'].max()
    ppMax = country['purchasingPowerIndex'].max()
    resMax = country['restaurantIndex'].max()
    rentMax = country['rentIndex'].max()
    safMax = country['safetyIndex'].max()
    crMax = country['crimeIndex'].max()

    print(cpiRMax)
    print(ppMax)
    country.loc[np.logical_and(country['infrastructureValue'] > 1, country['infrastructureValue'] <= 2.2), 'infrastructureValue'] = 1
    country.loc[np.logical_and(country['infrastructureValue'] > 2.2, country['infrastructureValue'] <= 3.4), 'infrastructureValue'] = 2
    country.loc[np.logical_and(country['infrastructureValue'] > 3.4, country['infrastructureValue'] <= 4.6), 'infrastructureValue'] = 3
    country.loc[np.logical_and(country['infrastructureValue'] > 4.6, country['infrastructureValue'] <= 5.8), 'infrastructureValue'] = 4
    country.loc[np.logical_and(country['infrastructureValue'] > 5.8, country['infrastructureValue'] <= 7), 'infrastructureValue'] = 5

    #cpi + rent Index
    country.loc[np.logical_and(country['cpiRentIndex'] > cpiRMax * 0,
                               country['cpiRentIndex'] <= cpiRMax * 0.2), 'cpiRentIndex'] = 1
    country.loc[np.logical_and(country['cpiRentIndex'] > cpiRMax * 0.2,
                               country['cpiRentIndex'] <= cpiRMax * 0.4), 'cpiRentIndex'] = 2
    country.loc[np.logical_and(country['cpiRentIndex'] > cpiRMax * 0.4,
                               country['cpiRentIndex'] <= cpiRMax * 0.6), 'cpiRentIndex'] = 3
    country.loc[np.logical_and(country['cpiRentIndex'] > cpiRMax * 0.6,
                               country['cpiRentIndex'] <= cpiRMax * 0.8), 'cpiRentIndex'] = 4
    country.loc[np.logical_and(country['cpiRentIndex'] > cpiRMax * 0.8,
                               country['cpiRentIndex'] <= cpiRMax), 'cpiRentIndex'] = 5

    #CPI Index
    country.loc[np.logical_and(country['cpiIndex'] > cpiMax * 0,
                               country['cpiIndex'] <= cpiMax * 0.2), 'cpiIndex'] = 1
    country.loc[np.logical_and(country['cpiIndex'] > cpiMax * 0.2,
                               country['cpiIndex'] <= cpiMax * 0.4), 'cpiIndex'] = 2
    country.loc[np.logical_and(country['cpiIndex'] > cpiMax * 0.4,
                               country['cpiIndex'] <= cpiMax * 0.6), 'cpiIndex'] = 3
    country.loc[np.logical_and(country['cpiIndex'] > cpiMax * 0.6,
                               country['cpiIndex'] <= cpiMax * 0.8), 'cpiIndex'] = 4
    country.loc[np.logical_and(country['cpiIndex'] > cpiMax * 0.8,
                               country['cpiIndex'] <= cpiMax), 'cpiIndex'] = 5

    #Groceries Index
    country.loc[np.logical_and(country['groceriesIndex'] > groMax * 0,
                               country['groceriesIndex'] <= groMax * 0.2), 'groceriesIndex'] = 1
    country.loc[np.logical_and(country['groceriesIndex'] > groMax * 0.2,
                               country['groceriesIndex'] <= groMax * 0.4), 'groceriesIndex'] = 2
    country.loc[np.logical_and(country['groceriesIndex'] > groMax * 0.4,
                               country['groceriesIndex'] <= groMax * 0.6), 'groceriesIndex'] = 3
    country.loc[np.logical_and(country['groceriesIndex'] > groMax * 0.6,
                               country['groceriesIndex'] <= groMax * 0.8), 'groceriesIndex'] = 4
    country.loc[np.logical_and(country['groceriesIndex'] > groMax * 0.8,
                               country['groceriesIndex'] <= groMax), 'groceriesIndex'] = 5

    #Purchasing Power Index
    country.loc[np.logical_and(country['purchasingPowerIndex'] > ppMax * 0,
                               country['purchasingPowerIndex'] <= ppMax * 0.2), 'purchasingPowerIndex'] = 1
    country.loc[np.logical_and(country['purchasingPowerIndex'] > ppMax * 0.2,
                               country['purchasingPowerIndex'] <= ppMax * 0.4), 'purchasingPowerIndex'] = 2
    country.loc[np.logical_and(country['purchasingPowerIndex'] > ppMax * 0.4,
                               country['purchasingPowerIndex'] <= ppMax * 0.6), 'purchasingPowerIndex'] = 3
    country.loc[np.logical_and(country['purchasingPowerIndex'] > ppMax * 0.6,
                               country['purchasingPowerIndex'] <= ppMax * 0.8), 'purchasingPowerIndex'] = 4
    country.loc[np.logical_and(country['purchasingPowerIndex'] > ppMax * 0.8,
                               country['purchasingPowerIndex'] <= ppMax), 'purchasingPowerIndex'] = 5

    #restaurant Index
    country.loc[np.logical_and(country['restaurantIndex'] > resMax * 0,
                               country['restaurantIndex'] <= resMax * 0.2), 'restaurantIndex'] = 1
    country.loc[np.logical_and(country['restaurantIndex'] > resMax * 0.2,
                               country['restaurantIndex'] <= resMax * 0.4), 'restaurantIndex'] = 2
    country.loc[np.logical_and(country['restaurantIndex'] > resMax * 0.4,
                               country['restaurantIndex'] <= resMax * 0.6), 'restaurantIndex'] = 3
    country.loc[np.logical_and(country['restaurantIndex'] > resMax * 0.6,
                               country['restaurantIndex'] <= resMax * 0.8), 'restaurantIndex'] = 4
    country.loc[np.logical_and(country['restaurantIndex'] > resMax * 0.8,
                               country['restaurantIndex'] <= resMax), 'restaurantIndex'] = 5

    # rent Index
    country.loc[np.logical_and(country['rentIndex'] > rentMax * 0,
                               country['rentIndex'] <= rentMax * 0.2), 'rentIndex'] = 1
    country.loc[np.logical_and(country['rentIndex'] > rentMax * 0.2,
                               country['rentIndex'] <= rentMax * 0.4), 'rentIndex'] = 2
    country.loc[np.logical_and(country['rentIndex'] > rentMax * 0.4,
                               country['rentIndex'] <= rentMax * 0.6), 'rentIndex'] = 3
    country.loc[np.logical_and(country['rentIndex'] > rentMax * 0.6,
                               country['rentIndex'] <= rentMax * 0.8), 'rentIndex'] = 4
    country.loc[np.logical_and(country['rentIndex'] > rentMax * 0.8,
                               country['rentIndex'] <= rentMax), 'rentIndex'] = 5

    # safety Index
    country.loc[np.logical_and(country['safetyIndex'] > safMax * 0,
                               country['safetyIndex'] <= safMax * 0.2), 'safetyIndex'] = 1
    country.loc[np.logical_and(country['safetyIndex'] > safMax * 0.2,
                               country['safetyIndex'] <= safMax * 0.4), 'safetyIndex'] = 2
    country.loc[np.logical_and(country['safetyIndex'] > safMax * 0.4,
                               country['safetyIndex'] <= safMax * 0.6), 'safetyIndex'] = 3
    country.loc[np.logical_and(country['safetyIndex'] > safMax * 0.6,
                               country['safetyIndex'] <= safMax * 0.8), 'safetyIndex'] = 4
    country.loc[np.logical_and(country['safetyIndex'] > safMax * 0.8,
                               country['safetyIndex'] <= safMax), 'safetyIndex'] = 5

    # Crime index
    country.loc[np.logical_and(country['crimeIndex'] > crMax * 0,
                               country['crimeIndex'] <= crMax * 0.2), 'crimeIndex'] = 1
    country.loc[np.logical_and(country['crimeIndex'] > crMax * 0.2,
                               country['crimeIndex'] <= crMax * 0.4), 'crimeIndex'] = 2
    country.loc[np.logical_and(country['crimeIndex'] > crMax * 0.4,
                               country['crimeIndex'] <= crMax * 0.6), 'crimeIndex'] = 3
    country.loc[np.logical_and(country['crimeIndex'] > crMax * 0.6,
                               country['crimeIndex'] <= crMax * 0.8), 'crimeIndex'] = 4
    country.loc[np.logical_and(country['crimeIndex'] > crMax * 0.8,
                               country['crimeIndex'] <= crMax), 'crimeIndex'] = 5

    country.to_csv("../../data_final/countryData_level.csv", index=False)


if __name__ == '__main__':
    main()