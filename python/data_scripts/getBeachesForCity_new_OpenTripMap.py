# Script that retrieves beaches for all cities in "allCities_clean.csv"
# Created - 16.02.2020 - by Kajetan

import csv
import requests
import json
import time

#initialize multiple times used variables and set inital value
radius=0

def main():
    row_number = 1
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open('../data_raw/allCitiesOver100k.csv', mode='r') as input:
        reader = csv.reader(input)

        # Open/Create csv file for beach data
        with open('../data_raw/beachesInCities_new.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius',
                          'gCountLevel0', 'gCountLevel1', 'gCountLevel2', 'gCountLevel3', 'gCountLevel7',
                          'wCountLevel0', 'wCountLevel1', 'wCountLevel2', 'wCountLevel3', 'wCountLevel7',
                          'bCountLevel0', 'bCountLevel1', 'bCountLevel2', 'bCountLevel3', 'bCountLevel7',
                          'sCountLevel0', 'sCountLevel1', 'sCountLevel2', 'sCountLevel3', 'sCountLevel7',
                          'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7',
                          'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7',
                          'uCountLevel0', 'uCountLevel1', 'uCountLevel2', 'uCountLevel3', 'uCountLevel7',
                          'oCountLevel0', 'oCountLevel1', 'oCountLevel2', 'oCountLevel3', 'oCountLevel7']
            writer = csv.DictWriter(output, fieldnames=fieldnames)

            #write out first row as column names
            writer.writeheader()

            # Skip header when reading csv input file
            next(reader, None)

            # Iterate through all rows of the .csv input file and get necessary data
            # Input headers/keys: countryCode,type,cityName,-cityId-,regionName,regionCode,-lat-,-lon-,-population-,elevation,timezone
            for row in reader:
                city_id = row[3]
                lat = row[6]
                lon = row[7]
                population = row[8]

                # Make request for beaches in city and process data
                url = url_builder(lat, lon, population, "beaches")
                response = requests.request("GET", url)

                data = json.loads(response.text)

                # initialize variables and set initial value
                rate = 0
                kind = ""

                # set all beach variables and levels
                g_count_level0 = 0
                g_count_level1 = 0
                g_count_level2 = 0
                g_count_level3 = 0
                g_count_level7 = 0

                w_count_level0 = 0
                w_count_level1 = 0
                w_count_level2 = 0
                w_count_level3 = 0
                w_count_level7 = 0

                b_count_level0 = 0
                b_count_level1 = 0
                b_count_level2 = 0
                b_count_level3 = 0
                b_count_level7 = 0

                s_count_level0 = 0
                s_count_level1 = 0
                s_count_level2 = 0
                s_count_level3 = 0
                s_count_level7 = 0

                r_count_level0 = 0
                r_count_level1 = 0
                r_count_level2 = 0
                r_count_level3 = 0
                r_count_level7 = 0

                n_count_level0 = 0
                n_count_level1 = 0
                n_count_level2 = 0
                n_count_level3 = 0
                n_count_level7 = 0

                u_count_level0 = 0
                u_count_level1 = 0
                u_count_level2 = 0
                u_count_level3 = 0
                u_count_level7 = 0

                o_count_level0 = 0
                o_count_level1 = 0
                o_count_level2 = 0
                o_count_level3 = 0
                o_count_level7 = 0

                wiki_id_list = []
                xid_list = []
                osm_list = []

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                # extract all beaches and count them according to their class
                if 'features' in data:
                    for g in data['features']:
                         # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics = g['properties']
                        if 'rate' in characteristics:
                            rate = characteristics['rate']

                        if 'wikidata' in characteristics:
                            wiki_id = characteristics['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics:
                            xid = characteristics['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics:
                            osm = characteristics['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if 'kinds' in characteristics:
                            kind = characteristics['kinds']

                        if not skip:
                            if "golden_sand_beaches" in kind:
                                if rate >= 4:
                                    g_count_level7 += 1
                                elif rate >= 3:
                                    g_count_level3 += 1
                                elif rate >= 2:
                                    g_count_level2 += 1
                                elif rate >= 1:
                                    g_count_level1 += 1
                                elif rate == 0:
                                    g_count_level0 += 1

                            elif "white_sand_beaches" in kind:
                                if rate >= 4:
                                    w_count_level7 += 1
                                elif rate >= 3:
                                    w_count_level3 += 1
                                elif rate >= 2:
                                    w_count_level2 += 1
                                elif rate >= 1:
                                    w_count_level1 += 1
                                elif rate == 0:
                                    w_count_level0 += 1

                            elif "black_sand_beaches" in kind:
                                if rate >= 4:
                                    b_count_level7 += 1
                                elif rate >= 3:
                                    b_count_level3 += 1
                                elif rate >= 2:
                                    b_count_level2 += 1
                                elif rate >= 1:
                                    b_count_level1 += 1
                                elif rate == 0:
                                    b_count_level0 += 1

                            elif "shingle_beaches" in kind:
                                if rate >= 4:
                                    s_count_level7 += 1
                                elif rate >= 3:
                                    s_count_level3 += 1
                                elif rate >= 2:
                                    s_count_level2 += 1
                                elif rate >= 1:
                                    s_count_level1 += 1
                                elif rate == 0:
                                    s_count_level0 += 1

                            elif "rocks_beaches" in kind:
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

                            elif "nude_beaches" in kind:
                                if rate >= 4:
                                    n_count_level7 += 1
                                elif rate >= 3:
                                    n_count_level3 += 1
                                elif rate >= 2:
                                    n_count_level2 += 1
                                elif rate >= 1:
                                    n_count_level1 += 1
                                elif rate == 0:
                                    n_count_level0 += 1

                            elif "urbans_beaches" in kind:
                                if rate >= 4:
                                    u_count_level7 += 1
                                elif rate >= 3:
                                    u_count_level3 += 1
                                elif rate >= 2:
                                    u_count_level2 += 1
                                elif rate >= 1:
                                    u_count_level1 += 1
                                elif rate == 0:
                                    u_count_level0 += 1

                            elif "other_beaches" in kind:
                                if rate >= 4:
                                    o_count_level7 += 1
                                elif rate >= 3:
                                    o_count_level3 += 1
                                elif rate >= 2:
                                    o_count_level2 += 1
                                elif rate >= 1:
                                    o_count_level1 += 1
                                elif rate == 0:
                                    o_count_level0 += 1

                    # put gathered data into one row in the csv file
                    writer.writerow({'cityId': city_id, 'searchRadius': radius,
                                     'gCountLevel0': g_count_level0, 'gCountLevel1': g_count_level1,'gCountLevel2': g_count_level2,
                                     'gCountLevel3': g_count_level3, 'gCountLevel7': g_count_level7,
                                     'wCountLevel0': w_count_level0, 'wCountLevel1': w_count_level1, 'wCountLevel2': w_count_level2,
                                     'wCountLevel3': w_count_level3, 'wCountLevel7': w_count_level7,
                                     'bCountLevel0': b_count_level0, 'bCountLevel1': b_count_level1, 'bCountLevel2': b_count_level2,
                                     'bCountLevel3': b_count_level3, 'bCountLevel7': b_count_level7,
                                     'sCountLevel0': s_count_level0, 'sCountLevel1': s_count_level1, 'sCountLevel2': s_count_level2,
                                     'sCountLevel3': s_count_level3, 'sCountLevel7': s_count_level7,
                                     'rCountLevel0': r_count_level0, 'rCountLevel1': r_count_level0,'rCountLevel2': r_count_level2,
                                     'rCountLevel3': r_count_level3, 'rCountLevel7': r_count_level7,
                                     'nCountLevel0': n_count_level0, 'nCountLevel1': n_count_level0, 'nCountLevel2': n_count_level2,
                                     'nCountLevel3': n_count_level3, 'nCountLevel7': n_count_level7,
                                     'uCountLevel0': u_count_level0, 'uCountLevel1': u_count_level0, 'uCountLevel2': u_count_level2,
                                     'uCountLevel3': u_count_level3, 'uCountLevel7': u_count_level7,
                                     'oCountLevel0': o_count_level0, 'oCountLevel1': o_count_level1, 'oCountLevel2': o_count_level2,
                                     'oCountLevel3': o_count_level3, 'oCountLevel7': o_count_level7,})

                    print("Row with City ID - " + str(city_id) + " - inserted succesfully! - Row number: " + str(row_number))

                    row_number += 1
                    time.sleep(20)


# Function to build the request url
def url_builder(lat, lon, population, kinds):
    global radius
    api_key = "&apikey=5ae2e3f221c38a28845f05b67ea0bd21f4cb2e16986f218aefa2a6ae"
    base_url = "https://api.opentripmap.com/0.1/en/places/"
    if int(population) > 1000000:
        radius = 15000

    elif int(population) > 500000:
        radius = 10000

    else:
        radius = 5000

    radius_full = "radius?radius=" + str(radius)
    lat = "&lat=" + str(lat)
    lon = "&lon=" + str(lon)
    kinds = "&kinds=" + kinds
    limit = "&limit=" + str(10000)
    url = base_url + radius_full + lon + lat + kinds + limit + api_key
    return url


if __name__ == '__main__':
    main()