SD_tp = pd.read_csv('SD_tp.csv', header = False)
SD_temp = pd.read_csv('SD_temp.csv', header = False)
SD_tp['DATE'] = map(str,SD_tp['DATE'])
SD_tp['month'] = [datetime.datetime.strptime(date, "%Y%m%d").strftime("%m/%Y") for date in SD_tp['DATE']]
SDproduction = Merge1[Merge1['Host Customer Physical Address County'] == 'San Diego']

SDproduction['month'] = [datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%m/%Y") for date in SDproduction['Production Period End Date']]

def nearest(month):
    SD_snow = SD_tp[SD_tp['month'] == month]
    Production = SDproduction[SDproduction['month'] == month]
    SD_snow['LATITUDE'] = map(float, SD_snow['LATITUDE'])
    SD_snow['LONGITUDE'] = map(float, SD_snow['LONGITUDE'])
    sd_latitude_snow= [round(float(elem), 4) for elem in SD_snow['LATITUDE']]
    sd_longitude_snow = [round(float(elem), 4) for elem in SD_snow['LONGITUDE']]
    sd_snow_gps = zip(sd_latitude_snow, sd_longitude_snow)
    pts_tp = [geopy.Point(p[0], p[1]) for p in sd_snow_gps]
    production_gps = zip(Production['latitude'], Production['longtitude'])
    onept = [ geopy.Point(coord[0],coord[1]) for coord in production_gps]
    nearest= []
    for coord in onept:
        Alldist = [(p, geopy.distance.distance(p, coord).km) for p in pts_tp ]
        if min(Maydist, key=lambda x: (x[1]))[1] <25:
            nearest.append(min(Alldist, key=lambda x: (x[1]))[0])
    Production['LATITUDE'] = [point[0] for point in nearest]
    Production['LONGITUDE'] = [point[1] for point in nearest]
    month_merge = pd.merge(Production, SD_snow, on = ['LATITUDE','LONGITUDE'], how = 'left')
    return month_merge
    
#May_Near = pd.DataFrame(May_gps)
#May_Near.columns = ['latitude','longtitude']

month = '08/2013'
snow= nearest(month)


#May_merge = May_merge[['latitude', 'longtitude','TPCP','TSNW']]
#May_prod = pd.merge(SDproduction, May_merge, on = ['latitude', 'longtitude'], how = 'left')

            nearest_SDtp.append(-9999)