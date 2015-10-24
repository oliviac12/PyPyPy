# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:22:38 2015

@author: Olivia Chen
"""

# match zip code with GPS coordinate and elevation by using the zipcode.csv in raw data

import pandas as pd
zips = pd.read_csv('zipcode.csv', header = False)
Zip = zips[['zip code', 'latitude', 'longitude']]
Zip.columns = ['ZipCode', 'Latitude', 'Longtitude']

   
Cali_cleanData['ZipCode'] = Cali_cleanData['ZipCode'].astype(str)
MergeZip = pd.merge(Cali_cleanData, Zip, on='ZipCode', how='inner')