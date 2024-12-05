i=0
n=4
while i<=n:
    j=0
    while j<=n:
        if(j==i or j==n-1):
            print('*',end='')
        else:
            print(' ',end=' ')
        j+=1
    print()
    i+=1