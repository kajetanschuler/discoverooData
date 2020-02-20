# Skript löscht Städte die weniger als 100.000 hat
# Created - 04.01.2020 - by Kajetan

import csv


def main():
    with open('../archive/allCities.csv', 'rt') as inp, open('../data_processed/allCitiesMinPopulation.csv', 'wt') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp)
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            population = int(row[8])
            if population >= 200000:
                writer.writerow(row)
                print("Written")


if __name__ == '__main__':
    main()