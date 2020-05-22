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
    calculateCulturalIndex.main()
    calculateGeologicalFormationIndex.main()
    calculateBeachIndex.main()
    addCityImagePath.main()
    calculateUniqueRegionCode.main() # 1
    cleanCityData.main() # 2
    # Output WeatherStationsByCity für Stadt, weatherDataPerStation für weatherData_final
    processWeatherData.main()

    # Schritt 2
    createCountryData.main()

    # Schritt 3 (Zuerst country-Daten mergen, da diese in createCityData verwendet werden)
    createCityData.main()

    # Schritt 4 (Zuerst city-Daten erstellen, da diese in createCityData verwendet werden)
    createRegionData.main()

    # Schritt 4 Level Creation
    levelCreationCityData.main()
    levelCreationCountryData.main()
    levelCreationRegionData.main()



if __name__ == '__main__':
    main()
