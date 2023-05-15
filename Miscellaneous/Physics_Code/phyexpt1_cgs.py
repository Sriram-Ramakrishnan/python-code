import matplotlib.pyplot as plt
import math
m =[500,700,900,1100,1300]
L = [29,33,34,36.3,38.8]
rts = []
u = 2.3/100
F = 0
for i in range(5):
    print(str(i+1)+") Mass = %f g,\n Resonating Length = %f cm"%(m[i],L[i]))
    T = (m[i])*980
    rts.append(T**0.5)
    print("Tension =",T,"dyne")
    f = (1/(2*L[i]))*((T/u)**0.5)
    print("Frequency = ",f,"Hz")
    F+=f
    print()
print("Average value of frequency = ",(F/5),"Hz")

for i in range(4):
    slope = (rts[i+1]-rts[i])/(L[i+1]-L[i])
    fr = slope/(2*math.sqrt(u))
    print("Slope = %.4f, Freq = %.4f Hz"%(slope,fr))
    
plt.plot(L,rts)
plt.title("")
plt.xlabel("Resonating Length (in cm)")
plt.ylabel("√(tension) in √dyne")
plt.show()
