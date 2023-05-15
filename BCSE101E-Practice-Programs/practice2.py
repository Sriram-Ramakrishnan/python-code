list1 = [-343,2324,345543,-56544,564,36733]
l = [[],[],[],[],[],[]]
newlist = []
for i in list1:
    if i < 0:
        l[len(str(abs(i)))-1].append(i)
    else:
        l[len(str(i))-1].append(i)
print(l)
for i in range(len(l)):
    if l[i] == []:
        pass
    else:
        if len(l[i]) == 1:
            if str(l[i][0]) == str(l[i][0])[::-1]:
                newlist.append(int(str(l[i][0])[0:len(str(l[i][0]))//2]))
            else:
                if l[i][0] < 0:
                    newlist.append(-abs(int(str(l[i][0])[::-1])))
                else:
                    newlist.append(int(str(l[i][0])[::-1]))
        else:
            s = sum(l[i])
            newlist.append(s)
print(newlist)
            
            
        
