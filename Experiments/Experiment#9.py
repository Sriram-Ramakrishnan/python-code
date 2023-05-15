def text_read(filename):
    file = open(filename+'.txt','r')
    read = file.read()
    print(read)
    file.close()
def text_readline(filename):
    file = open(filename+'.txt','r')
    i = 1
    while True:
        line = file.readline()
        if line == '':
            break
        else:
            print("Line#",i,end = ':')
            print(line)
            i+=1
    file.close()    
def text_readchar(filename,char):
    file = open(filename+'.txt','r')
    print(file.read(char))
    file.close()
print("""Read Function utility:\n1)Read Full File.\n2)Read line by line
3)Read till 'n' charecters\n4)Exit""")
opt = int(input("Option :"))
while opt <= 3:
    if opt == 1:
        text_read("python")
    elif opt == 2:
        text_readline("python")
    elif opt == 3:
        char = int(input("How many charecters:"))
        text_readchar("python",char)
    print("""\nRead Function utility:\n1)Read Full File.\n2)Read line by line
3)Read till 'n' charecters\n4)Exit""")
    opt = int(input("Option :"))
        
