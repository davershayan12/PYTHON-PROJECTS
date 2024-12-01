'''2.	Write a user-defined function called max( ), that returns the maxium of three integernumbers.'''
def max(num1,num2,num3):
    if num1>num2 and num1>num3:
        return f'{num1} is grater than both {num2} and {num3}.'
    elif num2>num1 and num1>num3:
        return f'{num2} is grater than both {num1} and {num3}.'
    elif num3>num1 and num3>num2:
        return f'{num3} is grater than both {num1} and {num2}.'
num1=int(input('enter your number1:'))
num2=int(input('enter your number2:'))
num3=int(input('enter your number3:'))
print(max(num1,num2,num3))