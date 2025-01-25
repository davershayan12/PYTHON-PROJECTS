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
       
#        print(f"{value[i]}")
import re

def replace_with_regex(file_path, pattern, replacement):
    with open(file_path, 'r') as file:
        content = file.read()
    
    updated_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w') as file:
        file.write(updated_content)

replace_with_regex('example.txt', r'\bword\b', 'replacement')

