import random

def player() -> list:
    roles = {"warrior": [110, 20, "Dimension Strike", "Iron Slash", "Defence"],"archer": [100, 30, "Fire Arrow", "Multiple Arrow", "Defence"],"dagger": [90, 40, "One Point Slash", "Back Slash", "Defence"]}
    print("Enter your role")
    for role, stats in roles.items():
        print(f"{role}:\n HP: {stats[0]}\n Attack power: {stats[1]}\n 1.Attack: {stats[2]}\n 2.Attack: {stats[3]}\n 3.{stats[4]}")
    while True:
        role = input().lower()
        if role in roles:
            player = roles[role][:]
            return player
        else:
            print("invaild choice! try again")

def battle_ground():
    roles = {"warrior": [200, 20, "Dimension Strike", "Iron Slash", "Defence"],"archer": [150, 30, "Fire Arrow", "Multiple Arrow", "Defence"],"dagger": [120, 40, "One Point Slash", "Back Slash", "Defence"]}
    playerrole = player()
    Health = playerrole[0]
    Attack = playerrole[1]
    for role, stats in roles.items():
        print(f"your enemy: {role}:Hp: {stats[0]}Attack: {stats[1]}")
        while True:
            print(f"your HP: {player[0]} \n Your enemy Hp:{stats[0]}")
            print(f"1.{playerrole[2]}\n2.{playerrole[3]}\n3.{playerrole[4]}")
            
            userAttack = int(input("enter number of Attack (1-3): "))
            if userAttack!= 1 or userAttack != 2 or userAttack !=3:
                print("inivalid attack number")
                continue
            enemyAttack = random.randint(1, 3)
            if (userAttack == 1 and enemyAttack == 2) or (userAttack == 2 and enemyAttack == 3) or (userAttack == 3 and enemyAttack == 1):
                stats[0] -= playerrole[1]
                print(f"you hit the enemy with {playerrole[userAttack+2]} !")
            elif (userAttack == 1 and enemyAttack == 3) or(userAttack ==3 and enemyAttack== 2) or (userAttack == 2 and enemyAttack ==1):
                playerrole[0] -= stats[1]
                print(f"Enemy hits you with {stats[enemyAttack+2]}!")
            else:
                print("both launch the same attack.No damage")

            if stats[0] <= 0:
                Health += 30
                playerrole[0]=Health
                Attack += 10
                playerrole[1]=Attack
                print(f"You won!your HP increases to {playerrole[0]} and Attack to {playerrole[1]}")
                break
            elif playerrole[0] <= 0:
                print("You lost!")
                break
        if playerrole[0] <= 0:
            break
    print("Congratulations! You defeated all enemies.")

battle_ground()