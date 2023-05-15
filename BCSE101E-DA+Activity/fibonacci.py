def fibonacci(n):
    x,y = 0,1
    for i in range(n):
        if i == n-1:
            print(y)
        else:
            print(y,end = ',')
        x,y = y,x+y
n = int(input("No of terms:"))
fibonacci(n)
