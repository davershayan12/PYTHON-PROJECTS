def player()->list:
    roles={"worrior":[110,20,"Dimention Strike","iron Slash","Defence"],"archer":[100,30,"Fire Arow","Multiple Arrow","Defence"],"dagger":[90,40,"One Point Slash","Back slash","Defence"]}
    print("Enter your role")
    for  role,stats in roles:
        print(f"{role}:\n HP: {stats[0]}\n Atack power:{stats[1]}\n 1.Attack:{stats[2]}\n 2.Attack:{stats[3]}\n 4.{stats[4]}")
    role:str=input()
    player:list=roles[role]
    return player
    