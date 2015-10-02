# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:24:12 2015

@author: Olivia Chen
"""
import geocoder
g = geocoder.google("San Diego, CA")
   # gps = []
elevation = geocoder.elevation([g.latlng[0], g.latlng[1]])
geocoder.elevation([32.899996, -117.20722])

g2 = geocoder.elevation([32.899996, -117.20722])

lat = g.latlng[0]
lng = g.latlng[1] 
g = geocoder.google("San Diego, CA")
   # gps = []
elevation = geocoder.elevation([g.latlng[0], g.latlng[1]])
geocoder.elevation([32.899996, -117.20722])

g2 = geo.elevation([32.899996, -117.20722])

lat = g.latlng[0]
lng = g.latlng[1] 
 





