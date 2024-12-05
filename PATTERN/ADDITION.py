i=0
n=4
while i<=n:
    j=0
    while j<=n:
        if(j==n/2 or i==n/2):
            print('*',end='')
        else:
            print('',end=' ')
        j+=1
    print()
    i+=1