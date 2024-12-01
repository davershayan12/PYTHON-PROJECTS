def common_gcd(x,y):
   result=1
   a=[]
   b=[]
   c=[]
   j=0
   i=2
   while True:
    if x%i==0:
        x=int(x/i)
        a.append(i)
        j+=1
        i=2
        continue
    i+=1
    if x==1:
     break
   j=0
   i=2
   while True:
    if y%i==0:
        y=int(y/i)
        b.append(i)
        j+=1
        i=2
        continue
    i+=1
    if y==1:
        break
   print(a)
   print(b)
   r=0 
   for i in range(len(a)):
       for j in range(len(b)):
          if a[i]==b[j]:
            c.append(a[i])
            r+=1
            break
   for i in range(len(c)):
       result*=c[i]
   return result
   
print(common_gcd(30,15))