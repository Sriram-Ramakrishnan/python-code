emails = ["abc@lottery.com","asd@wincash.com",
          "s@wincash.com","gsdf@getrich.com",
          "fjsk@lottery.com","lkm@wincash.com",
          "hgf@wincash.com","cnb@getrich.com",
          "qwe@lottery.com","nmj@getrich.com"]
d = {}
print("Phishing Emails:")
for i in emails:
    print(i)
    x=i.split('@')
    for j in x:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
max_word = max(d,key=d.get)
print("\nMost Common Occuring word is: ",max_word)

        
        
    
