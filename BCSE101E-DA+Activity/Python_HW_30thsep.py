'''
#Program#1:Average runs scored by a batsman
run1 = int(input("Enter your 1st score :"))
run2 = int(input("Enter your 2nd score :"))
run3 = int(input("Enter your 3rd score :"))
run4 = int(input("Enter your 4th score :"))
total_runs = run1+run2+run3+run4
avg_runs = total_runs/4
print("Your average score is ",avg_runs)

#Program#2:Area of circle
import math
radius = float(input("Enter the radius of the circle :"))
area = math.pi*radius**2
print("Area of the circle is %5.2f"% area)

#Program#3:University lab setting:
chairs = int(input("No. of chairs required:"))
tables = int(input("No. of tables required:"))
cost_of_chair = float(input("Cost of a chair:"))
cost_of_table = float(input("Cost of a table:"))
computers = int(input("No. of computers required:"))
cost_of_computer = float(input("Cost of a computer:"))
labour_cost = float(input("Cost of labour per hour:"))
hours = int(input("No. of hours worked:"))
totalcost = chairs*cost_of_chair + tables*cost_of_table + computers*cost_of_computer + labour_cost*hours
print("The total cost for setting the lab is",totalcost)

#Program#4:Browser problem
hours = int(input("Enter the no. of hours spent:"))
minutes = int(input("Enter the no. of minutes spent:"))
if hours >= 7:
    print("Invalid input")
else:
    if hours >=5:
        cost = 200 + (hours-5)*50 + minutes*1
    else:
        cost = hours*50 + minutes*1
print("Bill for Internet Browsing = Rs.",cost)

#Program#5:Scholarship Eligiblity
first_g = input("Are you the first graduate of your family:[Y/N]")
maths = float(input("Enter the maths mark:"))
physics = float(input("Enter the physics mark:"))
chemistry = float(input("Enter the chemistry mark:"))
avg = (maths + chemistry + physics)/3
if avg >= 98.0 and first_g.lower() == "y":
    print("Congratulations,you are eligible for the scholarship")
else:
    print("Sorry you are not eligible for the scholarship")

#Program#6:Roots of a quadratic equation
import math
a = int(input("Enter the value of the coefficient of x^2:"))
b = int(input("Enter the value of the coefficient of x:"))
c = int(input("Enter the value of the constant:"))
x1 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b-math.sqrt(b**2 - 4*a*c))/(2*a)
print("The roots of the quadratic equation ",a,"x^2 +",b,"x +",c,"are",x1,"and",x2)

#Program#7:Leap year check
year = int(input("Enter the year:"))
if year %4 == 0:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
'''
#Program#8:Segregate based on their CGPA:
cgpa = float(input("Enter the CGPA of the student:"))
if 9 <= cgpa <= 10:
    print("Outstanding CGPA.")
elif 8 <= cgpa < 9:
    print("Excellent CGPA.")
elif 7 <= cgpa < 8:
    print("Good CGPA.")
elif 6 <= cgpa < 7:
    print("Average CGPA.")
elif 5 <= cgpa < 6:
    print("Better CGPA.")
else:
    print("Poor CGPA.")

