#Function:
def linearsearch(list,value):
    if value in list:
        print('Element found at index',list.index(value))

    else:
        print('Element does not exist')
#Program:
n = int(input("Enter total no. of elements:"))
lis = []
for i in range(n):
    element = int(input("Enter Element:"))
    lis.append(element)

value = int(input("Enter element to be searched:"))
linearsearch(lis,value)
