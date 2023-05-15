
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
    
