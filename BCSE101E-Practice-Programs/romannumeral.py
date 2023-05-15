num = int(input())
unitsplace = num%10
tensplace =  num//10
romnum = ''
if tensplace in [1,2,3]:
    romnum = 'X'*unitsplace
elif tensplace == 4:
    romnum = "XL"
elif tensplace in [5,6,7,8]:
    romnum = "L"+"X"*(tensplace-5)
elif tensplace == 9:
    romnum = "XC"
else:
    pass

if unitsplace in [1,2,3]:
    romnum += 'I'*unitsplace
elif unitsplace == 4:
    romnum += "IV"
elif unitsplace in [5,6,7,8]:
    romnum += "V"+"I"*(unitsplace-5)
elif unitsplace == 9:
    romnum += "IX"
else:
    pass

print(romnum)


    
