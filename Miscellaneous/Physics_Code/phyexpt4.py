import math
from mysql_csv_fns import *
n = [1,1,1,2,2,2,3,3,3]
N = 10**5
s = [25,30,35,25,30,35,25,30,35]
twol = [3.2,3.8,4.4,6.4,7.6,9,9.4,11.8,13.6]
l = []
tano = []
o = []
sino = []
lam = []
for i in range(9):
    l[i] = twol[i]/2
    tano[i] = l[i]/s[i]
    o[i] = math.degrees(math.atan(tano[i]))
    sino[i] = math.sin(o[i])
    lam[i] = sino[i]/(n[i]*N)
table = [n,twol,l,tano,o,sino,lam]
title = ['n','2L','L','tan O','O','sin O','Lambda']