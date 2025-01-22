guest =[]
for i in range (5):
    x = input("Guest Name to invite :")
    guest.append(x)
for guests in guest:
    print(f"{guests} you are invited for the Dinner")
print(f"sorry {guest[0]}, can't make it to the dinner")
del guest[0]

guest.insert(0,"David")
for guests in guest:
    print(f"{guests} you are invited for the Dinner")