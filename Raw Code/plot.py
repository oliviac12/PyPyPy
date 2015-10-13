# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:13:23 2015

@author: Olivia Chen
"""


 import numpy as np
 import pandas as pd
 import matplotlib.pyplot as plt
 import matplotlib.dates as mdates
 # lineplot.py

# Make an array of x values
x = [1, 2, 3, 4, 5]
# Make an array of y values for each x value
y = [1, 4, 9, 16, 25]
# use pylab to plot x and y
pl.plot(x, y)
# show the plot on the screen
pl.show()
# use pylab to plot x and y as red circles
pl.plot(x, y, 'ro')
#color
pl.plot(x,y,'r')
#change line style
pl.plot(x, y, '--')
import datetime


Merge2 = pd.read_csv('Merge2.csv', header = False)
plotdate = Merge2[['Period kWh Production','DATE' ]]
plotdate.columns = ['Production','Date']
plotdate['Date'] = map(str,plotdate['Date'])
date = np.array([datetime.datetime.strptime(date, "%Y%m%d") for date in plotdate['Date']])
Production = np.array(plotdate['Production'])
plt.plot(date, Production)
plt.show()


