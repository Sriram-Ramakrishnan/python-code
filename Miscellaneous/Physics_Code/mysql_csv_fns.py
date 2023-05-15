
import csv
import time
#MySQL Functions
#Showing loading action
def loading(n):
    i = 0
    while i <= n:
        time.sleep(1)
        print(" .",end = '')
        i+=1
"----------------------------------------"
def MySQL_details():
    try:
        list = csv_read("MySQL")
        list[0].append("old")
        return list[0]

    except FileNotFoundError:
        print("\n*New system detected.\n\tEnter the following details for access to database:")
        host = str(input("Host : "))
        user = str(input("User : "))
        passwd = str(input("Password : "))
        content = [[host,user,passwd]]
        csv_write("MySQL",content)
        content = [[host,user,passwd,"new"]]
        return content[0]
"----------------------------------------"
def backup_transfer(database,oldornew):
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2],db = database)
    mycursor = mydb.cursor()
    filename = str(database)+".txt" 
    try:
        f = open(filename,'r')
    except FileNotFoundError:
        print("No previous data were found. You will be starting with a new database.")
        f = open(filename,'a')
        f.close()
    else:
        print("Database already exists.")
        content = f.readlines()
        if oldornew == 'new':
            while True:
                print("\nWould you like to back up the data to this system (y/n) ",end = '')
                ans_1 =  str(input(":"))
                if ans_1.lower() == 'y':
                    for query in content:
                        mycursor.execute(query)
                        mydb.commit()
                    break
                elif ans_1.lower() == 'n':
                    print("WARNING! Previously stored data will be deleted and cannot be restored.")
                    print("Would you still like to back up the data to this system (y/n) ",end = '')
                    ans_2 = str(input(":"))
                    if ans_2.lower() == 'n':
                        f.close()
                        print("Deleting Previous data .",end = '')
                        loading(10)
                        f = open(filename,"w")
                        f.close()   
                        print("Creating New file .",end = '')
                        loading(5)
                        print("Successfully done. New database is ready to go!")
                        break
                    else:
                        print("Type yes if you want to transfer the data to your system.")
        elif oldornew == 'old':
            pass
"----------------------------------------"                   
def MySQL_create_db(database):
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2])
    mycursor = mydb.cursor()
    query = "CREATE DATABASE "+database
    mycursor.execute(query)
    mydb.commit() 
"----------------------------------------"
def MySQL_create(table_name,parameters,database):#parameters will be in nested list format
    title_list = []
    for i in range(len(parameters)):
        name_column = parameters[i][0]
        var_type = parameters[i][1]
        var_len = parameters[i][2]
        constraint_1= parameters[i][3]

        if var_len == '':
            c_details = (name_column+' '+var_type +' '+constraint_1+',')

        else:
            var_len = int(var_len)
            c_details = (name_column+' '+var_type+"(%d)"+' '+constraint_1+',') %var_len
        title_list.append(c_details)
    my_snip= ''
    for j in title_list:
        my_snip+=j
    table_dets = "CREATE TABLE "+table_name+" ("+(my_snip[:len(my_snip)-1])+")"#Removes the last comma in the query
    return table_dets
"----------------------------------------"
def MySQL_insert(table_name,data,database):
    my_snippet = "INSERT INTO "+table_name+" VALUES %s"  
    my_values= tuple(data)     # Base tuple
    my_code = (my_snippet %(my_values,))
    return my_code
"----------------------------------------"
def MySQL_update(table_name,update_parameters,database):
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2],db = database)
    mycursor = mydb.cursor()
    mycursor.execute("DESC "+table_name)
    my_data = mycursor.fetchall()
    my_title = {}
    for i in my_data:
        for _ in range(len(my_data)):
            title = i[0]
            title_type = i[1]
            my_title[title] = title_type
            break
    update_row = update_parameters[0]
    while True:
        if update_row in my_title.keys():
            if my_title[update_row][:4].lower == "char":
                modify_val = str(update_parameters[1])
                
            elif my_title[update_row][:3].lower == "int":
                modify_val = int(update_parameters[1])

            elif my_title[update_row][:5].lower == "float":
                modify_val = float(update_parameters[1])

            else:
                modify_val = str(update_parameters[1])
            break

        else:
            print("Column doesn't exist,Try again")
            update_row = str(input("Enter the column to be modified:"))
    condition_row = update_parameters[2]
    while True:
        if condition_row in my_title.keys():
            if my_title[condition_row][:4].lower == "char":
                condition_val = str(update_parameters[3])

            elif my_title[condition_row][:3].lower == "int":
                condition_val = int(update_parameters[3])

            elif my_title[condition_row][:5].lower == "float":
                condition_val = float(update_parameters[3])

            else:
                condition_val = str(update_parameters[3])
            break
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
"----------------------------------------"
def MySQL_execute(query,database):#Executes the query and writes it in a text file for backtracking and restoring data.
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2],db = database)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()
    if query[:6] in ['INSERT','UPDATE','DELETE']:
        dbfile = str(str(database)+".txt")
        file = open(dbfile,"a")
        nquery = str(query) + "\n"
        file.write(nquery)
"----------------------------------------"
def type_converter(value):
    return str(value)
"----------------------------------------"
def MySQL_display(data,col_names):
    data_dict = rev_table(data)       
    str_data = []
    len_list2 = []    
    e = 0    
    for i in data_dict:                                # i is a single column's data
        len_list,str_list = [],[]        
        for j in i:
            len_list.append(len(j))                    # length of each data is added             
        max_len = max(len_list)                        # maximum is taken for equal and neat spacing
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
"----------------------------------------"
def csv_read(filename):
    content = []
    filename += ".csv"
    file = open(filename,"r")
    read = csv.reader(file)
    for i in read:
        if i == []:
            pass
        else:
            content.append(i)
    file.close()
    return content    
"----------------------------------------"
def csv_write(filename,content):
    filename += ".csv"
    file = open(filename,"w+")
    writer = csv.writer(file)
    writer.writerows(content)
    file.close()
"----------------------------------------"
def rev_table(data):#This function reverts rows into columns and vice versa.
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
    return data_dict
"----------------------------------------"
def db_check(database):
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2])
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    tables = mycursor.fetchall()
    mydb.commit()
    for i in tables:
        if database == i[0]:
            break
    else:
        MySQL_create_db(database)
"----------------------------------------"
def table_check(table_name,parameters,database):
    l = MySQL_details()
    mydb = mysql.connector.connect(host = l[0],user = l[1],passwd = l[2],db = database)
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    mydb.commit()
    for i in tables:
        if table_name == i[0]:
            break
    else:
        query = MySQL_create(table_name,parameters,database)
        MySQL_execute(query,database)
"----------------------------------------"            
def MySQL_delete(table_name,parameters):
    query_1 = "DELETE FROM " + str(table_name)
    query_2 = " WHERE " + str(parameters[0]) + " = " +  str(parameters[1])
    statement =  query_1 + query_2
    return statement
"----------------------------------------"
