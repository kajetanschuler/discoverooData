import csv
import requests
import json
import time

#Multiple times needed Variables
radius=0

def main():
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open('../data_processed/allCitiesMinPopulation.csv', mode='r') as input:
        reader = csv.reader(input)

        # Open/Create csv file for geological formations
        with open('../data_raw/beachesInCities.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius',
                          'mCountLevel0', 'mCountLevel1', 'mCountLevel2', 'mCountLevel3', 'mCountLevel7',
                          'RCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7' ]
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
                url = url_builder(lat, lon, population)
                response_g= requests.request("GET", url)

                data_g = json.loads(response_g.text)

                # initialize variables and set initial value
                rate = 0
# mountain peaks
                g_count_level0 = 0
                g_count_level1 = 0
                g_count_level2 = 0
                g_count_level3 = 0
                g_count_level7 = 0

                wiki_id_list = []
                xid_list = []
                osm_list = []

                # extract all mountain peaks and count them
                for g in data_g['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_g = g['properties']
                    if 'rate' in characteristics_g:
                        rate = characteristics_g['rate']

                    if 'wikidata' in characteristics_g:
                        wiki_id = characteristics_g['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_g:
                        xid = characteristics_g['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_g:
                        osm = characteristics_g['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
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
# rock formations
                # reset and create new variables for gathering rock formations
                w_count_level0 = 0
                w_count_level1 = 0
                w_count_level2 = 0
                w_count_level3 = 0
                w_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population)
                response_w = requests.request("GET", url)

                data_w = json.loads(response_w.text)

                # extract all rock formations and count them
                for y in data_w['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_w = y['properties']

                    if 'rate' in characteristics_w:
                        rate = characteristics_w['rate']

                    if 'wikidata' in characteristics_w:
                        wiki_id = characteristics_w['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_w:
                        xid = characteristics_w['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_w:
                        osm = characteristics_w['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
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

                                 })

                print("Row with City ID - " + str(city_id) + " - inserted succesfully!")
                time.sleep(20)

# Function to build the request url
def url_builder(lat, lon, population):
    global radius
    kinds=''
    api_key = "&apikey=5ae2e3f221c38a28845f05b67ea0bd21f4cb2e16986f218aefa2a6ae"
    base_url = "https://api.opentripmap.com/0.1/en/places/"
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