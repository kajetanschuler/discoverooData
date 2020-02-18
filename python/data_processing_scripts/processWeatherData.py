# Script was Wetterdaten auswertet und prozessiert
# Created - 17.02.2020 - by Kajetan
import pandas as pd


def main():
    weather_stations = pd.read_csv("../data_raw/weatherDataPerStation/weatherStationsByCity.csv")

    # Iterate through all rows and get corresponding Station Data
    for index, row in weather_stations.iterrows():
        station_id = row['stationId']
        station_file = "../data_raw/weatherDataPerStation/" + station_id + " .csv"
        station_data = pd.read_csv(station_file)
        prcp = station_data[['date', 'prcp']]
        tmax = station_data[['date', 'tmax']]
        tmin = station_data[['date', 'tmin']]

        # Drop unnecessary NaN rows
        prcp = prcp.dropna()
        tmax = tmax.dropna()
        tmin = tmin.dropna()

        # Get data for January
        tmax_jan = tmax[tmax['date'].str.contains('2017-01|2018-01|2019-01')]
        tmax_jan_len = len(tmax_jan.index)
        tmax_jan_value = tmax_jan['tmax'].sum() / tmax_jan_len

        tmax_feb = tmax[tmax['date'].str.contains('2017-02|2018-02|2019-02')]
        tmax_feb_len = len(tmax_feb)
        tmax_feb_value = tmax_feb['tmax'].sum() / tmax_feb_len
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        oct = 0
        nov = 0
        dec = 0




def process_data():
    print()


if __name__ == '__main__':
    main()