import pickle
data = []
file_name = str(input("Enter the binary file name to be created :"))
file_name+=".dat"
file =open(file_name,"wb+")
while True:
    rollno = int(input("Enter roll number :"))
    name =  str(input("Enter name of student :"))
    data.append([rollno,name])
    print("Would you like to insert another record?(y/n)",end = '')
    c = str(input(""))
    if c == 'n':
        break
pickle.dump(data,file)
file.close()
rollno = int(input("Enter roll number to be searched:"))
file =open(file_name,"rb+")
data = pickle.load(file)
for i in data:
    if i[0] == rollno:
        print("Roll No:",i[0],",Name:",i[1])
        break
else:
    print("Roll Number not found")


    
