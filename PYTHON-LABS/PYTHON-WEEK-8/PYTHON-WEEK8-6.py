def add(x,lst=[] ):
    if x not in lst:
        lst.append(x)
        return lst

def main():
    list1 = add(2)
    print(list1)
    list2 = add(3, [11, 12, 13, 14])
    print(list2)
main()
