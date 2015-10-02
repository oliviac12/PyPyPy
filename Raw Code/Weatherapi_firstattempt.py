# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:18:11 2015

@author: Olivia Chen
"""
import urllib2
import json
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