def primeno(): 

    num = int(input('Enter Number : ')) 

    for i in range(2,((num//2)+1)): 

        if num%i==0: 

            print('\tGiven Number',num,'is not a Prime Number') 

            break 

    else: 

        if num == 1: 

            print("1 is neither prime nor composite!") 

        else: 

            print('\tGiven Number',num,'is a Prime Number') 

 

def armstrongno(): 

    number = int(input("Enter Number :")) 

    string_of_number = str(number) 

    length = len(string_of_number) 

    armstrong_number = 0 

    for i in range(length): 

        num = int(string_of_number[i]) 

        cube_num = num**3 

        armstrong_number += cube_num 

    if armstrong_number == number: 

        print("Entered number is an Armstrong Number") 

    else: 

        print("Entered number is not an Armstrong Number") 

     

 

def disariumno(): 

    number = int(input("Enter Number :")) 

    string_of_number = str(number) 

    length = len(string_of_number) 

    disarium_number = 0 

    for i in range(1,length+1): 
        num = int(string_of_number[i-1]) 

        power_num = num**i 

        disarium_number += power_num 

    if disarium_number == number: 

        print("Entered number is a Disarium Number") 

    else: 

        print("Entered number is not a Disarium Number") 

 

def tempchange(): 

    celsius = float(input("Enter Celsius Degrees :")) 

    fahrenheit = (9/5)*celsius + 32 

    print("%.2f Celsius degrees is equal to"%celsius,"%.2f Fahrenheit."%fahrenheit) 

 

def kmtomiles(): 

    km = float(input("Enter the value of Kilometers travelled:")) 

    miles = km*1.6093 

    print("%.2f Kilometers is equal to"%km,"%.2f miles."%miles) 

 

def runprog(): 

    print(""" 

    1.Prime No. check 

    2.Armstrong No. check 

    3.Disarium No. check 

    4.Celsius to Fahrenheit conversion 

    5.Km to miles conversion 

    Enter program no to be executed:""",end = '') 

    a = int(input()) 

    if a == 1: 

        primeno() 

        runprog() 

    elif a == 2: 

        armstrongno() 

        runprog() 

    elif a == 3: 

        disariumno() 

        runprog() 

    elif a == 4: 

        tempchange() 

        runprog() 

    elif a == 5: 

        kmtomiles() 

        runprog() 

    else: 

        pass 

a,b = 0,2
for i in range(a,b):
    print(i)
print("Operation successful")
print("It is within feasible distance:")
print("Its fine ")