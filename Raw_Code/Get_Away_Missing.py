import pandas as pd
Data = pd.read_csv("f_DFF.csv", header = False)
Data['CSI Project Tilt'][Data['CSI Project Tilt'].isnull()]
Data = Data[pd.notnull(Data['CSI Project Tilt'])]
Data = Data[pd.notnull(Data['Specific_Yield'])]
GPS = zip(Data['latitude'], Data['longtitude'])
unique = set(GPS)
len(unique)  #359

