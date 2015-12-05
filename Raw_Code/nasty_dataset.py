
#32.75 ,-116.95
#8-Mar


from itertools import islice
import csv
import numpy as np
import datetime
import itertools
data = []
with open('GHI-1.csv', 'rb') as csvfile:
    csv_f = csv.reader(csvfile)
    first = next(csv_f)
    gps = first[4:6]
    for row in islice(csv_f, 1, None):
        data.append(filter(None, row))
    data = np.array(data)
  
#Data = pd.DataFrame(data[1:,1:], index=data[1:,0], columns=data[0,1:])

Data = pd.DataFrame(data, columns = ['Date', 'Time', 'GHI', 'X', 'DNI', 'Y', 'DHI','z'])
Data['Date'] = [datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y") for date in Data['Date']]
Data['GHI'] = map(int, Data['GHI'])
Data['DNI'] = map(int, Data['DNI'])
Data['DHI'] = map(int, Data['DHI'])
GHI = list(Data.groupby(by=['Date'])['GHI'].sum()/1000)
DNI = list(Data.groupby(by=['Date'])['DNI'].sum()/1000)
DHI = list(Data.groupby(by=['Date'])['DHI'].sum()/1000)
unique_Date = list(set(Data['Date']))
lat = list(itertools.repeat(gps[0], 13))
log = list(itertools.repeat(gps[1], 13))
Monthly = pd.DataFrame()
#Monthly = pd.DataFrame(GHI, DNI, DHI, columns = ['GHI','DNI','DHI'])
Monthly['Lat'] = lat
Monthly['Log'] = log
Monthly['GHI'] = GHI
Monthly['DNI'] = DNI
Monthly['DHI'] = DHI
Monthly['Date'] = unique_Date

