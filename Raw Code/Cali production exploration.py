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

# Subset the data to specific columns we need
Cali_cleanData = data[['Application Number','Program','Host Customer Physical Address City',
'Host Customer Physical Address Zip Code','Production Period End Date','Period kWh Production']]
# rename variable zipcode
Cali_cleanData.rename(columns={'Host Customer Physical Address Zip Code': 'ZipCode'}, inplace=True)
#open the zipcode data set to merge with the cali production data set
zips = pd.read_csv('zipcode.csv', header = False)
Zip = zips[['zip code', 'latitude', 'longitude']]
Zip.columns = ['ZipCode', 'Latitude', 'Longtitude']
#convert zipcode as string in order for mergeing later 
Cali_cleanData['ZipCode'] = Cali_cleanData['ZipCode'].astype(str)
#merge the zipcode and cali_prodcution
Merge1 = pd.merge(Cali_cleanData, Zip, on='ZipCode', how='inner')
#clean the merged dataset, fixed gps location format
latitude = []
for row in Merge1['Latitude']:
    latitude.append(row.replace('"', '').strip())
Merge1['latitude'] = latitude
longtitude = []
for row in Merge1['Longtitude']:
    longtitude.append(row.replace('"', '').strip())
Merge1['longtitude'] = longtitude
#finalize the merge dataset
Merge1 = Merge1.drop('Latitude', 1)
Merge1 = Merge1.drop('Longtitude', 1)

Merge1.to_csv('Merge1.csv')

#Creat GHI data for our locatioins in Cali production dataset
######################################################################################

import urllib2
import json
import numpy as np
latitude = np.array(latitude)
longtitude = np.array(longtitude)
latitude = map(float, latitude)
longtitude = map(float, longtitude) 
gps = zip(latitude, longtitude)
unique_gps = set(gps)
unique_GPS = list(set(unique_gps))
#creating a function to get GHI of a specific location
def ghi(lat, lon):
    baseurl = 'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=Qpa5B4aYqoSYi0C4jeGgbtVkM91k5ZSU7KZi849R&'
    url = baseurl +'lat=' + str(lat) + '&' + 'lon=' + str(lon)
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    monthly_ghi = parsed_json['outputs']['avg_ghi']['monthly']
    return monthly_ghi
#try to build a dataframe of GHI
GHI_jan = []   
GHI_jan(ghi(32.89999,-117.20722))
GHI.append(ghi(32.761801,-117.01273))
for gps in unique_GPS:
    ghi.append(ghi(gps)     
    
    
elevation(latitude, longtitude)
elevation.feet
elevation = []
elevation = geo.elevation([Merge1['latitude'], Merge1['longtitude']])
Merge1['elevation'] = elevation
    
