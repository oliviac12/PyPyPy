# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:58:28 2015

@author: Olivia Chen
"""

# open Measured production data from CSI website and merge it with Zipcode data set to match 
#gps coordinates and elevation
# https://www.californiasolarstatistics.ca.gov/data_downloads/
import numpy as np
import geocoder as geo
import pandas as pd
data = pd.read_csv('MeasuredProduction1.csv', header = False)


Cali_cleanData = data[['Application Number','Program','Host Customer Physical Address City',
'Host Customer Physical Address Zip Code','Production Period End Date','Period kWh Production']]

Cali_cleanData.rename(columns={'Host Customer Physical Address Zip Code': 'ZipCode'}, inplace=True)

zips = pd.read_csv('zipcode.csv', header = False)
Zip = zips[['zip code', 'latitude', 'longitude']]
Zip.columns = ['ZipCode', 'Latitude', 'Longtitude']

   
Cali_cleanData['ZipCode'] = Cali_cleanData['ZipCode'].astype(str)
Merge1 = pd.merge(Cali_cleanData, Zip, on='ZipCode', how='inner')
latitude = []
for row in Merge1['Latitude']:
    latitude.append(row.replace('"', '').strip())
Merge1['latitude'] = latitude
longtitude = []
for row in Merge1['Longtitude']:
    longtitude.append(row.replace('"', '').strip())
Merge1['longtitude'] = longtitude
Merge1 = Merge1.drop('Latitude', 1)
Merge1 = Merge1.drop('Longtitude', 1)
Merge1['latitude'] = Merge1['latitude'].astype(float)
Merge1['longtitude'] = Merge1['longtitude'].astype(float)


#how to use elevation how to use elevation ???????
elevation = []
gps = zip(latitude, longtitude)
unique = set(gps)
for la, lo in unique:
    ele = geo.elevation([la,lo])
    elevation.append(ele.feet)
    
    
    
elevation(latitude, longtitude)
elevation.feet
elevation = []
elevation = geo.elevation([Merge1['latitude'], Merge1['longtitude']])
Merge1['elevation'] = elevation
    
