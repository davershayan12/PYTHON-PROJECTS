i=5
while i>=0:
    j=5
    k=1
    while k<=i:
        print(' ',end='')
        k+=1
    print(' *',end='')
    while j>i:
        print(' ',end=' ')
        j-=1
    if i!=5:
        print('*',end='')
    print()    
    i-=1
i=1
while i<=5:
    j=1
    k=5
    while j<=i:
        print(' ',end='')
        j+=1
    print(' *',end='')
    while k>i:
        print(' ',end=' ')
        k-=1
    if i!=5:
        print('*',end='')
    print()    
    i+=1