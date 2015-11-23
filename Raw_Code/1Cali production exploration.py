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

data = pd.read_csv('MeasuredProduction.csv', header = False)

# Subset the data to specific columns we need
Cali_cleanData = data[['Application Number','Program','Host Customer Physical Address City',
                        'Host Customer Physical Address County','Host Customer Physical Address Zip Code',
                        'Production Period End Date','Period kWh Production']]
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
latitude = [round(float(elem), 4) for elem in latitude]
Merge1['latitude'] = latitude

longtitude = []
for row in Merge1['Longtitude']:
    longtitude.append(row.replace('"', '').strip())
longtitude = [round(float(elem), 4) for elem in longtitude]
Merge1['longtitude'] = longtitude

#finalize the merge dataset
Merge1 = Merge1.drop('Latitude', 1)
Merge1 = Merge1.drop('Longtitude', 1)


Merge1.to_csv('Merge1.csv')


    
