file = open("File1.txt",'r')
for i in file:
    ids,name,m,t,w,th,f,wage=i.split()
    l = [float(m),float(t),float(w),float(th),float(f)]
    sum_wage = 0
    for j in l:
        if j >= 6.0:
            sum_wage += float(wage)*(2*(j-6)+6)
        else:
            sum_wage+= float(wage)*j
    print("ID:",ids,"\nName:",name,"\nTotal wage:",sum_wage)
    
        
        
