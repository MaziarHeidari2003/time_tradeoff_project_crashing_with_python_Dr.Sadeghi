import pandas as pd
df = pd.read_csv('data.csv')
CS =  []
dshape = df.shape[0]
for i in range(dshape):
  cost = (df['CC'][i] - df['NC'][i])/(df['ND'][i] - df['CD'][i])
  CS.append(cost)

MCD = []
for i in range(dshape):
  ctime = df['ND'][i] - df['CD'][i]
  MCD.append(ctime)


TNC = df['NC'].sum()    
