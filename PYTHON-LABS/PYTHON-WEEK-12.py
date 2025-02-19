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

# m_g={'alice':90,'bob':80,'charlie':70}
# e_g={'alice':30,'bob':70,'David':70}

# new={}
# for d in [m_g,e_g]:
#     for key,value in d.items():
#         if key not in new:
#             new[key]=[value]
#         else:
#             new[key].append(value)
# new["David"].insert(0,0)
# new["charlie"].append(0)
# print(new)

# try:
#     polls='poll.txt'
#     exist=[]
#     with open(polls, 'a') as poll:
#         while True:
#             name = input("name: ")
#             language = input("language: ")
                         
#             if name in exist :
#                 print("Sorry, you already poll!")
#                 continue
             
#             poll.write(f"{name}: {language}\n")
#             exist.append(name)
#             ask = input("yes/no: ")
#             if ask == "no":
#                 break
# except FileNotFoundError:
#     print("File Not Found")

# with open('count.txt', 'r') as search:
#     c = search.read().lower()

#     ask = input("Word to search: ")
#     num=c.count(ask)  
#     print(num)

# describe_city(city="alsaka", country="canda") 

# L = [5, 8, 1, 9, 2, 17, 21, 10]

# while True:
#     con = False
#     for i in range(len(L) - 1):
#         if L[i] >= L[i + 1]:
#             L[i], L[i + 1] = L[i + 1], L[i]
#             con = True
#     if con == False:
#         break
# print(L)

# l = [ "c","d","a","A","Y"]
# while True:
#     swap = False
#     for i in range(len(l)-1):
#         if l[i]> l[i+1]:
#             l[i],l[i+1] = l[i+1],l[i]
#             swap=True
#     if swap == False:
#          break
# print(l)

# l = ["c", "d", "a", "A", "Y"]
# while True:
#     swap = False
#     for i in range(len(l) - 1):
#         if l[i] > l[i + 1]:
#             l[i], l[i + 1] = l[i + 1], l[i]
#             swap = True
#     if swap == False:
#         break
# print(l)

# student = {}
# ff = open('Student.txt', 'r')
# for i in ff:
#     a = i.split(',')
#     student[a[0]] = int(a[1]) 

# avg = 0
# for i in student:
#     avg = avg + student[i]
# avg = avg / len(student)

# print(avg) 
# top_student = []

# for name, marks in student.items():
#     if marks > 85:
#         top_student.append(name)
# with open('top_student.txt', 'w') as topStudent:
#     for i in top_student:
#         topStudent.write(i + '\n')

# sentence = input('sentence: ')

# a_z = sentence.count('a')
# e_z = sentence.count('e')
# i_z = sentence.count('i')
# o_z = sentence.count('o')
# u_z = sentence.count('u')

# total_z = a_z + e_z + i_z + o_z + u_z

# print("total:", total_z)

# tup_z = tuple(sentence.split())

# sorted_sentence = sorted(tup_z)

# print(sorted_sentence)

# Store = {}

# n = int(input("Enter the number of students: "))

# for i in range(n):
#     name = input(' name and marks:').split()
#     Store[name[0]] = int(name[1])

# print("Highest test score:", max(Store.values()))

# Sorted = dict(sorted(Store.items()))

# print("Sorted:", Sorted)

# medicines = {
#     "Centrum": [
#         {"name": "Vitamin C", "strength": "500mg", "dosage": "1 tablet daily"},
#         {"name": "Zinc Plus", "strength": "10mg", "dosage": "1 capsule daily"}
#     ],
#     "Belle Vie": [
#         {"name": "Omega 3", "strength": "1000mg", "dosage": "1 softgel daily"},
#         {"name": "Calcium", "strength": "600mg", "dosage": "1 tablet daily"},
#         {"name": "Iron", "strength": "50mg", "dosage": "1 capsule daily"},
#         {"name": "Vitamin D", "strength": "400IU", "dosage": "1 drop daily"}
#     ],
#     "Mascon": [
#         {"name": "Multivitamin", "strength": "750mg", "dosage": "1 tablet daily"},
#         {"name": "Folic Acid", "strength": "5mg", "dosage": "1 tablet daily"}
#     ]
# }

str=(1,3,5,7)
list_enumerate=list(enumerate(str))
print("list enumerate:", list_enumerate)



# import random
# res = [random.randrange(1, 50, 1) for i in range(7)]
# print ("Random number list is : " +str(res))
# list=[]
# for i in range(10):
#  r=random.randint(1,100)
#  if r not in list: 
#      list.append(r)
# print(random.choices(list,k=3)) 
# st = ["1mg"]
# medicines["GNC"] = [
#     {"name": "Protein Supplement", "strength": "", "dosage": "2 scoops daily"}
# ]
# del(medicines["Belle Vie"][3])
# print(medicines)# Assign the first value from the list to the medicine's strength



# for i in eng.keys():
#     if i not in math.keys():
#         new[i] = [0, eng[i]]
# print(new)

# try:
#     data = [10, 20, 'abc', 30, 'xyz', 40]
#     for i in data:
#         print(int(i))
# except ValueError:
#     print('Invalid Input')

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