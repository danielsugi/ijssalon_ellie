import csv
from presentatie import *

inkomsten = {"Aardbeien-ijs-totaal":1000,"Vanille-ijs-totaal":2000,"Chocolade-ijs-totaal":1500,"Waterijsjes-totaal":750}

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])
        print (key, ":", value, "euro")

totaal_inkomsten = presenteer (inkomsten)

onderstreep = ("="*25)

print (onderstreep)
print ("totaal :",presenteer(inkomsten), "euro")