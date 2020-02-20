# Script that processes all of the Raw data
# Created - 18.02.2020 - by Kajetan

from python.data_processing_scripts import changeCountryCodeOfInfrastructureData, mergeCostAndQuality, \
    mergeCityCountryData, calculateBeachIndex, calculateCulturalIndex, calculateGeologicalFormationIndex, \
    processWeatherData


def main():
    changeCountryCodeOfInfrastructureData.main()
    mergeCostAndQuality.main()
    mergeCityCountryData.main()
    calculateGeologicalFormationIndex.main()
    calculateCulturalIndex.main()
    calculateBeachIndex.main()
    processWeatherData.main()


if __name__ == '__main__':
    main()


# Todo: Anpassen für neue Skripte!