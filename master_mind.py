#Bulls and Cows
import random

while True:
    #Skappa hemliga koden med random
    hemlig_kod = []
    for tal in range(4):
        hemlig_kod.append(random.randint(0,9))
    print(hemlig_kod)
    for x in range(10):
        #Gissa 4 siffror
        gissa = []
        for tal in range(4):
            gissning = int(input("Gissa tal"+str(tal+1)+": "))
            gissa.append(gissning)
            
        #Jämföra om de är på rätt plats
        #eller om de finns i men på fel plats
        #Skapa rad
        print("Gissning:", gissa)
        for i in range(4):
            if hemlig_kod[i]==gissa[i]:
                gissa[i] = "B"
            elif hemlig_kod.count(gissa[i]) > 0:
                gissa[i] = "C"
            else:
                gissa[i] = "G"
        print("Gissning:", gissa)
        if gissa.count("B") == 4:
            break
    if gissa.count("B") == 4:
        print("Du har vunnit")
    else:
        print("Du har förlorat efter 10 försök")
        
    val = input("Spela igen? J/N".upper())
    if val== "J":
        print("Hej då")
        break
