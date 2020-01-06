import csv
import requests
import json
import time

#initialize multiple times used variables and set inital value
radius=0

def main():
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open('../data_processed/allCitiesMinPopulation.csv', mode='r') as input:
        reader = csv.reader(input)

        # Open/Create csv file for beach data
        with open('../data_raw/beachesInCities.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius',
                          'gCountLevel0', 'gCountLevel1', 'gCountLevel2', 'gCountLevel3', 'gCountLevel7',
                          'wCountLevel0', 'wCountLevel1', 'wCountLevel2', 'wCountLevel3', 'wCountLevel7',
                          'bCountLevel0', 'bCountLevel1', 'bCountLevel2', 'bCountLevel3', 'bCountLevel7',
                          'sCountLevel0', 'sCountLevel1', 'sCountLevel2', 'sCountLevel3', 'sCountLevel7',
                          'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7',
                          'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7',
                          'uCountLevel0', 'uCountLevel1', 'uCountLevel2', 'uCountLevel3', 'uCountLevel7' ]
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

 # golden beaches
                # Make request for beaches in city and process data
                url = url_builder(lat, lon, population, "golden_sand_beaches")
                response_g = requests.request("GET", url)

                data_g = json.loads(response_g.text)

                # initialize variables and set initial value
                rate = 0

                g_count_level0 = 0
                g_count_level1 = 0
                g_count_level2 = 0
                g_count_level3 = 0
                g_count_level7 = 0

                wiki_id_list = []
                xid_list = []
                osm_list = []

                # extract all golden beaches and count them
                if 'features' in data_g:
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
# white beaches
                # reset and create new variables for gathering white beaches
                w_count_level0 = 0
                w_count_level1 = 0
                w_count_level2 = 0
                w_count_level3 = 0
                w_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population,"white_sand_beaches")
                response_w = requests.request("GET", url)

                data_w = json.loads(response_w.text)

                # extract all beaches and count them

                if 'features' in data_w:
                    for w in data_w['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_w = w['properties']

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

#black beaches
                # reset and create new variables for gathering black beaches
                b_count_level0 = 0
                b_count_level1 = 0
                b_count_level2 = 0
                b_count_level3 = 0
                b_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "black_sand_beaches")
                response_b = requests.request("GET", url)

                data_b = json.loads(response_b.text)

                # extract all beaches and count them
                if 'features' in data_b:
                    for b in data_b['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_b = b['properties']

                        if 'rate' in characteristics_b:
                            rate = characteristics_b['rate']

                        if 'wikidata' in characteristics_b:
                            wiki_id = characteristics_b['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_b:
                            xid = characteristics_b['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_b:
                            osm = characteristics_b['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
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

#shingle beaches
                # reset and create new variables for gathering shingle beaches
                s_count_level0 = 0
                s_count_level1 = 0
                s_count_level2 = 0
                s_count_level3 = 0
                s_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "shingle_beaches" )
                response_s = requests.request("GET", url)

                data_s = json.loads(response_s.text)

                # extract all beaches and count them

                if 'features' in data_s:
                  for s in data_s['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_s = s['properties']

                        if 'rate' in characteristics_s:
                            rate = characteristics_s['rate']

                        if 'wikidata' in characteristics_s:
                            wiki_id = characteristics_s['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_s:
                            xid = characteristics_s['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_s:
                            osm = characteristics_s['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
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

# rocks beaches
                # reset and create new variables for gathering rocks beaches
                r_count_level0 = 0
                r_count_level1 = 0
                r_count_level2 = 0
                r_count_level3 = 0
                r_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "rocks_beaches")
                response_r = requests.request("GET", url)

                data_r = json.loads(response_r.text)

                # extract all beaches and count them
                if 'features' in data_r:
                    for r in data_r['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_r = r['properties']

                        if 'rate' in characteristics_r:
                            rate = characteristics_r['rate']

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
#nude beaches
                # reset and create new variables for gathering nude beaches
                n_count_level0 = 0
                n_count_level1 = 0
                n_count_level2 = 0
                n_count_level3 = 0
                n_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "nude_beaches")
                response_n = requests.request("GET", url)

                data_n = json.loads(response_n.text)

                # extract all beaches and count them
                if 'features' in data_n:
                    for n in data_n['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_n = n['properties']

                        if 'rate' in characteristics_n:
                            rate = characteristics_n['rate']

                        if 'wikidata' in characteristics_n:
                            wiki_id = characteristics_n['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_n:
                            xid = characteristics_n['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_n:
                            osm = characteristics_n['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
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
#urban beaches
                # reset and create new variables for gathering urban beaches

                u_count_level0 = 0
                u_count_level1 = 0
                u_count_level2 = 0
                u_count_level3 = 0
                u_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "urbans_beaches")
                response_u = requests.request("GET", url)

                data_u = json.loads(response_u.text)

                # extract all sights and count them
                if 'features' in data_u:
                    for u in data_u['features']:
                        # use as variable to skip a entry if it already exists
                        skip = False
                        characteristics_u = u['properties']

                        if 'rate' in characteristics_u:
                            rate = characteristics_u['rate']

                        if 'wikidata' in characteristics_n:
                            wiki_id = characteristics_u['wikidata']
                            if wiki_id in wiki_id_list:
                                skip = True
                            else:
                                wiki_id_list.append(wiki_id)

                        if 'xid' in characteristics_u:
                            xid = characteristics_n['xid']
                            if xid in xid_list:
                                skip = True
                            else:
                                xid_list.append(xid)

                        if 'osm' in characteristics_u:
                            osm = characteristics_u['osm']
                            if osm in osm_list:
                                skip = True
                            else:
                                osm_list.append(osm)

                        if not skip:
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
def url_builder(lat, lon, population, kinds):
    global radius
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
    kinds = "&kinds=" + kinds
    limit = "&limit=" + str(10000)
    url = base_url + radius_full + lon + lat + kinds + limit + api_key
    return url


if __name__ == '__main__':
    main()