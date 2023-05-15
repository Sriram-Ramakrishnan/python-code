import math
L = 13.5
sino = [0,0,0,0,0,0]
V = [4.0,4.5,5.0,4.0,4.5,5.0]
r1 = [2.3,2.4,2.2,4.2,4,3.6]
r2 = [2.7,2.6,2.5,5.1,4.2,4.0]
D = []
for i in range(6):
    r = (r1[i]+r2[i])/2
    R = round(r/2,3)
    sino[i] = round((1/math.sqrt(1+(L/R)**2)),3)
    lmb = round(12.3/math.sqrt(V[i]*1000),3)
    d = round(lmb/sino[i],3)
    D.append(d)
    print(r,R,lmb,sino[i],d)
print(round(sum(D[:3])/3,3))
print(round(sum(D[3:])/3,3))
