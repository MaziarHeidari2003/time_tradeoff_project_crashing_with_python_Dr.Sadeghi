from taskdata import *
from pulp import *
import numpy as np

print('Network problem, Project time reduction')

N = 9

xindx = np.arange(1,N+1)
a = np.arange(1,N+1)
al = np.arange(N)
b = np.arange(1,N+1)
bl = np.arange(N)

rindx = [(a[i],b[j]) for j in bl for i in al]

model = LpVariable('Reducing time of project',LpMinimize)

x = LpVariable.dicts('X',xindx,0,None)
r = LpVariable.dicts('R',xindx,0,None)

model = CS[0]*r[,9]