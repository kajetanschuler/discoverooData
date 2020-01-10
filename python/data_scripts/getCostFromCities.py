import requests
import json
import csv


def main():

    params = {
        "api_key": "'pijz4mm61rin8u",
        "format": "csv"
    }
    # APi Call
    response_cost = requests.get('https://www.numbeo.com/api/rankings_by_city_historical?api_key=pijz4mm61rin8u&section=1')
    #Store API result in data
    data_cost = json.loads(response_cost.text)
    data_cost2018 = data_cost['2018']

    response_crime_safety = requests.get('https://www.numbeo.com/api/rankings_by_city_historical?api_key=pijz4mm61rin8u&section=7')
    data_crime_safety = json.loads(response_crime_safety.text)
    data_crime_safety2018 = data_crime_safety['2018']

#fieldnames = Spaltenname

    with open ('../data_raw/costAndSafetyDataForCity.csv', 'wt', newline='') as output:
        fieldnames = ['countryName', 'cityID', 'cityName', 'cpiRentIndex', 'cpiIndex', 'groceriesIndex',
                      'purchasingPowerIndex',
                      'restaurantIndex', 'rentIndex', 'safetyIndex', 'crimeIndex']
        writer = csv.DictWriter(output, fieldnames = fieldnames)
        writer.writeheader()

        for city_data in data_cost2018:
            country_name = city_data['country']
            city_name = city_data['city_name']
            city_id = city_data['city_id']
            cpi_rent = city_data['cpi_and_rent_index']
            cpi = city_data['cpi_index']
            groceries = city_data['groceries_index']
            purchasing_power = city_data['purchasing_power_incl_rent_index']
            restaurant_index = city_data['restaurant_price_index']
            rent_index = city_data['rent_index']

            for safety_data in data_crime_safety2018:
                city_id2 = safety_data['city_id']
                if city_id == city_id2:
                    safety_index = safety_data['safety_index']
                    crime_index = safety_data['crime_index']
                    writer.writerow({'countryName': country_name, 'cityName': city_name, 'cityID': city_id,
                                     'cpiRentIndex': cpi_rent, 'cpiIndex': cpi,
                                     'groceriesIndex': groceries, 'purchasingPowerIndex': purchasing_power,
                                     'restaurantIndex': restaurant_index, 'rentIndex': rent_index,
                                     'safetyIndex': safety_index, 'crimeIndex': crime_index})
                    print("city with " + city_name + " successfully inserted")


if __name__ == '__main__':
    main()