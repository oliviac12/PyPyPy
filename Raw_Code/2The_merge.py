import pandas as pd
import geopy
import geopy.distance
import datetime

#merge nameplate and calculated variable "specific yield" (raw production/nameplate)
Production = cleanMeansuredProduction()
Nameplate = pd.read_csv('Nameplate.csv',header = False)
name_merge = pd.merge(Production, Nameplate, on = ['Application Number'], how = 'left')
name_merge['Specific Yield'] = name_merge['Nameplate Rating']/name_merge['Period kWh Production']
name_merge.to_csv('ProductionWithNameplate.csv')

#read percipitation data
tp = pd.read_csv('Rain_snow.csv', header = False)

#read temp data
temp = pd.read_csv('Temp.csv', header = False)

#create a new variable 'month' to help mereing
tp['DATE'] = map(str, tp['DATE'])
tp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in tp['DATE']]
temp['DATE'] = map(str, temp['DATE'])
temp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in temp['DATE']]

#creat month for production data as well
#since production period date might ends on the first day of the month,
#we need to make sure they are using the temp from the last month
month = []
for date in name_merge['Production Period End Date']:
    if datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%d") == '01':
        if datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%m") == '01':
            m = 12
        else:
            m = int(datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%m")) - 1
        y = int(datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y"))
        new = str(m) + '/' + str(y)
        month.append(datetime.datetime.strptime(new, "%m/%Y").strftime("%m/%Y"))
    else:
        month.append(datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%m/%Y"))

name_merge['month'] = month

# for merging production with percipitation and temp data, need to make sure
# they are merging within the same month. so I subset all the data for the same month
# then find the cloest GPS point in weather data for production data, then merge

#Merge production with percipitation data
#def nearest(Month):
#for Month in name_merge['month']:
def nearest(Month):
    s_r = tp[tp['month'] == Month]
    Production = name_merge[name_merge['month'] == Month]
    s_r = s_r[s_r['LATITUDE'] != 'unknown']
    s_r['LATITUDE'] = map(float, s_r['LATITUDE'])
    s_r['LONGITUDE'] = map(float, s_r['LONGITUDE'])
    latitude_snow= [round(float(elem), 4) for elem in s_r['LATITUDE']]
    longitude_snow = [round(float(elem), 4) for elem in s_r['LONGITUDE']]
    s_r['LATITUDE'] = latitude_snow
    s_r['LONGITUDE'] = longitude_snow
    snow_gps = zip(latitude_snow, longitude_snow)
    pts_tp = [geopy.Point(p[0], p[1]) for p in snow_gps]
    production_gps = zip(Production['latitude'], Production['longtitude'])
    onept = [ geopy.Point(coord[0],coord[1]) for coord in production_gps]
    nearest= []
    for coord in onept:
        Alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts_tp ]
        if min(Alldist, key=lambda x: (x[1]))[1] <25:
            nearest.append(min(Alldist, key=lambda x: (x[1]))[0])
        else:
            lst = [-9999,-9999]
            nearest.append(lst)
    Production['LATITUDE'] = [point[0] for point in nearest]
    Production['LONGITUDE'] = [point[1] for point in nearest]
    month_merge = pd.merge(Production, s_r, on = ['LATITUDE','LONGITUDE'], how = 'left')
    merge_sr = month_merge[['Application Number', 'Program', 'ZipCode', 'Production Period End Date',
                        'Period kWh Production', 'month_x', 'TPCP', 'TSNW']]
    return merge_sr

Month = '08/2015'
Rain_snow= Rain_snow.append(nearest(Month))



#LIST = map(nearest, name_merge['month'])
Rain_snow.to_csv('Rain_snow.csv')

df = pd.merge(Rain_snow, name_merge, on = ['Application Number','Program','ZipCode','Production Period End Date','Period kWh Production'], how = 'left')
df['Production Ratio'] = df['Period kWh Production']/df['Nameplate Rating']
df.to_csv('Rain_snow.csv')

#Merge production with temp data
def nearestTemp(Month):
    tem = temp[temp['month'] == Month]
    Production = name_merge[name_merge['month'] == Month]
    tem = tem[tem['LATITUDE'] != 'unknown']
    tem['LATITUDE'] = map(float, tem['LATITUDE'])
    tem['LONGITUDE'] = map(float, tem['LONGITUDE'])
    latitude_tem= [round(float(elem), 4) for elem in tem['LATITUDE']]
    longitude_tem = [round(float(elem), 4) for elem in tem['LONGITUDE']]
    tem['LATITUDE'] = latitude_tem
    tem['LONGITUDE'] = longitude_tem
    tem_gps = zip(latitude_tem, longitude_tem)
    pts_tp = [geopy.Point(p[0], p[1]) for p in tem_gps]
    production_gps = zip(Production['latitude'], Production['longtitude'])
    onept = [ geopy.Point(coord[0],coord[1]) for coord in production_gps]
    nearest= []
    for coord in onept:
        Alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts_tp ]
        if min(Alldist, key=lambda x: (x[1]))[1] <25:
            nearest.append(min(Alldist, key=lambda x: (x[1]))[0])
        else:
            lst = [-9999,-9999]
            nearest.append(lst)
    Production['LATITUDE'] = [point[0] for point in nearest]
    Production['LONGITUDE'] = [point[1] for point in nearest]
    month_merge = pd.merge(Production, tem, on = ['LATITUDE','LONGITUDE'], how = 'left')
    merge_tem = month_merge[['Application Number', 'Program', 'ZipCode', 'Production Period End Date',
                        'Period kWh Production', 'month_x', 'MMXT', 'MMNT','MNTM']]
    return merge_tem

Month = '08/2015'
TEMP= TEMP.append(nearestTemp(Month))
df1 = pd.merge(TEMP, name_merge, on = ['Application Number','Program','ZipCode','Production Period End Date','Period kWh Production'], how = 'left')
df1['Production Ratio'] = df1['Period kWh Production']/df1['Nameplate Rating']
df1.to_csv('TEMP.csv')
df1 = df1[['Application Number', 'Production Period End Date','month_x','MMXT', 'MMNT','MNTM']]
DF = pd.merge(df1, df, on = ['Application Number', 'Production Period End Date','month_x'], how = 'left')

#missing value
DF['MMXT'][DF['MMXT'].isnull()]
#since the data set is big enough so get rid of some missing value
DF = DF[pd.notnull(DF['MMXT'])]
DF['MMXT'] = DF['MMXT']/10
DF['MMNT'] = DF['MMNT']/10
DF['MNTM'] = DF['MNTM']/10
DF.to_csv('weatherMerge.csv')
