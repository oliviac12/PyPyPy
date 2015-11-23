import numpy as py
import itertools

#finding all tge points covering california based on 10km tiles
log1 = list(py.arange(-124.15, -120, 0.1))
log2 = list( py.arange(-123.75, -114.7, 0.1))
log = log1 + log2
log= [round(ele, 2) for ele in log]
lat1 = list(py.arange(39.05, 42, 0.1))
lat2 = list(py.arange(32.55, 39.05, 0.1))
lat = lat1 + lat2
lat = [round(ele, 2) for ele in lat]
Points = []
for Ele in lat:
    for ele in log:
        point = (Ele, ele)
        Points.append(point)
        
#359 unique GPS coorditaes in our date set
import pandas as pd
Data = pd.read_csv("f_DFF.csv", header = False)
Data['CSI Project Tilt'][Data['CSI Project Tilt'].isnull()]
Data = Data[pd.notnull(Data['CSI Project Tilt'])]
Data = Data[pd.notnull(Data['Specific_Yield'])]
GPS = zip(Data['latitude'], Data['longtitude'])
unique = set(GPS)
len(unique)  #359
Clo = []
for tp in unique:
    for pos in Points:
        if (pos[0]-0.05 <= tp[0] <= pos[0]+0.05) and (pos[1]-0.05 <= tp[1] <= pos[1]+0.05):
            Clo.append(pos)
        break
            
uniqueclo = list(set(Clo))
Coord = pd.DataFrame()
Coord['actual'] = list(unique)[0:358]
Coord['closest'] = list(Clo)
Coord.to_csv("ghipoints.csv")
UNIQUE = pd.DataFrame(uniqueclo)
UNIQUE.to_csv("solaranywhere.csv")
