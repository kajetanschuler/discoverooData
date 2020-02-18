# Script was Wetterdaten auswertet und prozessiert
# Created - 17.02.2020 - by Kajetan
import pandas as pd


def main():
    # Read Station / City data
    weather_stations = pd.read_csv("../data_raw/weatherDataPerStation/weatherStationsByCity.csv")

    # Drop duplicate rows as they are not needed
    weather_stations2 = weather_stations.drop_duplicates(subset='stationId')

    # Iterate through all rows and get corresponding Station Data
    for index, row in weather_stations.iterrows():
        station_id = row['stationId']
        station_file = "../data_raw/weatherDataPerStation/" + station_id + " .csv"
        station_data = pd.read_csv(station_file)

        # Get Tmax, Tmin and Prcp Data from station
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

        tmin_jan = tmin[tmin['date'].str.contains('2017-01|2018-01|2019-01')]
        tmin_jan_len = len(tmin_jan.index)
        tmin_jan_value = tmin_jan['tmin'].sum() / tmin_jan_len

        # Get data for February
        tmax_feb = tmax[tmax['date'].str.contains('2017-02|2018-02|2019-02')]
        tmax_feb_len = len(tmax_feb)
        tmax_feb_value = tmax_feb['tmax'].sum() / tmax_feb_len

        tmin_feb = tmin[tmin['date'].str.contains('2017-02|2018-02|2019-02')]
        tmin_feb_len = len(tmin_feb)
        tmin_feb_value = tmin_feb['tmin'].sum() / tmin_feb_len

        # Get data for March
        tmax_mar = tmax[tmax['date'].str.contains('2017-03|2018-03|2019-03')]
        tmax_mar_len = len(tmax_mar.index)
        tmax_mar_value = tmax_mar['tmax'].sum() / tmax_mar_len

        tmin_mar = tmin[tmin['date'].str.contains('2017-03|2018-03|2019-03')]
        tmin_mar_len = len(tmin_mar.index)
        tmin_mar_value = tmin_mar['tmin'].sum() / tmin_mar_len

        # Get data for April




def process_data():
    print()


if __name__ == '__main__':
    main()