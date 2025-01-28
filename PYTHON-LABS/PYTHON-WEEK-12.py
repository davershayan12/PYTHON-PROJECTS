# try:
#     a = "PYTHON"
#     a[0] = "x"
# except TypeError:
#     print('its Type error')

# math = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
# sci = {'Alice': 92, 'Bob': 88, 'David': 75}

# avg = {}

# for i in math.keys():
#     if i in sci.keys():
#         avg[i] = (math[i] + sci[i]) / 2
#     else:
#         avg[i] = math[i] / 2

# for j in sci.keys():
#     if j not in math.keys():
#         avg[j] = sci[j] / 2
# print(avg)

# product = {'apple': 2, 'banana': 1, 'orange': 3, 'grapes': 5}
# nproduct = {}
# for i in product.keys():
#     nproduct[i] = product[i] + (product[i]*0.1)
    
# math = {'Alice': 90, 'Bob': 80, 'Charlie': 78}
# eng = {'Alice': 85, 'Bob': 75, 'David': 93}

# new = {}

# for i in math.keys():
#     if i in eng.keys():
#         new[i] = [math[i], eng[i]]
#     else:
#         new[i] = [math[i], 0]

# for i in eng.keys():
#     if i not in math.keys():
#         new[i] = [0, eng[i]]
# print(new)

try:
    data = [10, 20, 'abc', 30, 'xyz', 40]
    for i in data:
        print(int(i))
except ValueError:
    print('Invalid Input')

# i = 0
# while i < len(a):
#     c = a[i]
#     print(c)
#     i+=i + 1

# def my_function(x):
#     return x[::-1]

# mytxt = my_function("I wonder how this text looks like backwards")
# print(mytxt)
 
# s= "Welcome"
# for i in range(0, len(s), 2):
#     print(s[i], end = '')

# s = input("Enter a string: ")
# if "Python" in s:
#     print("Python", "is in", s)
# else:
#     print("Python", "is not in", s)

# str='cold'
# list_enumerate=list(enumerate(str))
# print("list enumerate:", list_enumerate)
# print("list length:", len(str))
# s1 = "Welcome to Python"
# s2 = s1.replace("o","abc")
# print(s2)
# a = "Python" + "String"
# b = "<" + a*3 + ">"
# print(b)

# name =input('enter your name')
# ename=f'\t{name}\n\t'
# print(ename)
# print(ename.lstrip())
# print(ename.rstrip())
# print(ename .strip())

# favColor=input( 'enter color:')
# for i in range(3):
#     if i==0 or i==2 :
#         print(favColor*9,end='')
#     for j in range(9):
#        if i==1: 
#         if j==0 or j==8:
#             print(favColor,end='')
#         else:
            
#             for b in range(len(favColor)):
#               print(' ',end='')
#     print()