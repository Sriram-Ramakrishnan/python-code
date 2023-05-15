filename = str(input("Enter the name of the file:"))
file_hash = open(filename+".txt","r")
content = file_hash
for i in content:
    print(i)
