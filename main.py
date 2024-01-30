from task import *
import pandas as pd
import numpy as np


mydata = pd.read_excel(io='activities.xlsx', sheet_name='Sheet1')

ntask = mydata.shape[0]

mydata = computeCPM(mydata)
mydata['DAYS'][0] = 5
printTask(mydata)

ntask = mydata.shape[0]

cp = []
for i in range(ntask):
  if(mydata['CRITICAL'][i] == 'YES'):
    cp.append(mydata['CODE'][i])

print('The critical path is: ' + '-'.join(cp))

tdur = mydata['DAYS'][0]
for i in range(ntask):
  if i==0:
    continue
  if mydata['CRITICAL'][i] == 'YES':
    tdur = tdur + mydata['DAYS'][i]
    

print('Total project duration is ' + str(tdur) + ' unit time')    

