#Modules Used for Program:

import mysql.connector
import datetime

'======================================================================================================================='
#MySQL Interface:
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_command(str):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = "mydb")
    mycursor = mydb.cursor()
    not_commit_list = ['SHOW','DESC']
    if str[:4].upper() in not_commit_list:
        execute = mycursor.execute(str)
        my_data = mycursor.fetchall()
        MySQL_display(my_data)
    
    else:
        execute = mycursor.execute(str)
        mydb.commit()
        if str[:6] == "SELECT":
            my_data = mycursor.fetchall()
            MySQL_display(my_data)

        elif str[:6] == "INSERT": 
            print(mycursor.rowcount,"row(s) affected")

        else:
            pass
'-----------------------------------------------------------------------------------------------------------------------'
def type_converter(value):
    return str(value)
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_create(database):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    table_name = str(input("Enter the Name of the table:"))
    amt_titles = int(input("Enter the Number of Titles you require for the table:"))
    title_list = []
    
    for i in range(1,amt_titles+1):
        print("Entry # %d" %i)
        name_column = str(input("Enter Name of the Column's Title : "))
        var_type = str(input("Enter Variable type : "))
        var_len = str(input("Enter length of the data type : "))
        constraint_1= str(input("Enter Constraints(if any) : "))

        if var_len == '':
            c_details = (name_column+' '+var_type +' '+constraint_1+',')

        else:
            var_len = int(var_len)
            c_details = (name_column+' '+var_type+"(%d)"+' '+constraint_1+',') %var_len
        title_list.append(c_details)

    my_snip= ''
    
    for j in title_list:
        my_snip+=j
        
    table_dets = "CREATE TABLE "+table_name+" ("+(my_snip[:len(my_snip)-1])+")"
    print(table_dets)
    return table_dets
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_insert(table_name,database):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_data = mycursor.fetchall()
    my_snippet = "INSERT INTO "+table_name+" VALUES %s"
    my_title,my_values = {},[]
    for i in my_data:
        for j in range(len(my_data)):
            title = i[0]
            title_type = i[1]
            my_title[title] = title_type
            break
        
    for j in my_title.keys():
        print("Enter "+j,end = ' ')
        if my_title[title][:4].lower == "char":
            title_data = str(input(' : '))
        elif my_title[title][:3].lower == "int":
            title_data = int(input(' : '))
        elif my_title[title][:5].lower == "float":
            title_data = float(input(' : '))
        else:
            title_data = str(input(' : '))
        my_values.append(title_data)
    my_values= tuple(my_values)     # Base tuple
    my_code = (my_snippet %(my_values,))
    print(my_code)
    return my_code
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_update(table_name,database):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_data = mycursor.fetchall()
    my_title,my_values = {},[]
    for i in my_data:
        for j in range(len(my_data)):
            title = i[0]
            title_type = i[1]
            my_title[title] = title_type
            break


    update_row = str(input("Enter the column to be modified:"))
    while True:
        if update_row in my_title.keys():
            if my_title[update_row][:4].lower == "char":
                modify_val = str(input("Enter %s to be updated:"%update_row))
                break

            elif my_title[update_row][:3].lower == "int":
                modify_val = int(input("Enter %s to be updated:"%update_row))
                break

            elif my_title[update_row][:5].lower == "float":
                modify_val = float(input("Enter %s to be updated:"%update_row))
                break

            else:
                modify_val = str(input("Enter %s to be updated:"%update_row))
                break

        else:
            print("Column doesn't exist,Try again")
            update_row = str(input("Enter the column to be modified:"))

    condition_row =str(input("Enter the Specifications/Condition Column:"))

    while True:
        if condition_row in my_title.keys():
            if my_title[condition_row][:4].lower == "char":
                condition_val = str(input("Enter the Specification %s's Value:"%condition_row))

            elif my_title[condition_row][:3].lower == "int":
                condition_val = int(input("Enter the Specification %s's Value:"%condition_row))

            elif my_title[condition_row][:5].lower == "float":
                condition_val = float(input("Enter the Specification %s's Value:"%condition_row))

            else:
                condition_val = str(input("Enter the Specification %s's Value:"%condition_row))

        else:
            print("Column doesn't exist,Try again")
            condition_row = str(input("Enter the Specifications/Condition Column:"))

    cmd_1 = "UPDATE " + table_name + " SET " + update_row
    cmd_2 = "WHERE " + condition_row
    
    
    if type(modify_val) == int:
        val_1 = (" = %d " %modify_val)
        if type(condition_val) == str:
            val_2 = (" = '%s' "%condition_val)

        elif type(condition_val) == int:
            val_2 = (" = %d "%condition_val)

        elif type(condition_val) == float:
            val_2 = (" = %f "%condition_val)

        else:
            val_2 = (" = '%s' "%condition_val)

    elif type(modify_val) == str:
        val_1 = (" = '%s' " %modify_val)
        if type(condition_val) == str:
            val_2 = (" = '%s' "%condition_val)

        elif type(condition_val) == int:
            val_2 = (" = %d "%condition_val)

        elif type(condition_val) == float:
            val_2 = (" = %f "%condition_val)

        else:
            val_2 = (" = '%s' "%condition_val)

    
    elif type(modify_val) == float:
        val_1 = (" = %f " %modify_val)
        if type(condition_val) == str:
            val_2 = (" = '%s' "%condition_val)

        elif type(condition_val) == int:
            val_2 = (" = %d "%condition_val)

        elif type(condition_val) == float:
            val_2 = (" = %f "%condition_val)

        else:
            val_2 = (" = '%s' "%condition_val)

    statement = (cmd_1+val_1+cmd_2+val_2)
    return statement
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_display(data,col_names):
    data_list = []
    data_dict = []
    k = 1
    for col in range(len(data[0])):                    #len(data) will be no of rows; len(data[0]) will be no of columns.
        for i in data:                                 # i will be a single row
            column = i[col]
            column1 = type_converter(column)           #Converts any datatype to str for printing
            data_list.append(column1)
        data_dict.append(data_list)                    #Column wise data transformation
        k+=1
        data_list = []
        
    str_data = []
    len_list2 = []
    
    e = 0
    

    for i in data_dict:                                # i is a single column's data
        len_list,str_list = [],[]
        
        for j in i:
            len_list.append(len(j))                    # length of each data is added 
            
        max_len = max(len_list)                        # maximum is taken for equal and neat spacing
        index = len_list.index(max_len)                # index of a word length and the word is same.
        long_word = i[index]                           # the longest word
        len_topic = len(col_names[e])                  # table header's length is taken
        if max_len < len_topic:                        # longest word in the column vs the length of the header
            max_len = len_topic
        e+=1
        len_list2.append(max_len)                      # Overall length of a column
        
        for j in i:
            space_len = max_len - len(j)               # Amount of white spaces required
            str_space = "| "+j+((space_len)*" "+" ")
            str_list.append(str_space)
            
        str_data.append(str_list)
        
    data_list = []
    data_dict = []
    q = 1
    
    for row in range(len(str_data[0])):
        for i in str_data:
            row_data = i[row]
            data_list.append(row_data)
            
        data_dict.append(data_list)
        q+=1
        data_list = []
       
    header = "+"
    title = ""

    for i in len_list2:
        line = (i*"-")+"--+"
        header+=line
        for j in col_names:
            space_len = i - len(j)
            str_space = "| "+j+((space_len)*" "+" ")
            title+=str_space
            col_names.remove(j)
            break

    print(header[:-1]+"+")
    print(title+"|")
    print(header[:-1]+"+")

    for i in data_dict:
        table_format = ""
        
        for j in i:
            table_format+=j
        print(table_format+"|")
    
    print(header[:-1]+"+")
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_basic_display(data,colnames):
    for i in range(len(data)):
        print(i+1,")",end = '')
        for j in range(len(data[i])):
            print(colnames[j] + " : "+ data[i][j])
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_select(table_name,database,v_no):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_datas = mycursor.fetchall()
    mydb.commit()
    my_title,my_values = [],[]

    for i in my_datas:

        for j in range(len(my_datas)):
            title = i[0]
            my_title.append(title)
            break

    mycursor.execute("SELECT * FROM "+table_name)
    my_data = mycursor.fetchall()
    mydb.commit()
    print("")
    if v_no == 1:
        MySQL_display(my_data,my_title)

    elif v_no == 2:
        MySQL_basic_display(my_data,my_title)
    return "SELECT * FROM "+table_name
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_transfer(database1,database2):
    file = open(database1+".txt","r")
    file2 = open(database2+".txt",'a')
    queries = file.readlines()
    file2.writelines(queries)
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "rootuser",db = database2)
    cursor = mydb.cursor()
    for i in queries:
        if i[:6] in ["INSERT","CREATE","UPDATE","ALTER "]:
            cursor.execute(i)
            mydb.commit()
            j = cursor.rowcount
        else:
            pass
    print(j,"data rows transferred successfully.")
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_storage(query,database):
    dbfile = str(str(database)+".txt")
    file = open(dbfile,"a")
    nquery = str(query) + "\n"
    file.write(nquery)
