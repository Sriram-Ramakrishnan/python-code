def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)

def y(x):
    sum = 0
    for i in range(1,x+1):
        sum+=(i/fact(i))
    return sum

x = int(input("Enter number"))
print(fact(x),y(x))


a = 'Student name  father name  mother name  phoneno  reg no'
b = 'mark1  mark2  mark3'

def basic():
    l = []
    for i in a.split("  "):
        string = "Enter "+i+":"
        x = input(string)
        l.append(x)
    return l

def sem():
    L = []
    for j in b.split("  "):
        string = "Enter"+j+":"
        x = float(input(string))
        L.append(x)
    total = sum(L)
    avg  = total/3
    L.append(total)
    L.append(avg)
    return L

print(basic())
print(sem())
        
