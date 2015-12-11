import pandas as pd
import datetime


#load realGHI data
RealGHI = pd.read_csv("Final_monthly.csv", header = False)
#drop unnecessary columns
RealGHI = RealGHI.drop('Unnamed: 0', 1)
RealGHI = RealGHI.drop('Unnamed: 0.1', 1)
# type(RealGHI.lat[0])   numpy.float64

#load ghipoints data to connect cloest and actual points 
ghipoints = pd.read_csv("ghipoints.csv", header = False)
actual_lat = [gps[1: -1].split(', ')[0] for gps in ghipoints['actual']]
actual_log = [gps[1: -1].split(', ')[1] for gps in ghipoints['actual']]
lat = map(float, actual_lat)
log = map(float, actual_log)
lat = [round(la, 4) for la in lat]
log = [round(lo, 4) for lo in log]
ghipoints['latitude'] = lat
ghipoints['longtitude'] = log
clo_lat = [ point[1:6] for point in ghipoints['closest']]
clo_lat= map(float, clo_lat)
clo_log = [ point[8: -1] for point in ghipoints['closest']]
clo_log = map(float, clo_log)
ghipoints['clo_lat'] = clo_lat
ghipoints['clo_log'] = clo_log
ghipoints = ghipoints.drop('closest', 1)
ghipoints = ghipoints.drop('actual', 1)


#load MAIN DATA (data set used for modeling) 
main = pd.read_csv("f_DFF.csv", header = False)
main = main[pd.notnull(main['CSI Project Tilt'])]
main = main[pd.notnull(main['Specific_Yield'])]

#Merge Main DATA and ghipoints with actual log and lat
gps_Merge = pd.merge(main, ghipoints, on=['latitude','longtitude'], how='inner')

#go back to RealGHI data, make sure cloest coordinate is in the same format as Main data
#RealGHI['closest'] = zip(RealGHI['lat'], RealGHI['log'])

#Merge Main Data with RealGHI with cloest and Data
gps_Merge['Production Period End Date'] = [datetime.datetime.strptime(date, "%m/%d/%y" ).strftime("%m/%Y") for date in gps_Merge['Production Period End Date']]
gps_Merge.rename(columns={'Production Period End Date': 'Date' }, inplace=True)
gps_Merge.rename(columns={'GHI': 'ghi' }, inplace=True)
RealGHI.rename(columns={'lat': 'clo_lat', 'log':'clo_log' }, inplace=True)
final_merge = pd.merge(gps_Merge, RealGHI, on=['Date', 'clo_lat', 'clo_log'], how='inner') #not working











ghipoints = ghipoints.drop('closest', 1)
ghipoints.rename(columns={'actual': 'GPS'}, inplace=True)


#Get ready to merge solaranywhere cloest GPS to actual GPS

latitude = [ round(lat, 4) for lat in Data['latitude']]
logtitude = [ round(log, 4) for log in Data['longtitude']]
Data['GPS'] = zip(latitude, logtitude)



#ghipoints = ghipoints.drop('actual_lat', 1)
#ghipoints = ghipoints.drop('actual_log', 1)
ghipoints = ghipoints.drop('GPS', 1)
gps_Merge = pd.merge(Data, ghipoints, on=['latitude','longtitude'], how='inner')
gps['clo_log'][Data['clo_log'].isnull()]
type(ghipoints['GPS'])
type(Data['GPS'])


gps_Merge.tail()

gps_Merge.rename(columns={'Production Period End Date': 'Date' }, inplace=True)
gps_Merge.rename(columns={'GHI': 'ghi' }, inplace=True)
RealGHI.rename(columns={'latitude': 'clo_lat', 'longtitude': 'clo_log' }, inplace=True)
final_merge = pd.merge(gps_Merge, RealGHI, on=['clo_lat','clo_log', 'Date'], how='left')
gps_Merge.head()
RealGHI.head()
RealGHI = RealGHI.drop('', 1)
