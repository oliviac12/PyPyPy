# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 10:15:36 2015

@author: Olivia Chen
"""

import pandas as pd
import geopy
import geopy.distance
import datetime


#Using Merge1 from the previous step
Merge1 = pd.read_csv('Merge1.csv', header=False)
SD_temp = pd.read_csv('SD_temp.csv', header = False)
SD_tp = pd.read_csv('SD_tp.csv', header = False)
SDproduction = Merge1[Merge1['Host Customer Physical Address County'] == 'San Diego']
sd_latitude = [round(float(elem), 4) for elem in SDproduction['latitude']]
sd_longitude = [round(float(elem), 4) for elem in SDproduction['longtitude']]
#get unique lartitude and longitutde
gps = zip(sd_latitude, sd_longitude)
unique_gps = set(gps)
unique_GPS = list(set(unique_gps))

#### MERGE PRODUCTION with SD PERCIPITATION
#get unique lartitude and longitutde to SD_tp
SD_tp['LATITUDE'] = map(float, SD_tp['LATITUDE'])
SD_tp['LONGITUDE'] = map(float, SD_tp['LONGITUDE'])
sd_latitude_tp = [round(float(elem), 4) for elem in SD_tp['LATITUDE']]
sd_longitude_tp = [round(float(elem), 4) for elem in SD_tp['LONGITUDE']]
sd_tp_gps = zip(sd_latitude_tp, sd_longitude_tp)
unique_SDTP = list(set(sd_tp_gps))

# find the nearest avaibale percipitation info for production 
nearest_SDtp = []
pts_tp = [geopy.Point(p[0], p[1]) for p in unique_SDTP]
onept = [ geopy.Point(coord[0],coord[1]) for coord in unique_GPS ]
for coord in onept:
        alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts_tp ]
        if min(alldist, key=lambda x: (x[1]))[1] < 25:
            nearest_SDtp.append(min(alldist, key=lambda x: (x[1]))[0])
        else:
            nearest_SDtp.append(-9999)

# put original lat,log and nearest points togther 
unique = pd.DataFrame(unique_GPS)
unique.columns = ['latitude','longtitude']
unique['LATITUDE'] = [point[0] for point in nearest_SDtp]
unique['LONGITUDE'] = [point[1] for point in nearest_SDtp]


#merge SD_tp and unique
tp_merge = pd.merge(SD_tp, unique, on = ['LATITUDE','LONGITUDE'], how = 'left')
#check if there's missing value
tp_merge['DATE'][tp_merge['DATE'].isnull()]
#convert 'DATE' type from float to int in order to convert to datetime later 
tp_merge['DATE'] = map(str,tp_merge['DATE'])
#creat a new variable to indicate only month and year of the date called 'month'
tp_merge['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in tp_merge['DATE']]
#same time for production data so we can merge on 'month' later
SDproduction['month'] = [datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y") for date in SDproduction['Production Period End Date']]
#subset tp_merge to only varibale that we are interested in the future. 
TP_merge = tp_merge[['latitude', 'longtitude','TPCP','TSNW','month']]
#merge TP_merge with production
merge2 = pd.merge(SDproduction, TP_merge, on = ['latitude', 'longtitude','month'], how = 'left')
#check missing value
merge2['TPCP'][merge2['TPCP'].isnull()]  #7993 missing value, about 40% of the total ummmmm

#subset the missing value
missing =merge2[pd.isnull(merge2['TPCP'])]


#### MERGE PRODUCTION with SD TEMP

#convert gps coordinate string into float in SD_temp
SD_temp['LATITUDE'] = map(float, SD_temp['LATITUDE'])
SD_temp['LONGITUDE'] = map(float, SD_temp['LONGITUDE'])
sd_latitude_temp = [round(float(elem), 4) for elem in SD_temp['LATITUDE']]
sd_longitude_temp = [round(float(elem), 4) for elem in SD_temp['LONGITUDE']]
sd_temp_gps = zip(sd_latitude_temp, sd_longitude_temp)
unique_SDTEMP = list(set(sd_temp_gps))

#find the nearest for sd_temp
nearest_SDtemp = []
pts = [geopy.Point(p[0], p[1]) for p in unique_SDTEMP]
onept = [ geopy.Point(coord[0],coord[1]) for coord in unique_GPS ]
for coord in onept:
        alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts ]
        if min(alldist, key=lambda x: (x[1]))[1] < 25:
            nearest_SDtemp.append(min(alldist, key=lambda x: (x[1]))[0])
        else:
            nearest_SDtemp.append(-9999)

unique = pd.DataFrame(unique_GPS)
unique.columns = ['latitude','longtitude']
unique['LATITUDE'] = [point[0] for point in nearest_SDtemp]
unique['LONGITUDE'] = [point[1] for point in nearest_SDtemp]

#merge SD_tp and unique
tp_merge = pd.merge(SD_tp, unique, on = ['LATITUDE','LONGITUDE'], how = 'left')
#check if there's missing value
tp_merge['DATE'][tp_merge['DATE'].isnull()]
#convert 'DATE' type from float to int in order to convert to datetime later 
tp_merge['DATE'] = map(str,temp_merge['DATE'])
#creat a new variable to indicate only month and year of the date called 'month'
tp_merge['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in tp_merge['DATE']]
#same time for production data so we can merge on 'month' later
SDproduction['month'] = [datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y") for date in SDproduction['Production Period End Date']]
#subset tp_merge to only varibale that we are interested in the future. 
TP_merge = tp_merge[['latitude', 'longtitude','TPCP','TSNW','month']]
#merge TP_merge with production
merge2 = pd.merge(SDproduction, TP_merge, on = ['latitude', 'longtitude','month'], how = 'left')
#check missing value
merge2['TPCP'][merge2['TPCP'].isnull()]  #7993 missing value, about 40% of the total ummmmm

missing = merge2[pd.null(merge2['TPCP'])]
merge2.to_csv('Merge2.csv')

