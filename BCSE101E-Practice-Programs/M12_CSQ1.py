'''
days = int(input())
if days < 0:
    print("Enter a positive number")
else:
    print(days*24*60*60)
'''
while True:
    r = int(input("R:"))
    g = int(input("G:"))
    b = int(input("B:"))
    x = r/g
    print("R/G = ",round(x,3))
    x = g/b
    print("G/B = ",round(x,3))
    x = r/b
    print("R/B = ",round(x,3))
