# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:42:20 2015

@author: qinnanchen
"""

from bs4 import BeautifulSoup
import urllib2
import pandas as pd 

def extract(soup, month)
mon_snow = "https://weather-warehouse.com/WeatherHistory/PastWeatherData_SanDiegoSeaworld_SanDiego_CA_January.html"
page = urllib2.urlopen(mon_snow)
soup = BeautifulSoup(page)
year = []
total_snow = []
max24_snow = []
table = soup.find(class_= "stripeMe")
for row in table.findAll('tr')[1:]:
    col = row.findAll('td')
    col1 = col[0].string
    year.append(col1)
    col2 = col[10].string
    total_snow.append(col2)
    col3 = col[11].string
    max24_snow.append(col3)
    Jan_snow = {'Year' : year, 'Total Snow' : total_snow, 'Max Snow in 24hr' : max24_snow}
    
urlbase = 'https://weather-warehouse.com/WeatherHistory/PastWeatherData_SanDiegoSeaworld_SanDiego_CA_'
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
for month in months:
    url = urlbase + month + '.html'
    print url 


