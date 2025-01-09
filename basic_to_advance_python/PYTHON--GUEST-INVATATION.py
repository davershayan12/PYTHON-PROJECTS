# Initial guest list.
member = ['David', 'Tanzeel', 'Umer']

# Inviting guests
for i in member:
    print(f'{i}, you are invited.')

# 3.5: Changing guest list
print(f'{member[2]} could not make it to dinner.')

member[2] = 'Daver'

for i in member:
    print(f'{i}, you are invited.')

# 3.6: More guests
print('A bigger table has been arranged.')

member.insert(0, 'Umer')
member.insert((len(member) - 1) // 2, 'Dayan')
member.append('Shayan')

for i in member:
    print(f'{i}, you are invited.')

# 3.7: Shrink guest list
print('Only two people can come to dinner.')
i=len(member)-1
while i >= 2:
    print(f'{member[i]}, sorry we can’t invite you to dinner.')
    member.pop()
    i-=1

# Final guest list
for i in member:
    print(f'{i}, you are still invited.')