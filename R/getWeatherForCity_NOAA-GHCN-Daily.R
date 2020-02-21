# Import Libraries
library(rnoaa)
library(readr)

getwd()
# Set Working directory and options
dir = "../python/data_raw"
setwd(dir)
getwd()

# station <- meteo_tidy_ghcnd("AEM00041217", keep_flags = FALSE, var = c("TMAX", "TMIN"), date_min = "2010-01-01", date_max = "2018-12-31")

# Read csv with cities

cities <- read_csv("allCitiesOver100k.csv")
rows <- nrow(cities)
station_data <- ghcnd_stations()

dir = "../data_raw/weatherDataPerStation"
setwd(dir)
getwd()

dir = "../"
setwd(dir)
getwd()

dir = "../data_raw/weatherDataPerStation"
setwd(dir)
getwd()

full_station_city_data = data.frame(cityId = numeric(), y = character(), latitude = numeric(), longitude = numeric())

# Iterate through all rows an get nearby weather stations
for (t in 1:rows) {
  row <- cities[t,]
  lat <- row['lat']
  lon <- row['lon']
  name_city <- row['cityName']
  id_city <- row['cityId']
  rm(city)
  city <- data.frame(id = "city", latitude = lat, longitude = lon)
  nearby_stations <- meteo_nearby_stations(lat_lon_df = city, lat_colname = "lat", lon_colname = "lon", station_data = station_data, radius = 100, var = c("TMAX", "TMIN"), year_min = 2010, year_max = 2018)
  id = nearby_stations$city
  station_id = id$id
  id1 = station_id[1]
  id1 <- trimws(id1)
  
  dist = id$distance
  dist = dist[1]
  
  if (!is.na(id1)) {
    csv_file <- paste(id1, ".csv")
    try(weather_data <- meteo_tidy_ghcnd(stationid = id1, var = c("TMAX","TMIN", "PRCP"), date_min = "2010-01-01"))
    try(write.table(weather_data, file = csv_file, ",", append = FALSE, quote = FALSE, col.names = TRUE, row.names = FALSE))
    full_station_city_data <- rbind(full_station_city_data, data.frame(cityId = id_city, stationId = id1, latitude = lat, longitude = lon, distance = dist))
  }
  
  }

dir = "../"
setwd(dir)
getwd()
write.table(full_station_city_data, file = "weatherStationsByCity.csv", sep = ",", append = FALSE, quote = FALSE,
            col.names = TRUE, row.names = FALSE)


