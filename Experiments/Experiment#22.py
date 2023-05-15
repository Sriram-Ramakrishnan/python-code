import mysql.connector
import tabulate
db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = 'rootuser',db = 'exp_db')
c = db.cursor()
while True:
    print("Employee Deletion Menu:")
    empno = int(input("Emp No.to be deleted:"))
    query = "SELECT * FROM employee WHERE empno = %d"%(empno)
    c.execute(query)
    l = c.fetchall()
    s = []
    for i in l:
        s.append(i)
    if s!= []:
        print(tabulate.tabulate(s,headers=['EmpNo','EmpName','Dept','Salary'],tablefmt='psql'))
        print("Above record to be deleted?(y/n):",end = '')
        ch = input()
        if ch == 'n':
            continue
        else:
            query = "DELETE FROM employee WHERE empno = %d"%empno
            c.execute(query)
            db.commit()
    print("More Records to delete?(y/n)->",end = '')
    opt = input()
    if opt.lower() == 'n':
        break
