import numpy as np
import pandas as pd

from geopy.distance import vincenty
import datetime
import time

citybike = pd.read_csv('/home/vlad/PycharmProjects/data-analytics/data/201809-citibike-tripdata.csv')
head = citybike.head()
shape = citybike.shape

# average travel time in minutes
citybike['tripduration'] = citybike['tripduration'] / 60
ave_trip = round(citybike.describe()['tripduration']['mean'], 2)

# How many trips started and ended at the same station?
_shape = citybike[(citybike['start station id'] == citybike['end station id'])].shape

# How many trips started and ended at the same station? Indicate the number of unique bikes
unique_trip = citybike[(citybike['start station id'] == citybike['end station id'])]['bikeid'].unique().shape

# What is the most used bikeid in the city by the number of rides?
most_used = citybike['bikeid'].value_counts()[:1]

# Find a bike (bikeid), which on average has longer rides than everyone else
long_ride = citybike.groupby('bikeid')['tripduration'].mean().sort_values(ascending=False)[:1]

# Find the number of rows missing start station id
missing_start = citybike[citybike['start station id'].isnull()].shape

# What is the average trip duration depending on the type of subscription with an accuracy of 2 digits?
sub_type = round(citybike.groupby('usertype')['tripduration'].mean(), 2)

# For each station, find the distance between stations
distance_s = citybike['distance_km'] = citybike.apply(
    lambda x: vincenty((x['start station latitude'], x['start station longitude']),
                       (x['end station latitude'], x['end station longitude'])).kilometers, axis=1
)
# and then find the average distance for all trips, having previously thrown out closed trajectories
# (those with the same start station id = end station id).
mean_value = (citybike['distance_km'].mean())
end_st_id = citybike['end station name'].value_counts()[:5]

# Select a station (start station id) with a maximum number of departures from 18 to 20 pm
citybike['end_hour'] = citybike['stoptime'].apply(lambda x: datetime.datetime.fromtimestamp(
    time.mktime(datetime.datetime.strptime(x.strip(), "%Y-%m-%d %H:%M:%S.%f").timetuple())).hour
                                                  )

citybike['start_hour'] = citybike['starttime'].apply(lambda x: datetime.datetime.fromtimestamp(

    time.mktime(datetime.datetime.strptime(x.strip(), "%Y-%m-%d %H:%M:%S.%f").timetuple())).hour
                                                     )

data = citybike[(citybike.start_hour.isin([18, 19, 20]))]['start station id'].value_counts().head()

# Select the stations (end station id) that arrive from 6 a.m. to 10 a.m.
end_stations = [3140, 3106, 3116, 369]
citybike[(citybike.end_hour.isin([6, 7, 8, 9, 10])) &
         (citybike['end station id'].isin(end_stations))]['end station id'].unique()

find_st = citybike[(citybike.end_hour.isin([6, 7, 8, 9, 10])) &
                   (citybike['end station id'].isin(end_stations))]['end station id'].unique()

selective_station = np.array([3106., 3116., 3140., 369.])
