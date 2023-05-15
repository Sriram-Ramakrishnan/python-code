import re
'''
string  = input()
vowels = re.findall("[aeiou]",string.lower())
symbols = re.findall("[!@#$%^&*()]",string)
space = re.findall("[ ]",string)
print(vowels,symbols,space)
'''

#Write a program to remove zero's in the starting of the numerals. Input: 000200, Output: 200
string = input()
pattern = '^0+'
replace = ''
new_string = re.sub(pattern, replace, string) 
print(new_string)
