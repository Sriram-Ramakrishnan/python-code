#Program#4:Browser problem
hours = int(input("Enter the no. of hours spent:"))
minutes = int(input("Enter the no. of minutes spent:"))
if hours >= 7:
    print("Invalid input")
else:
    if hours >=5:
        cost = 200 + (hours-5)*50 + minutes*1
    else:
        cost = hours*50 + minutes*1
print("Bill for Internet Browsing = Rs.",cost)
