#1.	Write a program to add first seven terms twice of the following series:
#1/1!+2/2!+....
i=1
fac=1
ans=0
while i <= 7:
    fac*=i
    ans=i/fac
    print(f'{i}/{i}!')
    i+=1
print(ans)