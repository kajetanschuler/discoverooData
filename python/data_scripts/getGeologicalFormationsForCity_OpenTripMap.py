import csv
import requests
import json
import time

#Multiple times needed Variables
radius=0

def main():
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open('../data_processed/allCities_clean.csv', mode='r') as input:
        reader = csv.reader(input)

        # Open/Create csv file for geological formations
        with open('../data_raw/geologicalInformationInCities.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius', 'population',
                          'mCountLevel0', 'mCountLevel1', 'mCountLevel2', 'mCountLevel3', 'mCountLevel7',
                          'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7']
            writer = csv.DictWriter(output, fieldnames=fieldnames)

            #write out first row as column names
            writer.writeheader()

            # Skip header when reading csv input file
            next(reader, None)

            # Iterate through all rows of the .csv input file and get necessary data
            # Input headers/keys: countryCode,type,cityName,-cityId-,regionName,regionCode,-lat-,-lon-,-population-,elevation,timezone
            for row in reader:
                city_id = row[3]
                lat = row[7]
                lon = row[8]
                population = row[5]

                # mountain peaks
                # Make request for mountain peaks in city and process data
                url = url_builder(lat, lon, population, "mountain_peaks")

                response_m= requests.request("GET", url)

                data_m = json.loads(response_m.text)

                # initialize variables and set initial value
                rate = 0

                m_count_level0 = 0
                m_count_level1 = 0
                m_count_level2 = 0
                m_count_level3 = 0
                m_count_level7 = 0

                wiki_id_list = []
                xid_list = []
                osm_list = []

                # extract all mountain peaks and count them
                if 'features' in data_m:
                    for m in data_m['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_m = m['properties']
                        if 'rate' in characteristics_m:
                            rate = characteristics_m['rate']

                        if 'wikidata' in characteristics_m:
                            wiki_id = characteristics_m['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_m:
                            xid = characteristics_m['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_m:
                            osm = characteristics_m['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
                            if rate >= 4:
                                m_count_level7 += 1
                            elif rate >= 3:
                                m_count_level3 += 1
                            elif rate >= 2:
                                m_count_level2 += 1
                            elif rate >= 1:
                                m_count_level1 += 1
                            elif rate == 0:
                                m_count_level0 += 1
# rock formations
                # reset and create new variables for gathering rock formations
                r_count_level0 = 0
                r_count_level1 = 0
                r_count_level2 = 0
                r_count_level3 = 0
                r_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "rock_formations")
                response_r = requests.request("GET", url)

                data_r = json.loads(response_r.text)

                # extract all rock formations and count them
                if 'features' in data_r:
                    for r in data_r['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_r = r['properties']

                        if 'rate' in characteristics_r:
                            rate = characteristics_r ['rate']

                        if 'wikidata' in characteristics_r:
                            wiki_id = characteristics_r['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_r:
                            xid = characteristics_r['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_r:
                            osm = characteristics_r['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
                            if rate >= 4:
                                r_count_level7 += 1
                            elif rate >= 3:
                                r_count_level3 += 1
                            elif rate >= 2:
                                r_count_level2 += 1
                            elif rate >= 1:
                                r_count_level1 += 1
                            elif rate == 0:
                                r_count_level0 += 1


                # put gathered data into one row in the csv file
                writer.writerow({'cityId': city_id, 'searchRadius': radius, 'population': population,
                                 'mCountLevel0': m_count_level0, 'mCountLevel1': m_count_level1,'mCountLevel2': m_count_level2,
                                 'mCountLevel3': m_count_level3, 'mCountLevel7': m_count_level7,
                                 'rCountLevel0': r_count_level0, 'rCountLevel1': r_count_level0,'rCountLevel2': r_count_level2,
                                 'rCountLevel3': r_count_level3, 'rCountLevel7': r_count_level7
                                 })

                print("Row with City ID - " + str(city_id) + " - inserted succesfully!")
                time.sleep(20)

# Function to build the request url
def url_builder(lat, lon, population, kinds):
    global radius
    api_key = "&apikey=e1f6061817mshb6a5d107db1f20fp1b58cejsn545de208fcf6"
    base_url = "https://opentripmap-places-v1.p.rapidapi.com/en/places/"

    if int(population) > 1000000:
        radius = 50000

    elif int(population) > 500000:
        radius = 30000

    else:
        radius = 20000

    radius_full = "radius?radius=" + str(radius)
    lat = "&lat=" + str(lat)
    lon = "&lon=" + str(lon)
    kinds = "&kinds=" +  kinds
    limit = "&limit=" + str(10000)

    url = base_url + radius_full + lon + lat + kinds + limit + api_key
    return url


if __name__ == '__main__':
    main()