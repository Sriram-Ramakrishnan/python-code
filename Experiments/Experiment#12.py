import csv
filename = input("Enter File Name to be created: ")
filename+=".csv"
file = open(filename,"w")
writer = csv.writer(file)
while True:
    empno= int(input("Enter EmpNo: "))
    empname = str(input("Enter Emp Name: "))
    empsal = float(input("Enter Emp Salary: "))
    writer.writerow([empno,empname,empsal])
    ans=input("Add more?(y/n): ")
    if ans == "n":
        break
file.close()
file = open(filename,"r")
read =csv.reader(file)
empno = int(input("Enter EmpNo to Search: "))
for i in read:
    if i == []:
        pass
    else:
        if i[0] == str(empno):
            print("Name: ",i[1],",Salary: ",i[2])
            break
else:
    print("EmpNo not found!")  
file.close()
    
