def common_gcd(x,y):
   result=1
   a=[]
   b=[]
   c=[]
   ans=x
   ans1=y
   j=0
   i=2
   while True:
    if ans%i==0:
        ans=int(ans/i)
        a.append(i)
        j+=1
        i=2
        continue
    i+=1
    if ans==1:
     break
   j=0
   i=2
   while True:
    if ans1%i==0:
        ans1=int(ans1/i)
        b.append(i)
        j+=1
        i=2
        continue
    i+=1
    if ans1==1:
        break
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
   
print(common_gcd(40,20))