'-----------------------------------------------------------------------------------------------------------------------'
def data_processor(table_name,database):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_datas = mycursor.fetchall()
    mydb.commit()
    my_title,my_values = [],[]

    for i in my_datas:

        for j in range(len(my_datas)):
            title = i[0]
            my_title.append(title)
            break

    mycursor.execute("SELECT * FROM "+table_name)
    my_data = mycursor.fetchall()
    mydb.commit()
    return my_values,my_title
'-----------------------------------------------------------------------------------------------------------------------'
def bar_graph(x_vals,y_vals,x_title,y_title,title):
    import matplotlib.pyplot as pyplot ; pyplot.rcdefaults()
    import numpy as np

    num_bars = np.arange(len(x_vals))
    bar_type = int(input("Enter The Type of Bar graph you would like below\n1] Normal \n2] Horizontal \n Enter the Option Below: "))
    
    if bar_type == 1:
        p.bar(num_bars,y_vals,align = "center",alpha = 0.5)
        p.xticks(num_bars,x_vals)
        p.xlabel(x_title)
        p.ylabel(y_title)
        p.title(title)
        p.show()

    elif bar_type == 2:
        p.barh(num_bars,y_vals,align = "center",alpha = 0.5)
        p.yticks(num_bars,x_vals)
        p.xlabel(y_title)
        p.ylabel(x_title)
        p.title(title)
        p.show()
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_alter(table_name,database):
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_datas = mycursor.fetchall()
    mydb.commit()
    print("Enter Specific action you require:\n 1) Add a column\n 2) Modify a Column\n 3) Rename a column\n 4) Drop a Column\nOperation Number",end = ' ')
    alter = int(input(""))
    startup_query = "ALTER TABLE " + table_name
    if alter == 1:
        c_details = ''
        amt_titles = int(input("Enter the number of columns you would like to add : "))
        for i in range(1,amt_titles+1):
            print("Entry # %d" %i)
            colname = str(input("Enter name of the column to be added :"))
            coltype = str(input("Enter type of the column :"))
            collen = str(input("Enter length of the column :"))
            colspec1 = str(input("Enter any specifications required : "))

            if collen == '':
                c_data = (colname+' '+coltype +' '+colspec1+',')

            else:
                collen = int(collen)
                c_data = (colname+' '+coltype+"(%d)"+' '+colspec1+',') %collen
                c_details += c_data

        MySQL_Query = 'ADD (' + c_details + ')'
        return startup_query + MySQL_Query 
             
    elif alter == 2:
        colname = str(input("Enter name of the column to be modified :"))
        print("Specify Modifications : ")
        coltype = str(input("Enter type of the column :"))
        collen = str(input("Enter length of the column :"))
        colspec1 = str(input("Enter any specifications required : "))

        if collen == '':
            c_details = (colname+' '+coltype +' '+colspec1+' ')

        else:
            collen = int(collen)
            c_details = (colname+' '+coltype+"(%d)"+' '+colspec1+' ') %collen 
        MySQL_Query = 'MODIFY ' + c_details
        return startup_query + MySQL_Query

    elif alter == 3:
        colname = str(input("Enter new name of the table :"))
        MySQL_Query = 'RENAME TO '+ colname
        return startup_query + MySQL_Query  

    elif alter == 4:
        colname = str(input("Enter name of the column to be deleted :"))
        MySQL_Query = 'DROP COLUMN ' + colname
        return startup_query + MySQL_Query
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_database():
    db = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser")
    dbcursor = db.cursor()
    dbcursor.execute("SHOW DATABASES")
    dboptions = dbcursor.fetchall()
    MySQL_display(dboptions,["Available Databases : "])
    database = str(input("Enter the database : "))
    for i in range(len(dboptions)):
        for j in dboptions[i]:
            if database == j :
                return database
                break
    else:
        print("Database not found...")
        MySQL_database()
    print("-----------------------------------------------------------------------------------------------------------------------")
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL_Ops(database):
    print("=======================================================================================================================")
    print("Current Database : ",database)
    mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "rootuser",db = database)
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    mytables = mycursor.fetchall()
    if mytables == []:
        print("Tables yet to be created")
    else:
        MySQL_display(mytables,["Available Tables : "])
    print("\n\tOperations available : ")
    print("""\t1. Create a New Table.\n\t2. Insert a row into an existing Table.\n\t3. Update values of an existing Table
    \t4. Display the results of a table\n\t5. Change the database\n\t6. Transfer data to another database\n\t7. Alter the structure/details of the table\n\t8. Exit the interface""")
    print("Enter the respective Operation Number for execution : ",end = '')
    Ops_No = int(input(""))
    if Ops_No == 1:
        MySQL_Query = MySQL_create(database)
        MySQL_storage(MySQL_Query,database)
        mycursor.execute(MySQL_Query)
        mydb.commit()
        print("Table Created Successfully.\n")
        print("-----------------------------------------------------------------------------")
        MySQL_Ops(database)

    elif Ops_No == 2:
        table_name = str(input("Enter Name of the Table where you want to insert an entry:"))
        i = 1
        while True:
            print("Row Entry #",i)
            MySQL_Query = MySQL_insert(table_name,database)
            MySQL_storage(MySQL_Query,database)
            mycursor.execute(MySQL_Query)
            mydb.commit()
            print("Row Entry Added Successfully.\n")
            print("-----------------------------------------------------------------------------")
            q = input("Would you like to insert another entry?(yes/no):")
            print("-----------------------------------------------------------------------------")
            i+=1
            if q.lower() == 'no':
                break

        MySQL_Ops(database)
            
    elif Ops_No == 3:
        table_name = str(input("Enter Name of the Table where you want to Update a row entry:"))
        MySQL_Query = MySQL_update(table_name,database)
        MySQL_storage(MySQL_Query,database)
        mycursor.execute(MySQL_Query)
        mydb.commit()
        print("Row Entry Updated Successfully.\n")
        print("-----------------------------------------------------------------------------")
        MySQL_Ops(database)

    elif Ops_No == 4:
        table_name = str(input("Enter Name of the Table where you want to view its contents : "))
        print("Formats of viewing:\n\t 1)Tabular format 2) Line by line format")
        v_no = int(input("Enter the format of printing you would like to see : "))
        print("Table name : \t",table_name)
        MySQL_Query = MySQL_select(table_name,database,v_no)
        MySQL_storage(MySQL_Query,database)
        MySQL_Ops(database)

    elif Ops_No == 5:
        db =  MySQL_database()
        print("Database changed from",database,"to",db,".\n")
        print("-----------------------------------------------------------------------------")
        MySQL_Ops(db)

    elif Ops_No == 6:
        db = str(input("Enter the Database Name to transfer the current database's data : "))
        MySQL_transfer(database,db)
        print("-----------------------------------------------------------------------------")
        MySQL_Ops(database)

    elif Ops_No == 7:
        table_name = str(input("Enter the name of the table to be altered :"))
        MySQL_Query = MySQL_alter(table_name,database)
        MySQL_storage(MySQL_Query,database)
        print("Table altered successfully.")
        print("-----------------------------------------------------------------------------")

        MySQL_Ops(database)

    elif Ops_No == 8:
        print("Interface logged out successfully.")
    
    else:
        print("\tOperation does not exist.\t\n Retry.\n")
        MySQL_Ops(database)
'-----------------------------------------------------------------------------------------------------------------------'
def MySQL():
    print("Running MySQL Python Interface...\n Successfully connected.")
    MySQL_Ops("database_1")
'-----------------------------------------------------------------------------------------------------------------------'
MySQL()
