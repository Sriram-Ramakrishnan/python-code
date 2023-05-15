lis = []
n = int(input("Enter total no. of elements:"))
for i in range(n):
    element = int(input("Enter Element:"))
    lis.append(element)

print("List:")
for i in range(n):
    print('Element#',i+1,':',lis[i])

print('Maximum value Element:',max(lis))
print('Mininum Value Element:',min(lis))
