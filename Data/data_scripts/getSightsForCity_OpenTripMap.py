import csv
import requests
import json
import time

radius = 0


def main():
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open ('../data_processed/allCitiesMinPopulation.csv', 'rt') as input:
        reader = csv.reader(input)

        # Open/Create csv file for historic sights data
        with open ('../data_raw/sightsInCities.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius',
                          'hCountLevel0', 'hCountLevel1', 'hCountLevel2', 'hCountLevel3', 'hCountLevel7',
                          'cCountLevel0', 'cCountLevel1', 'cCountLevel2', 'cCountLevel3', 'cCountLevel7',
                          'rCountLevel0', 'rCountLevel1', 'rCountLevel2', 'rCountLevel3', 'rCountLevel7',
                          'aCountLevel0', 'aCountLevel1', 'aCountLevel2', 'aCountLevel3', 'aCountLevel7',
                          'iCountLevel0', 'iCountLevel1', 'iCountLevel2', 'iCountLevel3', 'iCountLevel7',
                          'nCountLevel0', 'nCountLevel1', 'nCountLevel2', 'nCountLevel3', 'nCountLevel7']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()

            # Skip header when reading csv input file
            next(reader, None)

            # Iterate through all rows of the .csv input file and get necessary data
            for row in reader:
                city_id = row[3]
                population = row[8]
                lat = row[6]
                lon = row[7]

                # Make request for historic sights in city and process data
                url = url_builder(lat, lon, population, "historic")
                response_h = requests.request("GET", url)

                data_h = json.loads(response_h.text)

                # initialize variables and set initial value
                rate = 0

                h_count_level0 = 0
                h_count_level1 = 0
                h_count_level2 = 0
                h_count_level3 = 0
                h_count_level7 = 0

                wiki_id_list = []
                xid_list = []
                osm_list = []

                # extract all sights and count them
                for x in data_h['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_h = x['properties']
                    if 'rate' in characteristics_h:
                        rate = characteristics_h['rate']

                    if 'wikidata' in characteristics_h:
                        wiki_id = characteristics_h['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_h:
                        xid = characteristics_h['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_h:
                        osm = characteristics_h['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
                        if rate >= 4:
                            h_count_level7 += 1
                        elif rate >= 3:
                            h_count_level3 += 1
                        elif rate >= 2:
                            h_count_level2 += 1
                        elif rate >= 1:
                            h_count_level1 += 1
                        elif rate == 0:
                            h_count_level0 += 1

                # reset and create new variables for gathering cultural sights
                c_count_level0 = 0
                c_count_level1 = 0
                c_count_level2 = 0
                c_count_level3 = 0
                c_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "cultural")
                response_c = requests.request("GET", url)

                data_c = json.loads(response_c.text)

                # extract all sights and count them
                for y in data_c['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_c = y['properties']

                    if 'rate' in characteristics_c:
                        rate = characteristics_c['rate']

                    if 'wikidata' in characteristics_c:
                        wiki_id = characteristics_c['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_c:
                        xid = characteristics_c['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_c:
                        osm = characteristics_c['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
                        if rate >= 4:
                            c_count_level7 += 1
                        elif rate >= 3:
                            c_count_level3 += 1
                        elif rate >= 2:
                            c_count_level2 += 1
                        elif rate >= 1:
                            c_count_level1 += 1
                        elif rate == 0:
                            c_count_level0 += 1

                # reset and create new variables for gathering religious sights
                r_count_level0 = 0
                r_count_level1 = 0
                r_count_level2 = 0
                r_count_level3 = 0
                r_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "religion")
                response_r = requests.request("GET", url)

                data_r = json.loads(response_r.text)

                # extract all sights and count them
                for z in data_r['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_r = z['properties']

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

                # reset and create new variables for gathering architectural sights
                a_count_level0 = 0
                a_count_level1 = 0
                a_count_level2 = 0
                a_count_level3 = 0
                a_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "architecture")
                response_a = requests.request("GET", url)

                data_a = json.loads(response_a.text)

                # extract all sights and count them
                for a in data_a['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_a = a['properties']

                    if 'rate' in characteristics_a:
                        rate = characteristics_a['rate']

                    if 'wikidata' in characteristics_a:
                        wiki_id = characteristics_a['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_a:
                        xid = characteristics_a['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_a:
                        osm = characteristics_a['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
                        if rate >= 4:
                            a_count_level7 += 1
                        elif rate >= 3:
                            a_count_level3 += 1
                        elif rate >= 2:
                            a_count_level2 += 1
                        elif rate >= 1:
                            a_count_level1 += 1
                        elif rate == 0:
                            a_count_level0 += 1

                # reset and create new variables for gathering industrial sights
                i_count_level0 = 0
                i_count_level1 = 0
                i_count_level2 = 0
                i_count_level3 = 0
                i_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "industrial_facilities")
                response_i = requests.request("GET", url)

                data_i = json.loads(response_i.text)

                # extract all sights and count them
                for i in data_i['features']:
                    # use as variable to skip a entry if it already exists
                    skip = False
                    characteristics_i = i['properties']

                    if 'rate' in characteristics_i:
                        rate = characteristics_i['rate']

                    if 'wikidata' in characteristics_i:
                        wiki_id = characteristics_i['wikidata']
                        if wiki_id in wiki_id_list:
                            skip = True
                        else:
                            wiki_id_list.append(wiki_id)

                    if 'xid' in characteristics_i:
                        xid = characteristics_i['xid']
                        if xid in xid_list:
                            skip = True
                        else:
                            xid_list.append(xid)

                    if 'osm' in characteristics_i:
                        osm = characteristics_i['osm']
                        if osm in osm_list:
                            skip = True
                        else:
                            osm_list.append(osm)

                    if not skip:
                        if rate >= 4:
                            i_count_level7 += 1
                        elif rate >= 3:
                            i_count_level3 += 1
                        elif rate >= 2:
                            i_count_level2 += 1
                        elif rate >= 1:
                            i_count_level1 += 1
                        elif rate == 0:
                            i_count_level0 += 1

                # reset and create new variables for gathering natural sights
                n_count_level0 = 0
                n_count_level1 = 0
                n_count_level2 = 0
                n_count_level3 = 0
                n_count_level7 = 0

                wiki_id_list.clear()
                xid_list.clear()
                osm_list.clear()

                rate = 0

                url = url_builder(lat, lon, population, "natural")
                response_n = requests.request("GET", url)

                data_n = json.loads(response_n.text)

                # extract all sights and count them
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

                # put gathered data into one row in the csv file
                writer.writerow({'cityId': city_id, 'searchRadius': radius,
                                 'hCountLevel0': h_count_level0, 'hCountLevel1': h_count_level1, 'hCountLevel2': h_count_level2, 'hCountLevel3': h_count_level3, 'hCountLevel7': h_count_level7,
                                 'cCountLevel0': c_count_level0, 'cCountLevel1': c_count_level1, 'cCountLevel2': c_count_level2, 'cCountLevel3': c_count_level3, 'cCountLevel7': c_count_level7,
                                 'rCountLevel0': r_count_level0, 'rCountLevel1': r_count_level1, 'rCountLevel2': r_count_level2, 'rCountLevel3': r_count_level3, 'rCountLevel7': r_count_level7,
                                 'aCountLevel0': a_count_level0, 'aCountLevel1': a_count_level1, 'aCountLevel2': a_count_level2, 'aCountLevel3': a_count_level3, 'aCountLevel7': a_count_level7,
                                 'iCountLevel0': i_count_level0, 'iCountLevel1': i_count_level1, 'iCountLevel2': i_count_level2, 'iCountLevel3': i_count_level3, 'iCountLevel7': i_count_level7,
                                 'nCountLevel0': n_count_level0, 'nCountLevel1': n_count_level0, 'nCountLevel2': n_count_level2, 'nCountLevel3': n_count_level3, 'nCountLevel7': n_count_level7,
                                 })

                print("Row with City ID - " + str(city_id) + " - inserted succesfully!")
                time.sleep(20)


# Funtion to build the request url
def url_builder(lat, lon, population, kinds):
    global radius
    api_key = "&apikey=5ae2e3f221c38a28845f05b6cb6b4ac567a0e6b3fcde2740c98bc367"
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