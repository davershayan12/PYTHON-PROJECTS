# def authenticateUser(users):
#     while True:
#         reus = input('Enter username: ')
#         repass = input('Enter password: ')
#         if reus in users and users[reus] == repass:
#             print('Correct')
#             return True
#         else:
#             print('Wrong password')
#             ask = input('Continue (yes/no): ').lower()
#             if ask == 'no':
#                 return False

# def humanVerification():
#     while True:
#         for i in range(1, 3):
#             for j in range(1, i + 1):
#                 print('*', end='')
#             print()
#             if i == 2:
#                 break
#         ques = int(input('How many * are there to check you are human or not: '))
#         if ques == 3:
#             print('You are human')
#             return True
#         else:
#             print('Incorrect')
#         reask = input('Continue (yes/no): ').lower()
#         if reask == 'no':
#             return False

# def main():
#     users = {}
#     user = input('Input username: ')
#     passw = input('Input password: ')
#     users[user] = passw

#     if authenticateUser(users):
#         if humanVerification():
#             print('Access granted')
#         else:
#             print('Human verification failed')
#     else:
#         print('Authentication failed')
# main()

def test(a):
  def add(b): 
      a =+ 1 
      return a+b 
  return add 
func = test(4) 
print(func(4))
