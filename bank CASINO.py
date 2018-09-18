print("Välkommen till banken")
print("1. Casino")
print("2. Ta ut")
print("3. Sätta in")
print("4. Saldo")
print("5. Hejdå")


saldo = 0
meny = 0
while meny != 5:
    try:
        meny = int(input("Välj vad du vill göra i menyn "))
    except:
        print("du måste välja en siffra")
    if meny == 1:
        try:
            insats = int(input("Välkommen till casinot!, hur mycket vill du lägga in? "))
            saldo = saldo - insats
            tal = int(input(" Gissa på ett tal mellan 1 - 2. Rätt = du dubblar din insats, Fel = Du förlorar hälften av din insats "))
            import random
            x = random.randint(1,2)
            if tal == x:
                print("rätt nummer var", x)
                insats = insats * 2
                print("du vann")
                saldo = saldo + insats
            else:
                print("rätt nummer var", x)
                insats = 0
                print("du förlora")
        except:
            print("du måste välja en siffra")
    elif meny == 2:
        try:
            uttag = int(input("Hur mycket vill du ta ut? "))
            print("du tog ut", str(uttag))
            saldo = saldo - uttag
        except:
            print("du måste välja en siffra")
    elif meny == 3:
        try:
            saldo = saldo + int(input("Hur mycket vill du sätta in? "))
        except:
            print("du måste välja en siffra")
    elif meny == 4:    
        print(saldo)
    elif meny == 5:
        print("Hejdå")
    else: 
        print("Du måste välja 1,2,3,4 eller 5")