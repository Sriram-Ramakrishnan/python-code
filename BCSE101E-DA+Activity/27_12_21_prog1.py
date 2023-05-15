def ordering(s):
    s = list(s)

    string = ""
    for i in range(len(s)):

        if i+1 <= len(s)-1:
            if s[i] != s[i+1]:
                string+=s[i]+' '
            elif s[i] == s[i+1]:
                string+=s[i]
                if i+1 == len(s)-1:
                    string+=s[i]
                else:
                    pass
    l = string.split()
    for i in l:
        t = (len(i),int(i[0]))
        print(t,end =' ')
            
ordering('1222311')

        
