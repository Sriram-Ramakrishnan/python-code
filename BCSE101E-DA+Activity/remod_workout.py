# r'\t string' will print '\t string' instead of '     string'
# import re
# sentence = "ABC . . ."
# pattern =  re.compile(r'\.')




# sub():
# subbed_sentence =  pattern.sub(r"\2\3",sentence)
# Above syntax will substitute the groups of the pattern and return it.
# Note: 0 is the entire string, 1 to number of groups added -1 will be the respective groups



# matches =  pattern.findall(sentence)


import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
800-666-1235
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
"""
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'(8|9)00.(5{3}|6{3}).\d{4}')

# findall() method:
matches = pattern.findall(text_to_search)
# Returns a list of values where the respective pattern matches the searching string 
# Note: findall() prioritizes groups so if we use findall for a pattern 
print("findall() Method:")
for i in matches:
    print(i)

# finditer() method:
print("finditer() Method:")
matches =  pattern.finditer(text_to_search) # Returns an object with the found results
for i in matches:
    print(i.group(0)) #Prints the entire string found

# match() 
# Searches the starting and end of the string only: if it is a match,
matches =  pattern.match(text_to_search)
print("Match Method:",matches)

# search()
match = pattern.search(text_to_search)
print("Search Method:",match)
"""
def passwordcheck():
    password =  str(input("Password: "))
    pattern =  re.compile(r"([A-Za-z0-9]|[!@#$%^&*_+=.]){8,16}")
    if pattern.match(password) != None:
        strong_pattern = re.compile(r"^.+[!@#$%^&*_+=].+$")
        if strong_pattern.match(password) != None:
            print("Strong Password")
        else:
            fair_pattern = re.compile("^.+[0-9].+$")
            if fair_pattern.match(password) != None:
                print("Fair Password.")
            else:
                print("Weak Password.")

def email_checker():
    string = str(input("Email :"))
    result =  re.search("^.+@.+mail\.com",string)
    if result:
        print("Valid")
    else:
        print("Invalid")

def mobile_no_checker():
    mobno = str(input("Mobile number:"))
    result = re.search("^\d\d{8}\d$",mobno)
    if result:
        print("Valid")
    else:
        print("Invalid")


def dob_checker():
    dob = str(input("Date of birth:"))
    result = re.search("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/(19|20)\d\d$",dob)
    if result:
        print("Valid")
    else:
        print("Invalid")


def charscheck():
    filename = str(input())
    f = open(filename+".txt",'r')
    lists = f.readlines()
    v,c,uc,lc = 0,0,0,0
    for i in lists:
        vs = re.findall("[aeiou]",i,re.IGNORECASE)
        cs = re.findall("([^aeiou]&[a-z])",i,re.IGNORECASE)
        ucs = re.findall("[A-Z]",i)
        lcs = re.findall("[a-z]",i)
        if vs != []:
            v+=len(vs)
        if cs != []:
            cs+=len(cs)
        if ucs != []:
            uc+=len(ucs)
        if lcs != []:
            lc+=len(lcs)
    print(lc,uc,v,c)

charscheck()