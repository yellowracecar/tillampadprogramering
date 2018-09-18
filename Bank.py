print("Välkommen till banken")
print("1. Sätta in")
print("2. Ta ut")
print("3. Saldo")
print("4. Hejdå")

saldo = 0
meny = 0
while meny != 4:
    try:
        meny = int(input("Välja vad du vill göra i menyn "))
    except:
        print("du måste välja en siffra")
    if meny == 1:
        try:
            saldo = saldo + int(input("Hur mycket vill du sätta in? "))
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
        print(saldo)
    elif meny == 4:
        print("Hejdå")

    