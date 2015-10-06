# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:18:11 2015

@author: Olivia Chen
"""
import urllib2
import json
import requests
f = urllib2.urlopen('http://api.wunderground.com/api/e6a109eddf157c39/planner_07010731/q/CA/San_Francisco.json')
json_string = f.read()
parsed_json = json.loads(json_string)
s_Date = parsed_json['trip']['period_of_record']['date_start']['date']['day']
s_Monoth = parsed_json['trip']['period_of_record']['date_start']['date']['month']
s_year = Date = parsed_json['trip']['period_of_record']['date_start']['date']['year']
e_Date = parsed_json['trip']['period_of_record']['date_end']['date']['day']
e_Monoth = parsed_json['trip']['period_of_record']['date_end']['date']['month']
e_year = Date = parsed_json['trip']['period_of_record']['date_end']['date']['year']
print "Current temperature in %s is: %s" % (location, temp_f)

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