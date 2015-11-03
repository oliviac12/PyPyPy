###### Add tilt
T = pd.read_csv('Tilt.csv', header = False)
DTT = pd.read_csv('DFF.csv', header = False)
f_DTT = pd.merge(DTT, T, on = ['Application Number'], how = 'left')

f_DFF = pd.read_csv('f_DFF.csv', header = False)
f_DFF['TPCP'] = f_DFF['TPCP']/100
f_DFF['TSNW'] = f_DFF['TSNW']/10
f_DFF.to_csv('f_DFF.csv')