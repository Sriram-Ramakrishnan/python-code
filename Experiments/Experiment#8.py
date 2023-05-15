filename =  str(input("Enter source file name:"))
filename2 = str(input("Enter destination file name:"))
file = open(filename+".txt","r")
file2 = open(filename2+".txt",'a')
lines = file.readlines()
nlines = []
for i in lines:
    if "a" in i:
        continue
    else:
        nlines.append(i)
file2.writelines(nlines)
file.close()
file2.close()
print("Lines written successfully.")

