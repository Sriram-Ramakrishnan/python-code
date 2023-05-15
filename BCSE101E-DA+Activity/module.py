import math
def quadratic_roots(a,b,c):
    discriminant = math.pow(b,2) - 4*a*c
    print("Discriminant = ",discriminant)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant))/2*a
        root2 = (-b - math.sqrt(discriminant))/2*a
        print("Solution: ", root1,",",root2)
    elif discriminant == 0:
        root1 = -b/(2*a)
        root2 = -b/(2*a)
        print("Solution: ", root1,",",root2)

    else:
        print("No Solution")
        

