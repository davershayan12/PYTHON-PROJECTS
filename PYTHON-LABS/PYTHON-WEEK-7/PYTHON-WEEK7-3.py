'''3.    Write a Python program to find GCD of two numbers.'''
def common_gcd(x,y):
   val1=y
   val2=x  
   result=1
   a=[]
   b=[]
   c=[]
   i=2
   while True:
    if val1%i==0:
        val1=int(val1/i)
        a.append(i)
        i=2
        continue
    i+=1
    if val1==1:
     break
   i=2
   while True:
    if val2%i==0:
        val2=int(val2/i)
        b.append(i)
        i=2
        continue
    i+=1
    if val2==1:
        break
   r=0 
   for i in range(len(a)):
       for j in range(r,len(b)):
          if a[i]==b[j]:
            c.append(a[i])
            r+=1
            break
   for i in range(len(c)):
       result*=c[i]
   return f'{result} is gcd of {x} and {y}'
   
print(common_gcd(100,80))