##Using SD County as example to merge percipitation and temp data

import pandas as pd
import geopy
import geopy.distance
import datetime
#read percipitation data
SD_tp = pd.read_csv('SD_tp.csv', header = False)

#read temp data
SD_temp = pd.read_csv('SD_temp.csv', header = False)

#read SD production data
SDproduction = Merge1[Merge1['Host Customer Physical Address County'] == 'San Diego']

#create a new variable 'month' to help mereing 
SD_tp['DATE'] = map(str,SD_tp['DATE'])
SD_tp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in SD_tp['DATE']]

#creat month for production data as well
#since production period date might ends on the first day of the month, 
#we need to make sure they are using the temp from the last month
month = []
for date in SDproduction['Production Period End Date']:
    if datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%d") == '01':
        if datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m") == '01':
            m = 12
        else:
            m = int(datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m")) - 1
        y = int(datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y"))
        new = str(m) + '/' + str(y) 
        month.append(datetime.datetime.strptime(new, "%m/%Y").strftime("%m/%Y"))
    else:
        month.append(datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y"))
        
SDproduction['month'] = month

# for merging production with percipitation and temp data, need to make sure 
# they are merging within the same month. so I subset all the data for the same month
# then find the cloest GPS point in weather data for production data, then merge

#Merge production with percipitation data
    
def nearest(Month):
    SD_snow = SD_tp[SD_tp['month'] == Month]
    Production = SDproduction[SDproduction['month'] == Month]
    SD_snow['LATITUDE'] = map(float, SD_snow['LATITUDE'])
    SD_snow['LONGITUDE'] = map(float, SD_snow['LONGITUDE'])
    sd_latitude_snow= [round(float(elem), 4) for elem in SD_snow['LATITUDE']]
    sd_longitude_snow = [round(float(elem), 4) for elem in SD_snow['LONGITUDE']]
    SD_snow['LATITUDE'] = sd_latitude_snow
    SD_snow['LONGITUDE'] = sd_longitude_snow
    sd_snow_gps = zip(sd_latitude_snow, sd_longitude_snow)
    pts_tp = [geopy.Point(p[0], p[1]) for p in sd_snow_gps]
    production_gps = zip(Production['latitude'], Production['longtitude'])
    onept = [ geopy.Point(coord[0],coord[1]) for coord in production_gps]
    nearest= []
    for coord in onept:
        Alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts_tp ]
        if min(Alldist, key=lambda x: (x[1]))[1] <25:
            nearest.append(min(Alldist, key=lambda x: (x[1]))[0])
        else:
            nearest.append(-9999)
    Production['LATITUDE'] = [point[0] for point in nearest]
    Production['LONGITUDE'] = [point[1] for point in nearest]
    month_merge = pd.merge(Production, SD_snow, on = ['LATITUDE','LONGITUDE'], how = 'left')
    merge = month_merge[['Application Number', 'Program', 'ZipCode', 'Production Period End Date', 
                        'Period kWh Production', 'month_x', 'TPCP', 'TSNW']]
    return merge
    
#Month = '03/2015'
#snow= nearest(Month)
#perp = pd.DataFrame()
lst = ['05/2007','06/2007','07/2007','08/2007','09/2007','10/2007','11/2007','12/2007']
#'09/2007', '10/2007', 
LIST = map(nearest, SDproduction['month'])
T = pd.DataFrame()
for ele in LIST:
    T = T.append(pd.DataFrame(ele))


#May_merge = May_merge[['latitude', 'longtitude','TPCP','TSNW']]
#May_prod = pd.merge(SDproduction, May_merge, on = ['latitude', 'longtitude'], how = 'left')

            nearest_SDtp.append(-9999)
            
