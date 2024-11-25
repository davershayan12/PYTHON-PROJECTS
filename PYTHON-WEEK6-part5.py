#1.	Write a program to add first seven terms twice of the following series:
#1/1!+2/2!+....
i=1
fac=1
while i <= 7:
    fac*=i
    print(f'{i}/{fac}!')
    i+=1