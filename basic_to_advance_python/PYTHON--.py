import random

def player() -> list:
    roles = {"warrior": [110, 20, "Dimension Strike", "Iron Slash", "Defence"],
             "archer": [100, 30, "Fire Arrow", "Multiple Arrow", "Defence"],
             "dagger": [90, 40, "One Point Slash", "Back Slash", "Defence"]}
    print("Enter your role")
    for role, stats in roles.items():
        print(f"{role}:\n HP: {stats[0]}\n Attack power: {stats[1]}\n 1.Attack: {stats[2]}\n 2.Attack: {stats[3]}\n 3.{stats[4]}")
    while True:
        role = input().lower()
        if role in roles:
            playerRole = roles[role]
            return playerRole
        else:
            print("Invalid choice! Try again")

def battle_ground():
    roles = {"warrior": [200, 20, "Dimension Strike", "Iron Slash", "Defence"],"archer": [150, 30, "Fire Arrow", "Multiple Arrow", "Defence"],"dagger": [120, 40, "One Point Slash", "Back Slash", "Defence"]}
    
    playerRole = player()
    health = playerRole[0]
    attack = playerRole[1]
    
    for enemy, stats in roles.items():
        
        print(f"Your enemy: {enemy}:Hp: {stats[0]} attact: {stats[1]}")
        
        while True:
            print(f"Your HP: {playerRole[0]} \nYour enemy Hp: {stats[0]}")
            print(f"1.{playerRole[2]}\n2.{playerRole[3]}\n3.{playerRole[4]}")
            userAttack = int(input("Enter number of Attack (1-3): "))
            if userAttack not in [1, 2, 3]:
                print("Invalid attack number")
                continue
            enemyAttack = random.randint(1, 3)
            if (userAttack == 1 and enemyAttack == 2) or(userAttack == 2 and enemyAttack == 3) or(userAttack == 3 and enemyAttack == 1):
                stats[0] -= playerRole[1]
                print(f"You hit the enemy with {playerRole[userAttack + 1]}!")
                
                
            elif (userAttack == 1 and enemyAttack == 3) or (userAttack == 3 and enemyAttack == 2) or (userAttack == 2 and enemyAttack == 1):
                
                playerRole[0] -= stats[1]
                print(f"Enemy hits you with {stats[enemyAttack + 1]}!")
            
            
            else:
                print("Both launch the same attack. No damage")
            if stats[0] <= 0:
                playerRole[0] = health + 30
                health= playerRole[0]  
                playerRole[1] = attack + 10
                attack=playerRole[1]
                print(f"You won! Your HP increases to {playerRole[0]} and Attack to {playerRole[1]}")
                break 
            elif playerRole[0] <= 0:
                print("You lost!")
                break
        if playerRole[0] <= 0: 
            break 
                
    print("Congratulations! You defeated all enemies.")

battle_ground()