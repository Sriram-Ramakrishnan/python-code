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
