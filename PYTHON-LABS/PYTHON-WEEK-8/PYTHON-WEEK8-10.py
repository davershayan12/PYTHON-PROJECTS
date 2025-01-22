def printsquare():
    square=[]
    for i in range(8):
        num=int(input('enter the value: '))
        square.append(num*num)
    return square
print(printsquare())