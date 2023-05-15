import mysql.connector
import tabulate
db = mysql.connector.connect(host = 'localhost',user = 'root',passwd = 'rootuser',db = 'exp_db')
c = db.cursor()
l=['empno','name','dept','salary']
while True:
    print("Employee Details Updating Menu:")
    empno = int(input("Emp No.to be updated:"))
    field = input("Field :")
    if field.lower() not in l:
        print("Field doesnt exist.Retry.")
        continue
    value = input("Value :")
    query = f"UPDATE employee SET {field} = '{value}' WHERE empno = {empno}"
    c.execute(query)
    db.commit()
    print("Updated Records")
    print("More Records to update?(y/n)->",end = '')
    opt = input()
    if opt.lower() == 'n':
        break
