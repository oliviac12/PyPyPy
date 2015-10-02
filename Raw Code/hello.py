# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:24:12 2015

@author: Olivia Chen
"""



import geocoder
def coordinate(place):
    g = geocoder.google(place)
    print (g.latlng)
    
place = 'Davis,CA'
coordinate(place)

