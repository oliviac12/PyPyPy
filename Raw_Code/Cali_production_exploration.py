# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 09:58:28 2016

@author: Olivia Chen
"""

# open Measured production data from CSI website and merge it with Zipcode data set to match
#gps coordinates and elevation
# https://www.californiasolarstatistics.ca.gov/data_downloads/
import numpy as np
import geocoder as geo
import pandas as pd
# import geopy.distance
import datetime

def cleanMeansuredProduction():
    data = pd.read_csv('Raw_Data/MeasuredProduction_3-16-2016.csv')

# Subset the data to specific columns we need
    Cali_cleanData = data[['Application Number','Program','Host Customer Physical Address City',
                        'Host Customer Physical Address County','Host Customer Physical Address Zip Code',
                        'Production Period End Date','Period kWh Production']]
# rename variable zipcode

    Cali_cleanData.rename(columns={'Host Customer Physical Address Zip Code': 'ZipCode'}, inplace=True)
#open the zipcode data set to merge with the cali production data set
    zips = pd.read_csv('Raw_Data/zipcode.csv')
    Zip = zips[['zip code', 'latitude', 'longitude']]
    Zip.columns = ['ZipCode', 'Latitude', 'Longtitude']
#convert zipcode as string in order for mergeing later
#.loc[row_indexer,col_indexer] = value

    Cali_cleanData.loc[:,'ZipCode'] = Cali_cleanData['ZipCode'].astype(str)
#merge the zipcode and cali_prodcution
    Merge1 = pd.merge(Cali_cleanData, Zip, on='ZipCode', how='inner')
#clean the merged dataset, fixed gps location format
    Merge1.loc[:,'Latitude'] = Merge1.apply(lambda row: row['Latitude'].replace('"', '').strip(), axis = 1)
    Merge1.loc[:,'Longtitude'] = Merge1.apply(lambda row: row['Longtitude'].replace('"', '').strip(), axis = 1)
    return Merge1


#merge nameplate and calculated variable "specific yield" (raw production/nameplate)
Production = cleanMeansuredProduction()
#get nameplate

def get_nameplate():
    data = pd.read_csv('Raw_Data/WorkingDataSet_3-16-2016.csv')
    data = data[['Application Number', 'Nameplate Rating']]
    return data

Nameplate = get_nameplate()

name_merge = pd.merge(Production, Nameplate, on = ['Application Number'], how = 'left')
name_merge['Specific Yield'] = name_merge['Nameplate Rating']/name_merge['Period kWh Production']
# name_merge_nan = (name_merge.isnull().sum()/name_merge.shape[0])*100
# No missing value
# name_merge.to_csv('ProductionWithNameplate.csv')

###PICK UP HERE



#read percipitation data
tp = pd.read_csv('Rain_snow.csv', header = False)

#read temp data
temp = pd.read_csv('Temp.csv', header = False)

#create a new variable 'month' to help mereing
tp['DATE'] = map(str, tp['DATE'])
tp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in tp['DATE']]
temp['DATE'] = map(str, temp['DATE'])
temp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in temp['DATE']]



# Merge1.to_csv('Merge1.csv')
