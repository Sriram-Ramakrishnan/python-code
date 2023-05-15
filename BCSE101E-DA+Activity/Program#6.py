#Program#6:Roots of a quadratic equation
import math
a = int(input("Enter the value of the coefficient of x^2:"))
b = int(input("Enter the value of the coefficient of x:"))
c = int(input("Enter the value of the constant:"))
root1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
root2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
print("The roots of the quadratic equation ",root1,"and",root2)
