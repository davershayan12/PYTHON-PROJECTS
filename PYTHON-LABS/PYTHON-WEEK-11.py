# # def guess_the_capitals():
# #     correct = 0
# #     incorrect = 0
# #     capitals = {"Canada": "Ottawa",
# #     "Germany": "Berlin",
# #     "France": "Paris",
# #     "United Kingdom": "London",
# #     "Italy": "Rome",
# #     "Spain": "Madrid",
# #        }
# #     for key , value in capitals.items():
# #        userguess=input(f"enter your guess of {key}: ") 
# #        if userguess== value:
# #            correct+=1
# #            print('coreect answer!')
# #        else:
# #            incorrect+=1
# #            print('incoreect answer!')
# #     print(f'coreect:{correct}    incoreect:{incorrect}')
# # guess_the_capitals()



# favouritePlaces={
#     "Alice": ["Paris", "New York", "Tokyo"],
#     "Bob": ["London", "Sydney", "Rome"],
#     "Charlie": ["Berlin", "Amsterdam", "Barcelona"]
# }

# for key,value in favourite_places.items():
#     print(f"{key} favourite place is:")
#     for i in range(3):
       
# #        print(f"{value[i]}")
# a = np.array([])
# b=[]
# n=[]
# for i in range(6):
    
#     if i==0 or i==1 or i==5:
#       for j in range(10):
#         n.append(i)
# a=np.append(n,b)  
# print(a)
import numpy as np
print(np.arange(2,11).reshape(3,3))