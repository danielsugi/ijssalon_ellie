#Hw_Les8_vraag_1_2
def mijn_functie_1(a):
    for i in list(a):
        print(i ** 2)
mijn_functie_1(a = [2,4,10,12])

#Hw_Les8_vraag_1_3
def mijn_functie_2(*korte_lijst):
    for i in list (korte_lijst):
        print([(i[0]+i[1]),(i[0]-i[1]),(i[0]*i[1]),(i[0]/i[1])])