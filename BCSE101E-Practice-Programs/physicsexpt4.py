import math
from mysql_csv_fns import *
n = ['',1,'','',2,'','',3,'']
N = 10**5
s = [25,30,35,25,30,35,25,30,35]
twol = [3.2,3.8,4.4,6.4,7.6,9,9.4,11.8,13.6]
l = [0,0,0,0,0,0,0,0,0]
tano = [0,0,0,0,0,0,0,0,0]
o = [0,0,0,0,0,0,0,0,0]
sino = [0,0,0,0,0,0,0,0,0]
lam = [0,0,0,0,0,0,0,0,0]
sinoavg = ['','','','','','','','','']
for i in range(9):
    l[i] = round(twol[i]/2,4)
    tano[i] = round(l[i]/s[i],4)
    o[i] = round(math.degrees(math.atan(tano[i])),4)
    sino[i] = round(math.sin(math.radians(o[i])),4)
    if i in [2,5,8]:
        sinoavg[i-1] = round(sum(sino[i-2:i+1])/3,4)
        lam[i-1] = round((sinoavg[i-1]/(n[i-1]*N))*10**9,4)
table = [n,s,twol,l,tano,o,sino,sinoavg,lam]
title = ['n','s','2L','L','tan θ','θ','sin θ','Mean',"λ"]
table = rev_table(table)
MySQL_display(table,title)
