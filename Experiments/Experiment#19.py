import mysql.connector
import tabulate
db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = 'rootuser',db = 'exp_db')
c = db.cursor()
c.execute("CREATE TABLE employee (empno INT,name VARCHAR(20),dept VARCHAR(20),salary INT)")
db.commit()
while True:
    print("Employee Details:\n1.Add Record\n2.Display Record\nPress 0 for exit")
    opt = int(input("  ->"))
    if opt == 0:
        break
    elif opt == 1:
        empno = int(input("Emp No:"))
        name = str(input("Name :"))
        dept = str(input("Department:"))
        sal = int(input("Salary:"))
        content = (empno,name,dept,sal)
        query = "INSERT INTO employee VALUES %s"%(content,)
        c.execute(query)
        db.commit()
        print("Data added successfully.")
    elif opt == 2:
        query = "SELECT * FROM employee"
        c.execute(query)
        l = c.fetchall()
        print("Data:")
        s = []
        for i in l:
            s.append(i)
        print(tabulate.tabulate(s,headers=['EmpNo','EmpName','Dept','Salary'],tablefmt='psql'))
    else:
        print("Enter correct option")

