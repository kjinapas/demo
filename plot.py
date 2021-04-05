n=3
k=n
h=n*2
print(' '*(n**2)+"__")
for i in range(n,-1,-1):
    for j in range(1,n+1):
         for k in range(1,j*n):
             print("*",end='')
    print("")
print('')

