'''
matrix = []
for i in range(3):
    l = []
    for j in range(3):
        a = int(input())
        l.append(a)
    matrix.append(l)
'''
def Cmatrix(L):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(1,4):
        for j in range(1,4):
            if (i+j)%2 == 1:
                C[i-1][j-1] = -m(L,i,j)
            else:
                C[i-1][j-1] = m(L,i,j)
    print(C)

def m(L,i,j):
    n = []
    for k in range(1,4):
        for l in range(1,4):
            if k!=i and l!=j:
                n.append(L[k-1][l-1])
    return n[0]*n[3]-n[1]*n[2]
L = [[1,2,3],[4,5,6],[7,8,9]]
Cmatrix(L)                
                
