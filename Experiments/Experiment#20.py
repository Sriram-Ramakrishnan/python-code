import mysql.connector
import tabulate
db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = 'rootuser',db = 'exp_db')
c = db.cursor()
while True:
    print("Employee Details Search Bar:")
    empno = int(input("Emp No. ->"))
    query = "SELECT * FROM employee WHERE empno = %d"%(empno)
    c.execute(query)
    l = c.fetchall()
    print("Record:")
    s = []
    for i in l:
        s.append(i)
    print(tabulate.tabulate(s,headers=['EmpNo','EmpName','Dept','Salary'],tablefmt='psql'))
    print("More Records to search?(y/n)->",end = '')
    opt = input()
    if opt.lower() == 'n':
        break

a = f"INSERT INTO EMPLOYEE VALUES ('{}'

