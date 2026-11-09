#ord som söks
första_ord = "SLÄKTNING"
ord = []
for i in range(len(första_ord)):
    ord.append(första_ord[i])
#ord fast dolt, skrivs ut till användare med * 
nuvarande_dolt_ord = []
for i in range(len(ord)):
    nuvarande_dolt_ord.append("*")
hemligt = "".join(nuvarande_dolt_ord)

antal_felgissning = 9
felgissningar = ""
hittat_en_bokstav = False

#huvudloop
while nuvarande_dolt_ord != ord and antal_felgissning != 0:
    #input setup
    print("Du ska gissa ett ord, bokstav för bokstav, på 9 bokstäver")
    gissning = input("Ange en gissning -> ")
    
    #giltighetscheckar gissning
    if len(gissning) > 1:
        print("Ogiltig gissning")
        continue
    
    #checkar gissning genom att gå igenom varje bokstav i ordet
    for i in range(len(ord)):
        if gissning == ord[i]:
            nuvarande_dolt_ord[i] = gissning
            hittat_en_bokstav = True
            hemligt = "".join(nuvarande_dolt_ord)
    #kollar om vi hittat åtminstone en bokstav        
    if hittat_en_bokstav == False:
            print("Hittat_bokstav == false")
            antal_felgissning += -1
            felgissningar += gissning
    print("Du har nu", antal_felgissning, "st. felgissningar kvar.")
    print("Felgissningar: ", felgissningar)
    print(hemligt)
    print("")
    hittat_en_bokstav = False

if antal_felgissning == 0:
    print("Du fick slut på gissningar")
else:
    print(ord)
    print(nuvarande_dolt_ord)

    
    
    
#saker att göra:
#avslutning
#checkning av gissning: Nummer, gissat bokstav innan, liten bokstav ska bli stor bokstav
