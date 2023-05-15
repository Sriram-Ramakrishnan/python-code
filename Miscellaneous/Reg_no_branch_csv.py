import csv
filename = "Details"
filename+=".csv"
file = open(filename,"r")
writer = csv.writer(file)
file.close()
file = open(filename,"r")
read =csv.reader(file)
l = file.readlines()
BCI = []
for line in l:
    if line[0:5]=="21BCB":
        BCI.append(line)
file.close()

def reg_no(string):
    regno = int(string[5:9])
    return regno

def sorting_list(list):
    l = ["" for i in list]
    num,new = [],[]
    for i in list:
        j = reg_no(i)
        num.append(j)
    num.sort()
    
    for i in list:
        j = reg_no(i)
        l[num.index(j)] = i
    return l

BCI_up = sorting_list(BCI)

file = open("BCB.csv","w")
writer = csv.writer(file)
for i in BCI_up:
    file.write(i)
file.close()
        
