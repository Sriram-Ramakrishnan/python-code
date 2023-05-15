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
