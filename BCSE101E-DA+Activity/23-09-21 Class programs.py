'''
1) Factorial Program: f(n) = 1x2x3..n terms
2) Sum of series: S(n) =  1+2+3... n terms
3) Sum of odd numbers = 1+3+5+7...n terms
4) Sum of even numbers = 2+4+6+8..n terms
'''
'''
def f(n):       #Factorial
    i = 1
    fact = 1
    while i <= n:
        fact*=i
        i+=1
    return fact

def S(n):       #Sum of all terms
    sum = 0
    i = 1
    while i <= n:
        sum+=1
        i+=1
    return sum

def oddS(n):    
    sum = n**2
    return sum

def evenS(n,sum):
    sumodd = n**2
    sumeven = sum - sumodd
    return sumeven

i = int(input("No. of units consumed: "))
if 1 <= i <= 100:
    cost = i*2
elif 101 <= i <= 200:
    cost = 200 + (i-100)*4
elif i > 200:
    cost = 200+400+(i-200)*6
else:
    print("Enter correct data")

print("Numbers which are divisible by 7 and not divisible by 5:")
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end =";")

#27-09-2021
basic_pay = float(input("Enter the basic pay:"))
salary = basic_pay + basic_pay*0.3 + basic_pay*0.8 - basic_pay*0.12
print("Salary : %5.2f" %salary)'''









