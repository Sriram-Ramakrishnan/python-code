data = eval(input())
data_list = []
data_transform = []
k = 1
for col in range(len(data[0])):
    for i in data:
        column = i[col]
        data_list.append(column)
    data_transform.append(data_list)
    k+=1
    data_list = []
for i in data_transform:
    print(i)
