# Script that processes all of the Raw data
# Created - 18.02.2020 - by Kajetan
# Updated 19.05.2020 by Malik
# Updated 22.05.2020 by Svenja

from python.data_processing_scripts import processWeatherData, createRegionData, cleanCityData, \
    changeCountryCodeOfInfrastructureData, calculateUniqueRegionCode, addCityImagePath
from python.data_processing_scripts.IndicesCreation import calculateCulturalIndex, calculateBeachIndex, \
    calculateGeologicalFormationIndex
from python.data_processing_scripts.LevelCreation import levelCreationCityData, levelCreationCountryData, levelCreationRegionData
from python.data_merge_scripts import createCityData, createCountryData


def main():

    # Schritt 1
    changeCountryCodeOfInfrastructureData.main()
    print("1/14")

    calculateCulturalIndex.main()
    print("2/14")

    calculateGeologicalFormationIndex.main()
    print("3/14")

    calculateBeachIndex.main()
    print("4/14")

    addCityImagePath.main()
    print("5/14")

    calculateUniqueRegionCode.main() # 1
    print("6/14")

    cleanCityData.main() # 2
    print("7/14")

    # Output WeatherStationsByCity für Stadt, weatherDataPerStation für weatherData_final
    processWeatherData.main()
    print("8/14")

    # Schritt 2
    createCountryData.main()
    print("9/14")

    # Schritt 3 (Zuerst country-Daten mergen, da diese in createCityData verwendet werden)
    createCityData.main()
    print("10/14")

    # Schritt 4 (Zuerst city-Daten erstellen, da diese in createCityData verwendet werden)
    createRegionData.main()
    print("11/14")

    # Schritt 4 Level Creation
    levelCreationCityData.main()
    print("12/14")

    levelCreationCountryData.main()
    print("13/14")

    levelCreationRegionData.main()
    print("14/14")

if __name__ == '__main__':
    main()

#Optimieren durch: Alle csv's ab data processed löschen