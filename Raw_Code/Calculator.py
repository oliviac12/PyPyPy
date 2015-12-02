import pandas as pd
import math

raw_data = {
        'lat': ['39'],
        'Ghi': ['133.3'],
        'Dhi': ['25'],
        'Tilt':['20'],
        'Month':['Apr'],
        'nameplate':['120'],
        'Quantity':['400'],
        'De_rate':['0.85']}
Input = pd.DataFrame(raw_data, columns = ['lat', 'Ghi', 'Dhi','Tilt','Month',
                                          'nameplate','Quantity','De_rate'])

raw_data1 = {'Month': ['Jan','Feb', 'Mar', 'Apr', 'May', 
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'],
            'Model_Date_Number': ['15.50', '45.13', '74.75', '105.25', '135.75', '166.25',
            '196.75','227.75', '258.25', '288.75', '319.25', '349.75']}
            

Lookup1 = pd.DataFrame(raw_data1, columns = ['Month','Model_Date_Number'])

raw_data2 = {'Module_Rating': ['80', '100', '135', '150', '175', '200',
                               '215', '225', '250', '275', '300','320'],
            'Area': ['0.7', '0.8', '1.005', '1.005', '1.15', '1.279029',
                     '1.279029', '1.6005', '1.6005', '1.9344', '1.9', '2']}
lookup2 = pd.DataFrame(raw_data2, columns = ['Module_Rating','Area'])

Result = pd.DataFrame()
#Get day number
day_number = Lookup1[Lookup1['Month']== Input['Month'][0]]
Result['day_number'] = day_number['Model_Date_Number']
# Get DHI
DHI = float(Input['Ghi'][0]) - float(Input['Dhi'][0])
Result['DHI'] = DHI
# Get DIT
def dit(DHI,lat, day_number, Tilt):
    top = DHI*math.sin(90-lat+(23.45*math.sin((day_number-81)*0.9863))+Tilt)
    bottom = math.sin(90-lat+(23.45*math.sin((day_number-81)*0.9863)))
    answer = top/bottom
    return answer
    
dit(float(Result['DHI']), float(Input['lat']), float(Result['day_number']), float(Input['Tilt']))
    

