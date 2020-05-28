import pandas as pd
import numpy as np
from geopy import distance
from datetime import datetime


df = pd.read_csv('201809-citibike-tripdata.csv')

# total number of rows and columns in the dataset
_shape = df.shape
# Find the average trip length in minutes (tripduration column) accurate to 2 digits
_apply = df['tripduration'].apply(lambda x: x / 60)
_mean = round(_apply.mean(), 2)

# How many trips started and ended at the same station?
df_same_1 = df.where(df['start station name'] == df['end station name']).notnull()
_list = [station_name for station_name in df_same_1['start station name'] if station_name is True]
stations_value = len(_list)

# What is the most used bikeid in the city by the number of rides?
s = df['bikeid'].value_counts().head()

# bike id (bikeid), which on average has longer rides than all others
df_group = df.groupby('bikeid')[['tripduration']].sum().sort_values(['tripduration'], ascending=False)


# How many rows are missing start station id data?
_list = [station_name for station_name in df['start station name'].notnull() if station_name is False]
empty_rows = len(_list)

# average trip duration in minutes depending on the type of subscription
df_group = df.groupby('usertype')[['tripduration']].mean()
_apply = round(df_group.apply(lambda x: x/60), 2)

# the average length of trips in kilometers with an accuracy of 2 digits, previously throwing closed trajectories
df_rc = df.drop(np.where(df['start station name'] == df['end station name'])[0])
list_s = list(zip(df_rc['start station latitude'], df_rc['start station longitude']))
list_e = list(zip(df_rc['end station latitude'], df_rc['end station longitude']))
loc_dict = dict(zip(list_s,list_e))
dist = [distance.distance(key, value).km for key, value in loc_dict.items()]
dist_df = pd.DataFrame(np.array([dist])).T
col = dist_df.columns


# station (start station id) with a maximum number of departures from 18 to 20 pm inclusive
df['starttime'] = pd.to_datetime(df['starttime'])
start_date = '18:00'
end_date = '20:00'
ts_df = df[(df['starttime'] > datetime(2018, 9, 1))]
_list = [st_time for st_time in df['starttime'] if 18 < st_time < 20]


