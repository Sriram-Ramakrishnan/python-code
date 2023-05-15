'''
Module 5: 1. Password - Strength - Strong / Weak / Fair; 
2. Transpose of Matrix 


Module 6: 1. No of vowels, cons, spl char, numeric 
2. File - ID, name, wages, total hours worked on mon, tue, 
wed, thu, fri.  Calculate weakly wages (>6 hrs per day, 
should be Over Time and it may be double wages)'''


#Mod5 Q1:


#Mod6 Q1:
import re
s = input()
sl =  s.split()
vowels = re.findall("[aeiou]",s)
consonants =  re.findall("[b-df-hj-np-tv-z]",s)
splchar = re.findall("[!@#$%^&*_]",s)
num = re.findall("[0-9]",s)
print("Number of vowels:",len(vowels))
print("Number of consonants:",len(consonants))
print("Number of special characters:",len(splchar))
print("Number of numbers:",len(num))
'''
#Mod6 Q2:
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
    
        '''
        
