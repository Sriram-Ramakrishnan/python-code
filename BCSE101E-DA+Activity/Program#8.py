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
