
import pandas as pd
import datetime 
data = pd.read_csv('f_DFF.csv', header = False)
GHI = pd.read_csv('GHI.csv',header = False)
data.columns
data['M'] = [datetime.datetime.strptime(date, "%d-%b").strftime("%b") for date in data['month_x']]
data['M'] = [m.lower() for m in data['M']]
GHI.columns
GHI = GHI.drop("Unnamed: 0",1)
GHI.columns = ['M', 'GHI','latitude', 'longtitude']
add_GHI = pd.merge(data, GHI, on = ['M','latitude', 'longtitude'], how= 'left' )
add_GHI['GHI']
add_GHI.to_csv('f_DFF.csv')
