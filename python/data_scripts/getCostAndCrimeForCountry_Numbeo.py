import requests
import json
import csv
import pprint

def main():

    params = {
        "api_key": "'pijz4mm61rin8u",
        "format": "csv"
    }
    # APi Call
    response_cost = requests.get('https://www.numbeo.com/api/rankings_by_country_historical?api_key=pijz4mm61rin8u&section=1')
    #Store API result in data
    data_cost = json.loads(response_cost.text)
    data_cost2019 = data_cost['2019']

    response_crime_safety = requests.get('https://www.numbeo.com/api/rankings_by_country_historical?api_key=pijz4mm61rin8u&section=7')
    data_crime_safety = json.loads(response_crime_safety.text)
    data_crime_safety2019 = data_crime_safety['2019']

#fieldnames = Spaltenname

    with open ('../data_raw/costAndSafetyDataForCountry.csv', 'wt', newline='') as output:
        fieldnames = ['countryCode', 'cpiRentIndex', 'cpiIndex', 'groceriesIndex', 'purchasingPowerIndex',
                      'restaurantIndex', 'rentIndex', 'safetyIndex', 'crimeIndex']
        writer = csv.DictWriter(output, fieldnames = fieldnames)
        writer.writeheader()

        for country_data in data_cost2019:
            cpi_rent = country_data['cpi_and_rent_index']
            cpi = country_data['cpi_index']
            groceries = country_data['groceries_index']
            iso_code = country_data['iso3166_country_code']
            purchasing_power = country_data['purchasing_power_incl_rent_index']
            restaurant_index = country_data['restaurant_price_index']
            rent_index = country_data['rent_index']

            for safety_data in data_crime_safety2019:
                iso_code2 = safety_data['iso3166_country_code']
                if iso_code == iso_code2:
                    safety_index = safety_data['safety_index']
                    crime_index = safety_data['crime_index']
                    writer.writerow({'countryCode': iso_code, 'cpiRentIndex': cpi_rent, 'cpiIndex': cpi,
                                     'groceriesIndex': groceries, 'purchasingPowerIndex': purchasing_power,
                                     'restaurantIndex': restaurant_index, 'rentIndex': rent_index,
                                     'safetyIndex': safety_index, 'crimeIndex': crime_index})
                    print("country with " + iso_code + " sucessfully inserted")


if __name__ == '__main__':
    main()