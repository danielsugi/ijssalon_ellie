from algemene_functies import mijn_functie_2

#Hw_Les8_vraag_1_5
def aanbieding_1(smaak, prijs, korting):
    x = prijs * korting
    korting = prijs - x
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    return uitvoer
    
print (aanbieding_1("aardbei", 4, 0.1))

#Hw_Les8_vraag_1_6_en_1_7
def inkomsten_totaal(inkomsten):
	
    x = sum (inkomsten)
    y = float (x * 0.09)
    
    uitvoer = f"Het totaal van alle inkomsten van deze week is {x} euro, waarover {y} euro btw betaald dient te worden."
    return uitvoer

print (inkomsten_totaal(inkomsten = [220, 430, 125, 160, 205, 90, 345]))

#Hw_Les8_vraag_1_8
def laag_en_hoog(mijn_lijst):
    x = max(mijn_lijst)
    y = min(mijn_lijst)
    return x, y

print (laag_en_hoog(mijn_lijst = [220, 430, 125, 160, 205, 90, 345]))

#Hw_Les8_vraag_1_9 en_1_10
def gemiddelde(mijn_lijst):
	return sum(mijn_lijst) / len(mijn_lijst)
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
x = gemiddelde(mijn_lijst)
print("De gemiddelde inkomsten deze week zijn",round (x),"euro.")

#Hw_Les8_vraag_1_11
def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer
    
def laag_en_hoog(invoer_lijst):
    x = max(invoer_lijst)
    y = min(invoer_lijst)
    return x, y
print (meervoudig(invoer_lijst = ([10,5,3,2,1,2,9])))

#Hw_Les8_vraag_1_12

def laag_en_hoog(invoer_lijst_2):
    x = max(invoer_lijst_2)
    y = min(invoer_lijst_2)
    return x, y

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

combinatie(invoer_lijst_2=([12,3],[12,2],[10,5],[100,20]))