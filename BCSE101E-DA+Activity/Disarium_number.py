number = int(input("Enter Number :"))
string_of_number = str(number)
length = len(string_of_number)
disarium_number = 0
for i in range(length):
    num = int(string_of_number[i])
    cube_num = num**3
    disarium_number += cube_num
if disarium_number == number:
    print("Entered number is a Disarium Number")
else:
    print("Entered number is not a Disarium Number")
