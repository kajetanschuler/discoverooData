import csv
import requests
import json


def main():
    # Open .csv file that contains all cities with a minimum population of 200.000
    with open ('../data_processed/allCitiesMinPopulation.csv', 'rt') as input:
        reader = csv.reader(input)

        # Open/Create csv file for historic sights data
        with open ('../data_raw/historicalSightsInCities.csv', 'wt') as output:
            fieldnames = ['cityId', 'searchRadius',
                          'hCountLevel0', 'hCountLevel1', 'hCountLevel2', 'hCountLevel3', 'hCountLevel7',
                          'cCountLevel0', 'cCountLevel1', ]
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

                url = url_builder(lat, lon, population, "historic")
                response = requests.request("GET", url)

                data = json.loads(response.text)

                skip = False

                rate = ""
                wiki_id = ""
                xid = ""
                osm = ""
                h_count_level0 = 0
                h_count_level1 = 0
                h_count_level2 = 0
                h_count_level3 = 0
                h_count_level7 = 0


                wiki_id_list = []
                xid_list = []
                osm_list = []

                for x in data['features']:
                    characteristics = x['properties']
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

                    if not skip:
                        if rate >= 7:
                            h_count_level7 += 1
                        elif rate >= 3:
                            h_count_level3 += 1
                        elif rate >= 2:
                            h_count_level2 += 1
                        elif rate >= 1:
                            h_count_level1 += 1
                        elif rate == 0:
                            h_count_level0 += 1

# Todo: Reset list variables to empty
# Todo: Run next request with same city but different "kind"
# Todo: Write Full row into csv
# Todo: Run next row with new City Id


# Funtion to build the request url
def url_builder(lat, lon, population, kinds):
    api_key = "&apikey=5ae2e3f221c38a28845f05b6cb6b4ac567a0e6b3fcde2740c98bc367"
    base_url = "https://api.opentripmap.com/0.1/en/places/"
    if int(population) > 1000000:
        radius = 50000

    elif int(population) > 500000:
        radius = 30000

    else:
        radius = 20000

    radius = "radius?radius=" + str(radius)
    lat = "&lat=" + str(lat)
    lon = "&lon=" + str(lon)
    kinds = "&kinds=" +  kinds
    limit = "&limit=" + str(10000)

    url = base_url + radius + lon + lat + kinds + limit + api_key
    return url


if __name__ == '__main__':
    main()
