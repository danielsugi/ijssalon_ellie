prijzen = {
  "aardbei" : 3,
  "vanille" : 4,
  "chocolade" : 5
}
aanbieding = prijzen ["aardbei"] * 0.8

reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € "
reclame_tekst2 = (f"{reclame_tekst}{aanbieding}") [:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4 :
 if (len (el)) > 5:
  el= (el.upper())	
 else:
  el= (el.lower())
 print (el)