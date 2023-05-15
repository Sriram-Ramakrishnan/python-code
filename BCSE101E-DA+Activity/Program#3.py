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
