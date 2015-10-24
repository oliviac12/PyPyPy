# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:25:24 2015

@author: qinnanchen
"""

import pandas as pd
zips = pd.read_csv('zips.csv', header = False)
Zip = zips[['zip code', 'latitude', 'longitude']]
Zip.columns = ['ZipCode', 'Latitude', 'Longtitude']
ziptest = pd.read_csv('Ziptest.csv', header = False)

import re
for zip in Zip.ZipCode:
    re.search("[0-9]*", zip)

for row in Zip.ZipCode:
        if "H" in Zip.ZipCode:
            
        else:
            Zip.Valid= "valid"
        
            



Zip.ZipCode = ["9999" for row in Zip.ZipCode if "H" in row[3]]

        
Zip = Zip["H" or "X" not in zip for zip in Zip.ZipCode]
#try merge them as string 
pd.merge(ziptest, Zip, on='ZipCode', how='inner')
ziptest['ZipCode'] = ziptest['ZipCode'].astype(str)


