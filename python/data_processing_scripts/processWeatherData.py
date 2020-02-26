# Script was Wetterdaten auswertet und prozessiert
# Created - 17.02.2020 - by Kajetan
import pandas as pd


def main():
    # Read Station / City data
    weather_stations = pd.read_csv("../data_raw/weatherStationsByCity_50km.csv")

    # Drop duplicate rows as they are not needed
    weather_stations = weather_stations.drop_duplicates(subset='stationId')

    # Intialise list to store values
    data_list = []

    # Iterate through all rows and get corresponding Station Data
    for index, row in weather_stations.iterrows():
        station_id = row['stationId']
        station_file = "../data_raw/weatherDataPerStation/" + station_id + " .csv"
        station_data = pd.read_csv(station_file)

        # Check if tmax and tmin exist
        if 'tmax' in station_data and 'tmin' in station_data:

            # Get Tmax, Tmin and Prcp Data from station
            #prcp = station_data[['date', 'prcp']]
            tmax = station_data[['date', 'tmax']]
            tmin = station_data[['date', 'tmin']]

            # Drop unnecessary NaN rows
            #prcp = prcp.dropna()
            tmax = tmax.dropna()
            tmin = tmin.dropna()

            # Get data for January
            tmax_jan = tmax[tmax['date'].str.contains('2017-01|2018-01|2019-01')]
            tmax_jan_len = len(tmax_jan)
            # tmax_jan_value = tmax_jan['tmax'].sum() / tmax_jan_len

            if tmax_jan_len != 0:
                tmax_jan_value = tmax_jan['tmax'].sum() / tmax_jan_len

            elif tmax_jan_len == 0:
                tmax_jan_value = -999999

            tmin_jan = tmin[tmin['date'].str.contains('2017-01|2018-01|2019-01')]
            tmin_jan_len = len(tmin_jan)
            # tmin_jan_value = tmin_jan['tmin'].sum() / tmin_jan_len

            if tmin_jan_len != 0:
                tmin_jan_value = tmin_jan['tmin'].sum() / tmin_jan_len

            elif tmin_jan_len == 0:
                tmin_jan_value = -999999

            # Get data for February
            tmax_feb = tmax[tmax['date'].str.contains('2017-02|2018-02|2019-02')]
            tmax_feb_len = len(tmax_feb)
            # tmax_feb_value = tmax_feb['tmax'].sum() / tmax_feb_len

            if tmax_feb_len != 0:
                tmax_feb_value = tmax_feb['tmax'].sum() / tmax_feb_len

            elif tmax_feb_len == 0:
                tmax_feb_value = -999999

            tmin_feb = tmin[tmin['date'].str.contains('2017-02|2018-02|2019-02')]
            tmin_feb_len = len(tmin_feb)
            # tmin_feb_value = tmin_feb['tmin'].sum() / tmin_feb_len

            if tmin_feb_len != 0:
                tmin_feb_value = tmin_feb['tmin'].sum() / tmin_feb_len

            elif tmin_feb_len == 0:
                tmin_feb_value = -999999

            # Get data for March
            tmax_mar = tmax[tmax['date'].str.contains('2017-03|2018-03|2019-03')]
            tmax_mar_len = len(tmax_mar)
            # tmax_mar_value = tmax_mar['tmax'].sum() / tmax_mar_len

            if tmax_mar_len != 0:
                tmax_mar_value = tmax_mar['tmax'].sum() / tmax_mar_len

            elif tmax_mar_len == 0:
                tmax_mar_value = -999999

            tmin_mar = tmin[tmin['date'].str.contains('2017-03|2018-03|2019-03')]
            tmin_mar_len = len(tmin_mar)
            # tmin_mar_value = tmin_mar['tmin'].sum() / tmin_mar_len

            if tmin_mar_len != 0:
                tmin_mar_value = tmin_mar['tmin'].sum() / tmin_mar_len

            elif tmax_mar_len == 0:
                tmin_mar_value = -999999

            # Get data for April
            tmax_apr = tmax[tmax['date'].str.contains('2017-04|2018-04|2019-04')]
            tmax_apr_len = len(tmax_apr)
            # tmax_apr_value = tmax_apr['tmax'].sum() / tmax_apr_len

            if tmax_apr_len != 0:
                tmax_apr_value = tmax_apr['tmax'].sum() / tmax_apr_len

            elif tmax_apr_len == 0:
                tmax_apr_value = -999999

            tmin_apr = tmin[tmin['date'].str.contains('2017-04|2018-04|2019-04')]
            tmin_apr_len = len(tmin_apr)
            # tmin_apr_value = tmin_apr['tmin'].sum() / tmin_apr_len

            if tmin_apr_len != 0:
                tmin_apr_value = tmin_apr['tmin'].sum() / tmin_apr_len

            elif tmin_apr_len == 0:
                tmin_apr_value = -999999

            # Get data for May
            tmax_may = tmax[tmax['date'].str.contains('2017-05|2018-05|2019-05')]
            tmax_may_len = len(tmax_may)
            # tmax_may_value = tmax_may['tmax'].sum() / tmax_may_len

            if tmax_may_len != 0:
                tmax_may_value = tmax_may['tmax'].sum() / tmax_may_len

            elif tmax_may_len == 0:
                tmax_may_value = -999999

            tmin_may = tmin[tmin['date'].str.contains('2017-05|2018-05|2019-05')]
            tmin_may_len = len(tmin_may)
            # tmin_may_value = tmin_may['tmin'].sum() / tmin_may_len

            if tmin_may_len != 0:
                tmin_may_value = tmin_may['tmin'].sum() / tmin_may_len

            elif tmin_may_len == 0:
                tmin_may_value = -999999

            # Get data for June
            tmax_jun = tmax[tmax['date'].str.contains('2017-06|2018-06|2019-06')]
            tmax_jun_len = len(tmax_jun)
            # tmax_jun_value = tmax_jun['tmax'].sum() / tmax_jun_len

            if tmax_jun_len != 0:
                tmax_jun_value = tmax_jun['tmax'].sum() / tmax_jun_len

            elif tmax_jun_len == 0:
                tmax_jun_value = -999999

            tmin_jun = tmin[tmin['date'].str.contains('2017-06|2018-06|2019-06')]
            tmin_jun_len = len(tmin_jun)
            # tmin_jun_value = tmin_jun['tmin'].sum() / tmin_jun_len

            if tmin_jun_len != 0:
                tmin_jun_value = tmin_jun['tmin'].sum() / tmin_jun_len

            elif tmin_jun_len == 0:
                tmin_jun_value = -999999

            # Get data for July
            tmax_jul = tmax[tmax['date'].str.contains('2017-07|2018-07|2019-07')]
            tmax_jul_len = len(tmax_jul)
            # tmax_jul_value = tmax_jul['tmax'].sum() / tmax_jul_len

            if tmax_jul_len != 0:
                tmax_jul_value = tmax_jul['tmax'].sum() / tmax_jul_len

            elif tmax_jul_len == 0:
                tmax_jul_value = -999999

            tmin_jul = tmin[tmin['date'].str.contains('2017-07|2018-07|2019-07')]
            tmin_jul_len = len(tmin_jul)
            # tmin_jul_value = tmin_jul['tmin'].sum() / tmin_jul_len

            if tmin_jul_len != 0:
                tmin_jul_value = tmin_jul['tmin'].sum() / tmin_jul_len

            elif tmin_jul_len == 0:
                tmin_jul_value = -999999

            # Get data for August
            tmax_aug = tmax[tmax['date'].str.contains('2017-08|2018-08|2019-08')]
            tmax_aug_len = len(tmax_aug)
            # tmax_aug_value = tmax_aug['tmax'].sum() / tmax_aug_len

            if tmax_aug_len != 0:
                tmax_aug_value = tmax_aug['tmax'].sum() / tmax_aug_len

            elif tmax_aug_len == 0:
                tmax_aug_value = -999999

            tmin_aug = tmin[tmin['date'].str.contains('2017-08|2018-08|2019-08')]
            tmin_aug_len = len(tmin_aug)
            # tmin_aug_value = tmin_aug['tmin'].sum() / tmin_aug_len

            if tmin_aug_len != 0:
                tmin_aug_value = tmin_aug['tmin'].sum() / tmin_aug_len

            elif tmin_aug_len == 0:
                tmin_aug_value = -999999

            # Get data for September
            tmax_sep = tmax[tmax['date'].str.contains('2017-09|2018-09|2019-09')]
            tmax_sep_len = len(tmax_sep)
            # tmax_sep_value = tmax_sep['tmax'].sum() / tmax_sep_len

            if tmax_sep_len != 0:
                tmax_sep_value = tmax_sep['tmax'].sum() / tmax_sep_len

            elif tmax_sep_len == 0:
                tmax_sep_value = -999999

            tmin_sep = tmin[tmin['date'].str.contains('2017-09|2018-09|2019-09')]
            tmin_sep_len = len(tmin_sep)
            # tmin_sep_value = tmin_sep['tmin'].sum() / tmin_sep_len

            if tmin_sep_len != 0:
                tmin_sep_value = tmin_sep['tmin'].sum() / tmin_sep_len

            elif tmin_sep_len == 0:
                tmin_sep_value = -999999

            # Get data for October
            tmax_oct = tmax[tmax['date'].str.contains('2017-10|2018-10|2019-10')]
            tmax_oct_len = len(tmax_oct)
            # tmax_oct_value = tmax_oct['tmax'].sum() / tmax_oct_len

            if tmax_oct_len != 0:
                tmax_oct_value = tmax_oct['tmax'].sum() / tmax_oct_len

            elif tmax_oct_len == 0:
                tmax_oct_value = -999999

            tmin_oct = tmin[tmin['date'].str.contains('2017-10|2018-10|2019-10')]
            tmin_oct_len = len(tmin_oct)
            # tmin_oct_value = tmin_oct['tmin'].sum() / tmin_oct_len

            if tmin_oct_len != 0:
                tmin_oct_value = tmin_oct['tmin'].sum() / tmin_oct_len

            elif tmin_oct_len == 0:
                tmin_oct_value = -999999

            # Get data for November
            tmax_nov = tmax[tmax['date'].str.contains('2017-11|2018-11|2019-11')]
            tmax_nov_len = len(tmax_nov)
            # tmax_nov_value = tmax_nov['tmax'].sum() / tmax_nov_len

            if tmax_nov_len != 0:
                tmax_nov_value = tmax_nov['tmax'].sum() / tmax_nov_len

            elif tmax_nov_len == 0:
                tmax_nov_value = -999999

            tmin_nov = tmin[tmin['date'].str.contains('2017-11|2018-11|2019-11')]
            tmin_nov_len = len(tmin_nov)
            # tmin_nov_value = tmin_nov['tmin'].sum() / tmin_nov_len

            if tmin_nov_len != 0:
                tmin_nov_value = tmin_nov['tmin'].sum() / tmin_nov_len

            elif tmin_nov_len == 0:
                tmin_nov_value = -999999

            # Get data fpr December
            tmax_dec = tmax[tmax['date'].str.contains('2017-12|2018-12|2019-12')]
            tmax_dec_len = len(tmax_dec)
            # tmax_dec_value = tmax_dec['tmax'].sum() / tmax_dec_len

            if tmax_dec_len != 0:
                tmax_dec_value = tmax_dec['tmax'].sum() / tmax_dec_len

            elif tmax_dec_len == 0:
                tmax_dec_value = -999999

            tmin_dec = tmin[tmin['date'].str.contains('2017-12|2018-12|2019-12')]
            tmin_dec_len = len(tmin_dec)
            # tmin_dec_value = tmin_dec['tmin'].sum() / tmin_dec_len

            if tmin_dec_len != 0:
                tmin_dec_value = tmin_dec['tmin'].sum() / tmin_dec_len

            elif tmin_dec_len == 0:
                tmin_dec_value = -999999

            # Append data to list
            data_list.append([station_id, tmax_jan_value, tmin_jan_value, tmax_feb_value, tmin_feb_value, tmax_mar_value,
                              tmin_mar_value, tmax_apr_value, tmin_apr_value, tmax_may_value, tmin_may_value,
                              tmax_jun_value, tmin_jun_value, tmax_jul_value, tmin_jul_value, tmax_aug_value,
                              tmin_aug_value, tmax_sep_value, tmin_sep_value, tmax_oct_value, tmin_oct_value,
                              tmax_nov_value, tmin_nov_value, tmax_dec_value, tmin_dec_value])

            print("Station with ID - " + station_id + " - inserted")

    # Create DataFrame from data_list
    weather_data = pd.DataFrame(data_list, columns=['stationId','tmax_jan_value', 'tmin_jan_value', 'tmax_feb_value',
                                                    'tmin_feb_value', 'tmax_mar_value', 'tmin_mar_value',
                                                    'tmax_apr_value', 'tmin_apr_value', 'tmax_may_value',
                                                    'tmin_may_value', 'tmax_jun_value', 'tmin_jun_value',
                                                    'tmax_jul_value', 'tmin_jul_value', 'tmax_aug_value',
                                                    'tmin_aug_value', 'tmax_sep_value', 'tmin_sep_value',
                                                    'tmax_oct_value', 'tmin_oct_value', 'tmax_nov_value',
                                                    'tmin_nov_value', 'tmax_dec_value', 'tmin_dec_value'])

    weather_data = weather_data[weather_data.loc[:,] != -999999].dropna()

    weather_data = weather_data.set_index('stationId')
    weather_data = weather_data / 10

    weather_data = weather_data.round(1)
    weather_data.to_csv("../data_processed/weatherData_clean.csv", index=True)

    # print(weather_data)


if __name__ == '__main__':
    main()