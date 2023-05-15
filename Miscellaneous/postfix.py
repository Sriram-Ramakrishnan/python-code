'''def push_stack(list,element):
    list.append(element)
def display_stack(list):
    for i in list:
        print(i,end = ";")
stack =[]
while True:
    print("\nStack Menu\nOptions available:")
    print("1.Push\n2.Pop\n3.Display\n4.Exit")
    opt = int(input("Enter option req. :"))
    if opt == 1:
        element = str(input("Element to be pushed:"))
        push_stack(stack,element)
        print("Element pushed successfully.")
    elif opt == 2:
        if stack == []:
            print("Empty Stack.")
        else:
            stack.pop()
            print("Element popped successfully.")
    elif opt == 3:
        if stack == []:
            print("Empty Stack.")
        else:
            print("Elements in stack:")
            display_stack(stack)
    elif opt == 4:
        break
    else:
        print("Invailid Option")'''

def postfix(list):
    a = list[0]
    b = list[1]
    c = list[2]
    if b in ['+','-','*','/'] or c in ['+','-','*','/']:
        if b == '+':
            list[0] = a + c
            list.remove(b)
            list.remove(c)
        elif b == '-':
            list[0] = a - c
            list.remove(b)
            list.remove(c)
        elif b == '*':
            list[0] = a*c
            list.remove(b)
            list.remove(c)
        elif b == '/':
            list[0] = a / c
            list.remove(b)
            list.remove(c)
        elif c == '+':
            list[0] = a + b
            list.remove(b)
            list.remove(c)
        elif c == '-':
            list[0] = a - b
            list.remove(b)
            list.remove(c)
        elif c == '*':
            list[0] = a*b
            list.remove(b)
            list.remove(c)
        elif c == '/':
            list[0] = a / b
            list.remove(b)
            list.remove(c)
        else:
            pass
        print(list)
        if len(list) <= 2:
            return list
        else:
            postfix(list)
    

l = [32,4,'/',2,'*',12,3,'-','+']
print(postfix(l))
                
        
    
