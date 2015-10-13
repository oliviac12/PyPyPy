# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 10:15:36 2015

@author: Olivia Chen
"""

import numpy as np
import geocoder as geo
import pandas as pd
import geopy
import geopy.distance
import datetime

#Using Merge1 from the previous step
Merge1 = pd.read_csv('Merge1.csv', header = False)
SD_temp = pd.read_csv('SD_temp.csv', header = False)
SDproduction = Merge1[Merge1['Host Customer Physical Address County'] == 'San Diego']
sd_latitude = [round(float(elem), 4) for elem in SDproduction['latitude']]
sd_longitude = [round(float(elem), 4) for elem in SDproduction['longtitude']]
gps = zip(sd_latitude, sd_longitude)
unique_gps = set(gps)
unique_GPS = list(set(unique_gps))


#convert gps coordinate string into float
SD_temp['LATITUDE'] = map(float, SD_temp['LATITUDE'])
SD_temp['LONGITUDE'] = map(float, SD_temp['LONGITUDE'])
sd_latitude_temp = [round(float(elem), 4) for elem in SD_temp['LATITUDE']]
sd_longitude_temp = [round(float(elem), 4) for elem in SD_temp['LONGITUDE']]
sd_temp_gps = zip(sd_latitude_temp, sd_longitude_temp)
unique_SDTEMP = list(set(sd_temp_gps))

# find the nearest 

nearest_SDtemp = []
pts = [geopy.Point(p[0], p[1]) for p in unique_SDTEMP]
onept = [ geopy.Point(coord[0],coord[1]) for coord in unique_GPS ]
for coord in onept:
        alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts ]
        nearest_SDtemp.append(min(alldist, key=lambda x: (x[1]))[0])

unique = pd.DataFrame(unique_GPS)
unique.columns = ['latitude','longtitude']
unique['LATITUDE'] = [point[0] for point in nearest_SDtemp]
unique['LONGITUDE'] = [point[1] for point in nearest_SDtemp]


temp_merge = pd.merge(SD_temp, unique, on = ['LATITUDE','LONGITUDE'], how = 'inner')  #3486 obs 
temp_merge['DATE'] = map(str,temp_merge['DATE'])
temp_merge['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in temp_merge['DATE']]

SDproduction['month'] = [datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y") for date in SDproduction['Production Period End Date']]
merge2 = pd.merge(SDproduction, temp_merge, on = ['latitude', 'longtitude','month'], how = 'inner')

merge2.to_csv('Merge2.csv')

