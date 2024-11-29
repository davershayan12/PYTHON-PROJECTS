'''2.	Write a program to print all prime numbers from 900 to 1000. 
[Hint: Use nested loops, break and continue]
'''
i=900
while i<=1000:
    count=0
    num=2
    while num<=1000:
        if i%num==0:
            count+=1
            if count==2:
                break
        num+=1
        
    if count<2:
        print(i)    
    i+=1