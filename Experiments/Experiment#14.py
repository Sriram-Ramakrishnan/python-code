def push_queue(list,element):
    list.append(element)
def display_queue(list):
    for i in list:
        print(i,end = ";")
queue =[]
while True:
    print("\nQueue Menu\nOptions available:")
    print("1.Push\n2.Pop\n3.Display\n4.Exit")
    opt = int(input("Enter option req. :"))
    if opt == 1:
        element = str(input("Element to be pushed:"))
        push_queue(queue,element)
        print("Element pushed successfully.")
    elif opt == 2:
        if queue == []:
            print("Empty queue.")
        else:
            queue.pop(0)
            print("Element popped successfully.")
    elif opt == 3:
        if queue == []:
            print("Empty queue.")
        else:
            print("Elements in stack:")
            display_queue(queue)
    elif opt == 4:
        break
    else:
        print("Invailid Option")
