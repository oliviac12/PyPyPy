
def Convert_mon(data):
    Data = pd.DataFrame(data, columns = ['Date', 'Time', 'GHI', 'X', 'DNI', 'Y', 'DHI','z'])
    #Data['date'] = Data['Date'][0] + Data['Date'][3:]
    Data['Date'] = [datetime.datetime.strptime(date, "%m/%d/%Y" ).strftime("%m/%Y") for date in Data['Date']]
    Data['GHI'] = map(int, Data['GHI'])
    Data['DNI'] = map(int, Data['DNI'])
    Data['DHI'] = map(int, Data['DHI'])
    GHI = list(Data.groupby(by=['Date'])['GHI'].sum()/1000)
    DNI = list(Data.groupby(by=['Date'])['DNI'].sum()/1000)
    DHI = list(Data.groupby(by=['Date'])['DHI'].sum()/1000)
    unique_Date = list(set(Data['Date']))
    unique_Dtae = unique_Date.sort()
    lat = list(itertools.repeat(gps[0], 12))
    log = list(itertools.repeat(gps[1], 12))
    Monthly = pd.DataFrame({'lat' : lat, 'log' : log, 'GHI': GHI, 'DNI': DNI, 'DHI': DHI, 'Date':unique_Date})
    #monthly = monthly.append(Monthly)
    return Monthly

    #Monthly.to_csv('Monthly' + str(ele) + '.csv') 
Date = datetime.date.today()
Date
Date.datetime.date()
