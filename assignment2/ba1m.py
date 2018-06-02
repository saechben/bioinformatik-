def numberToSymbol(number):#Funktion definieren input Zahl, output Buchstabe bzw. String
  switch = { #Switch funktion wie bereits erläutert
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"}
  return switch.get(number)

def numberToPattern(patternsymbol, number,kmer):#Definition numberToPattern mit dazugehörigen Parametern
  for i in range(kmer,0,-1):#Einrichtung der For-Schleife mit besonderer Bedingung, dass i von kmer bis 0 geht 
    temp = number/kmer#Zwischenspeichern in Variable, Umrechnung in Dezimalsystem
    if(number > 3):#Bedingung wenn Zahl größer als 3, dann....
      symbol = numberToSymbol(number % kmer)#.. Modula von number mit kmer bzw. 4 und anschließend Umwandlung des Rests in Symbol mit numberToSymbol Funktion
    else:#wenn Bedinung nicht zutreffend bitte dies durchführen
      symbol = numberToSymbol(number)#direkte Zuordnung des Symbol zur number, da number kleiner oder gleich 3 ist
    patternsymbol += symbol#hinzufügen des Buchstabens zu Patternsymbol 
    number = temp # damit number nicht unverändert bleibt, muss diese aktualisiert werden, damit im nächsten Durchlauf das Ergebnis der Division verwendet wird           
  return patternsymbol#Ausgabe patternsymbol, sonst Funktion keinen output
  
def main():#Definition der Main Funktion, damit es keine globalen Variablen gibt 
  kmer = 4#Länge des kmers
  number = 45#Zahl für ein bestimmtes pattern
  result = numberToPattern("",number,kmer)#parameter definieren, welche mit numbertopattern gemapped werden
  print(result[::-1])#Umkehrung des Strings damit dieser in richtiger Reihenfolge ist

main()#aufrufen der main Funktion
