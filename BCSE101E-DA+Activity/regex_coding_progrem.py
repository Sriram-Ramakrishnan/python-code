'''
^ - Start eg: ^a
$ - End    a$
[] - sequences eg [abc] or [A-Za-z]
[^] - anything other than watever mentioned
Eg [^abcd] means anything other than a b c d
. - any charecter except newline
* - No of occurences >= 0     eg: ma*n 
+ - No of occurences >= 1     eg: ma+n
? - No of occurences = 0 or 1 eg: ma?n
{n,m} Repetition: eg: a{2,5} = aa to aaaaa
| - or operator eg: a|b
() - Groups eg: (c|d)xy = cxy or dxy
\ - Used if we have to specify other meta charecters above
eg \$a = $a pattern

Special sequences:
\AWord - Checks if 'Word' present at starting of string
Word\Z - Checks if 'Word' present at end of string
\b - letter(s) present at starting or ending of each word eg: \bword word\b
\B - Opposite of \b
\d - Decimals
\D - Non decimals i.e. [^0-9]
\s - whitespace i.e. (remember tnrfv) [ \t\n\r\f\v]
\S - non whitespace i.e [^ \t\n\r\f\v]
\w - ALphanumeric chars [0-9A-Za-z_]
\W - Non alphanumeric chars [^0-9A-Za-z_]
<([A-Z][A-Z0-9]*)\b[^>]*>.*?</\1>
'''
import re



data = list(input())
data_list = []
data_transform = []
k = 1
for col in range(len(data[0])):
    for i in data:
        column = i[col]
        data_list.append(column)
    data_transform.append(data_list)
    k+=1
    data_list = []
for i in data_transform:
    print(i)














