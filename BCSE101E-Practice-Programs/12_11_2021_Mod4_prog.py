import time
arr_ops = ["+","-","*","/"]
n = int(input())
L = input()
a = time.time()
L = L.split()

while len(L) > 2:
    for i in range(len(L)):
        if L[i] in arr_ops:
            opsL = L[i-2:i+1]
            L.pop(i-2)
            L.pop(i-1)
            L.pop(i)
            if opsL[2] == "+":
                L[i-2]= int(opsL[0])+int(opsL[1])
            if opsL[2] == "-":
                L[i-2]= int(opsL[0])-int(opsL[1])
            if opsL[2] == "*":
                L[i-2]= int(opsL[0])*int(opsL[1])
            if opsL[2] == "/":
                L[i-2]= int(opsL[0])/int(opsL[1])
        break
    print(L)
else:
    print(L[0])
    
print(time.time()-a)
