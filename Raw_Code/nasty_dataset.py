
#32.75 ,-116.95
#8-Mar


from itertools import islice
import csv
import numpy as np
import datetime
import itertools

name = range(3,1476)
mon = pd.DataFrame()
name = range(3, 11)
name = range(11, 20)


for ele in name:
    filename = 'GHI_' + str(ele) + '.csv'
    with open(filename, 'rU') as csvfile:
        csv_f = csv.reader(csvfile)
        gps = next(csv_f)[4:6]
        data = []
        for row in islice(csv_f, 1, 8760):
            data.append(filter(None, row))
    data1 = np.array(data)
    #data1 = np.dtype(np.str_, 10)
    Monthly = Convert_mon(data1)
    mon = pd.concat([mon, Monthly])
    print mon
    
mon.to_csv('Finally_monthly.csv')
  
#Data = pd.DataFrame(data[1:,1:], index=data[1:,0], columns=data[0,1:])

