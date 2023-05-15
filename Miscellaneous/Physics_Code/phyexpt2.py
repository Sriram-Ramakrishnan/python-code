import math
import matplotlib.pyplot as plt
'''
tc = []
for i in range(5):
    l = []
    
    tc.append(l)
e = math.e
h = 6.626*10**(-34)
print(h)

v = 3*10**8
freq = (v/635)*10**(-5)
print(freq)
'''
freq = [4.72,5.13,5.56,6.00,6.50]
volt = [0.34,0.50,0.66,0.84,1.07]

i = 2
slope = (volt[i+1]-volt[i])/(freq[i+1]-freq[i])
print("dy = ",(volt[i+1]-volt[i]))
print(freq[i+1]-freq[i])
print(slope)
h = round(slope,2)*10**(-14)*(1.6*10**(-19))
print(h)
plt.plot(freq,volt,marker = 'o')
plt.title("")
plt.xlabel("Incident photon frequency")
plt.ylabel("Stopping voltage")
plt.show()
