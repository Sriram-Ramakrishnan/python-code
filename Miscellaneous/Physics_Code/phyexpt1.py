import matplotlib.pyplot as plt
import math
from mysql_csv_fns import *
'''
m =[500,600,700,800,900]
L = [24,26,28,30,31]
rts = []
u = 2.3/1000
F = 0
for i in range(5):
    print(i+1,") m = %f Kg, L = %f m"%(m[i]/1000,L[i]/100))
    T = (m[i]/1000)*9.8
    T = round(T,2)
    rts.append(T**0.5)
    L[i] = L[i]/100
    print("Tension =",T,"N")
    f = (1/(2*L[i]))*((T/u)**0.5)
    f = round(f,3)
    print("Frequency = ",f,"Hz")
    F+=f
    print()
print("Average value of frequency = ",round(F/5,2),"Hz")

for i in range(4):
    slope = (rts[i+1]-rts[i])/(L[i+1]-L[i])
    fr = slope/(2*math.sqrt(u))
    print("Slope = %.4f, Freq = %.4f Hz"%(slope,fr))
'''
A = [12.25,12.05,11.85,11.65,11.45,11.25,11.05,10.85,10.65,10.45,10.25,10.05]
B = [0.1,0.3,2.8,10.2,41.4,81.2,104.5,55.4,31.3,12.25,5.5,0.1]
l = rev_table([A,B])
print(l)
plt.plot(A,B)
plt.title("")
plt.xlabel("Micrometer(in m)")
plt.ylabel("Current(mA)")
plt.show()



    