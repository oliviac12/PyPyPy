F = pd.read_csv('Manufacturers.csv', header = False)
Manu = pd.read_csv('Manu.csv',header = False)
add_f = pd.merge(Manu, F, on = ['Manufacturer'], how = 'left')
add_f['Failure_Rate'][add_f['Failure_Rate'].isnull()]
add_f = add_f[pd.notnull(add_f['Failure_Rate'])]
DF = pd.read_csv('weatherMerge.csv', header = False)
DFF = pd.merge(DF, add_f, on = ['Application Number'], how = 'left')
DFF['TST'] = DFF['TPCP']/10 - DFF['TSNW']/10
DFF = DFF.drop('TPCP', axis=1)
DFF = DFF.drop('Host Customer Physical Address City', axis = 1)
DFF = DFF.drop('Host Customer Physical Address County', axis = 1)
DFF.to_csv('DFF.csv')


#find out tankSolar
raw = pd.read_csv('MeasuredProduction.csv', header = False)
merge_manu = pd.merge(add_f, raw, on = ['Application Number'], how = 'left')
tankproduction = merge_manu[merge_manu['Manufacturer'] == 'TenKsolar']
tank = add_f[add_f['Manufacturer'] == 'TenKsolar']

