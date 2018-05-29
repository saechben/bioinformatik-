def numberToSymbol(number):#Funktion definieren input Zahl, output Buchstabe bzw. String
  switch = { #Switch funktion wie bereits erl�utert
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"}
  return switch.get(number)

def numberToPattern(patternsymbol, number,kmer):#Definition numberToPattern mit dazugeh�rigen Parametern
  for i in range(kmer,0,-1):#Einrichtung der For-Schleife mit besonderer Bedingung, dass i von kmer bis 0 geht 
    temp = number/kmer#Zwischenspeichern in Variable, Umrechnung in Dezimalsystem
    if(number > 3):#Bedingung wenn Zahl gr��er als 3, dann....
      symbol = numberToSymbol(number % kmer)#.. Modula von number mit kmer bzw. 4 und anschlie�end Umwandlung des Rests in Symbol mit numberToSymbol Funktion
    else:#wenn Bedinung nicht zutreffend bitte dies durchf�hren
      symbol = numberToSymbol(number)#direkte Zuordnung des Symbol zur number, da number kleiner oder gleich 3 ist
    patternsymbol += symbol#hinzuf�gen des Buchstabens zu Patternsymbol 
    number = temp # damit number nicht unver�ndert bleibt, muss diese aktualisiert werden, damit im n�chsten Durchlauf das Ergebnis der Division verwendet wird           
  return patternsymbol#Ausgabe patternsymbol, sonst Funktion keinen output
  
def main():#Definition der Main Funktion, damit es keine globalen Variablen gibt 
  kmer = 4#L�nge des kmers
  number = 45#Zahl f�r ein bestimmtes pattern
  result = numberToPattern("",number,kmer)#parameter definieren, welche mit numbertopattern gemapped werden
  print(result[::-1])#Umkehrung des Strings damit dieser in richtiger Reihenfolge ist

main()#aufrufen der main Funktion
