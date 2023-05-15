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
