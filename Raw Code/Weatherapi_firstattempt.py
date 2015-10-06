# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:18:11 2015

@author: Olivia Chen
"""
import urllib2
import json
import requests
f = urllib2.urlopen('https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=Qpa5B4aYqoSYi0C4jeGgbtVkM91k5ZSU7KZi849R&lat=32.8999&lon=-117.20722')
json_string = f.read()
parsed_json = json.loads(json_string)
monthly_ghi = parsed_json['outputs']['avg_ghi']['monthly']



#using noaa web servise, needed token in the head parameter instead of API key
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCNDMS&locationid=ZIP:94404&startdate=2007-01-01&enddate=2007-12-30'

url1 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?'
url2 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes'
URL3 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets'
response = requests.get(url, headers={'token':'FDTLhHxYJAIGtXwiIvSSmpmyipjiMEHw'})
parsed_json = response.json()
datatypeid=MNTM

URL1 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCNDMS&locationid=CNTY:San Diego&startdate=2010-05-01&enddate=2010-06-01'
response = requests.get(URL1, headers= {'token':'FDTLhHxYJAIGtXwiIvSSmpmyipjiMEHw'})
response = requests.get(url2, headers= {'token':'FDTLhHxYJAIGtXwiIvSSmpmyipjiMEHw'})

location = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locationcategories"
response = requests.get(location, headers= {'token':'FDTLhHxYJAIGtXwiIvSSmpmyipjiMEHw'})