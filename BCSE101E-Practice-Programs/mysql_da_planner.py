from mysql_csv_fns import *
Columnnames = ["S.No.","Subject","Activity","DeadLine"]
work = 1
data = []
while True:
    print()
    print("Homework #",work)
    print()
    list_row = [work]
    sub = input("%s :"%Columnnames[1])
    act = input("%s :"%Columnnames[2])
    dln = input("%s :"%Columnnames[3])
    if sub.lower() == "nop":
        break
    else:
        list_row.append(sub)
        list_row.append(act)
        list_row.append(dln)
        data.append(list_row)
        work+=1

MySQL_display(data,Columnnames)
    
