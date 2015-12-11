#Creat GHI data for our locatioins in Cali production dataset, GHI is monthly the same for every year from 
#NREL, so ....
######################################################################################
Production = pd.read_csv('Merge1.csv', header = False)
import urllib2
import json
import numpy as np
from pandas.io.json import json_normalize
import itertools
import datetime
latitude = Production['latitude']
longtitude = Production['longtitude']
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
#try to build a dataframe of GHI, dont name your list as 

GHI = []
for ele in unique_GPS[700:794]:
    GHI.append(ghi(ele[0], ele[1]))   
#convert to data frame
GPS = pd.DataFrame(unique_GPS)
GHI = json_normalize(GHI)
f_GHI = pd.concat([GHI, GPS], axis=1)
f_GHI.columns = ['apr', 'aug', 'dec', 'feb','jan', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep', 'lat','log']
GHI1 = pd.melt(GHI, value_vars=['apr', 'aug', 'dec', 'feb','jan', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'])

lat = list(itertools.repeat(list(GPS[0]), 12))
Lat= sum(lat, [])
GHI1['lat'] = Lat

log = list(itertools.repeat(list(GPS[1]), 12))
Log = sum(log, [])
GHI1['log'] = Log
GHI1.to_csv('GHI.csv')


