'''
def readfilechar():
    name = input("Enter File name without extension:")
    f = open(name+".txt","r")
    lines = f.readlines()
    uc,lc,vc,cc = 0,0,0,0
    for line in lines:
        words = line.split()
        for word in words:
            for i in range(len(word)):
                if word[i].lower() in ["a","e","i","o","u"]:
                    vc+=1
                if word[i].lower() not in ["a","e","i","o","u"]:
                    cc+=1
                if word[i].isupper():
                    uc+=1
                if word[i].islower():
                    lc+=1
    while True:                
        print("File options:\n1. Vowels\n2. Consonants\n3. Uppercase letters\n4. Lowercase letters")
        ch = int(input("Enter Choice: "))
        if ch == 1:
            print("No. of Vowels:",vc)
        elif ch == 2:
            print("No. of Consonants:",cc)
        elif ch == 3:
            print("No. of Uppercase letters:",uc)
        elif ch == 4:
            print("No. of Lowercase letters:",lc)
        else:
            print("Exited successfully")
            break
readfilechar()  

max()     
    '''
def fibonacci():
    while x<=100:
        x= 0
        y =1
        print(x+y)
        x,y=y,x+y
fibonacci()





















