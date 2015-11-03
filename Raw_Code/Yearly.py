import pandas as pd
import datetime

d = pd.read_csv('MeasuredProduction.csv', header = False)
#d['Production Period End Date'] = map(str, d['Production Period End Date'])
d['Year'] = [datetime.datetime.strptime(date, "%m/%d/%y").strftime("%Y") for date in d['Production Period End Date']]
Application = list(set(d['Application Number']))
