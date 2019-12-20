import csv

def main():
    with open('../data_raw/allCities.csv', 'rt') as inp, open('../data_processed/allCitiesMinPopulation.csv', 'wt') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        next(reader, None)
        for row in reader:
            population = int(row[8])
            if population >= 200000:
                writer.writerow(row)
                print("Written")

if __name__ == '__main__':
    main()