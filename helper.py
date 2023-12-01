def onderstreep(tekst=""):    
    uit = []    
    uit.append(tekst)    
    uit.append(len(tekst) * "=")    
    return uit

def som(x):
    x = sum (x.values())
    return x 