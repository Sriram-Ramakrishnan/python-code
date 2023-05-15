#Experiments:
content = '''Class XII Experiments:
1.  Program to check entered number is prime or not
2.  Program to search any word in given string or sentence
3.  Program for Linear search
4.  Program to check given string is palindrome or not
5.  Program to read and display file content line by line with each word separated by '#'
6.  Program to read the content of file and display the total number of consonants vowels uppercase letters lower case letters
7.  Program to create binary file to store roll number and name search for any roll number and display name if the roll number is found otherwise print roll number not found
8.  Program to create binary file to store roll number name and marks and update marks of entered roll number
9.  Program to read the content of the file line by line and write to another file except for the lines which contains an 'a' in it
10. Program to create csv file and store Emp no name salary and search any Empno display name salary and if not found display appropriate message
11. Program to generate random number from 1 to 6 simulating a dice
12. Program to implement stack in Python using list
13. Program to implement queue in Python using list
14. Program to take iOS sample phishing email and find out the most common word occurring'''
print(content)
while True:
    n = int(input("Experiment to execute : "))
    if n == 1:
        num = int(input('\tEnter Number : '))
        for i in range(2,((num//2)+1)):
            if num%i==0:
                print('\tGiven Number',num,'is not a Prime Number')
                break
        else:
            print('\tGiven Number',num,'is a Prime Number')

    elif n == 2:
        sentence = str(input("Enter Sentence : "))
        searchword = str(input("Enter word you would like to search : "))
        words = sentence.split()

        for i in words:
            if searchword == i:
                print("The word '",searchword,"' is present in the sentence")
                break

        else:
            print("The word '",searchword,"' is not present in the sentence")

    elif n == 3:
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

    elif n == 4:
        string = str(input("Enter String : "))
        if string[::-1] == string:
            print("Given string is a Palindrome")
        else:
            print("Given string is not a Palindrome")

    elif n == 5:
        filename = str(input("Enter the name of the file:"))
        file_hash = open(filename+".txt","r")
        content = file_hash.read()
        for i in range(len(content)):
                if content[i] == ' ':
                    print('#',end = '')
                else:
                    print(content[i],end = '')
                    
                
    elif n == 6:
        lc = uc = vc = cc = 0
        filename = str(input("Enter the name of the file:"))
        file_hash = open(filename+".txt","r")
        content = file_hash.readlines()
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        for i in content:
            words = i.split()
            for j in words:
                for k in range(len(j)):
                    if j[k].isupper():
                        uc+=1
                    else:
                        lc+=1
                    if j[k] in vowels:
                        vc+=1
                    else:
                        cc+=1
        print("Statistics of the content:\nNumber of :\nUppercase letters: ",uc,"\nLowercase letters:",lc,"\nVowels:",vc,"\nConsonants:",cc)

    elif n == 7:
        import pickle
        bin_file = open("Student.dat","ab+")
        


        
    y_n = str(input("\nContinue the program:"))
    if y_n == 'y':
        pass
    else:
        print("Terminated program.")
        break
                
        
        
        


























