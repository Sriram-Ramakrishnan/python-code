import pickle
data = []
file_name = str(input("Enter the binary file name to be created :"))
file_name+=".dat"
file =open(file_name,"wb")
while True:
    rollno = int(input("Enter roll number :"))
    name =  str(input("Enter name of student :"))
    marks = int(input("Enter marks :"))
    data.append([rollno,name,marks])
    print("Would you like to insert another record?(y/n):",end = '')
    c = str(input(""))
    if c == 'n':
        break
pickle.dump(data,file)
file.close()
rollno = int(input("Enter roll number whose mark is to be updated:"))
file =open(file_name,"rb")
data = pickle.load(file)
file.close()
for i in data:
    if i[0] == rollno:
        marks = int(input("Enter new marks :"))
        i[2] = marks
        file =open(file_name,"wb")
        pickle.dump(data,file)
        print("Mark uploaded successfully.")
        break
else:
    print("Roll Number not found.")
file.close()
