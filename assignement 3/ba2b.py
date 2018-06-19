def numberToSymbol(number):#Funktion definieren input Zahl, output Buchstabe bzw. String
  switch = { #Switch funktion wie bereits erl�utert
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"}
  return switch.get(number)


def numberToPattern(number,kmer):#Definition numberToPattern mit dazugeh�rigen Parametern
  patternsymbol = ""
  for i in range(kmer,0,-1):#Einrichtung der For-Schleife mit besonderer Bedingung, dass i von kmer bis 0 geht 
    temp = int(number/4) #Zwischenspeichern in Variable, Umrechnung in Dezimalsystem
    if(number > 3):#Bedingung wenn Zahl gr��er als 3, dann....
      symbol = numberToSymbol(number % 4)#.. Modula von number mit kmer bzw. 4 und anschlie�end Umwandlung des Rests in Symbol mit numberToSymbol Funktion
    else:#wenn Bedinung nicht zutreffend bitte dies durchf�hren
      symbol = numberToSymbol(number)#direkte Zuordnung des Symbol zur number, da number kleiner oder gleich 3 ist
    patternsymbol += symbol#hinzuf�gen des Buchstabens zu Patternsymbol 
    number = temp # damit number nicht unver�ndert bleibt, muss diese aktualisiert werden, damit im n�chsten Durchlauf das Ergebnis der Division verwendet wird           
  return patternsymbol[::-1]#Ausgabe patternsymbol, sonst Funktion keinen output


def medianstring(k,sequences):#Funktion definieren
  allkmers = [0] * (4**k)#array mit gew�nschter Gr��e erstellen
  for i in range (0,4**k):#Schleife von 0 bis 4**k              
    allkmers[i] = numberToPattern(i, k)#Ergebnis der numberToPattern Funktion in allkmers speichern
  lowestDistance = float("inf")#Definition der lowestDistance auf unendlich f�r den ersten Durchlauf,damit erstes Ergebnis auf jeden Fall als lowestDistance definiert wird
  distances = {}#definition distances als dictionary
  for kmer in allkmers: #Einrichtung der Schleife f�r die kmere in allkmers   
    result = 0   
    for sequence in sequences:#Schleife f�r jedes erstelle kmer in den sequences 
      distance = float("inf")      
      for i in range(len(sequence)-k+1):#Schleife f�r die sequence, um jedes kmer innerhalb der sequence zu �berpr�fen       
        temp = 0
        seqKmer = sequence[i:i+k]#kmer aus der sequence
        for a,b in zip(kmer, seqKmer):#Schleife f�r i Durchl�ufe f�r die jeweiligen Elemente aus kmer und seqKmer    
          if a != b:#falls a ungleich b...
            temp = temp + 1 #erh�he temp um 1     
        if temp < distance:#wenn temp kleiner distance
          distance = temp#definition von distance als temp f�r den n�chsten Durchlauf    
      result = result + distance #Ergebnis   
    if result < lowestDistance:#wenn Ergebnis result kleiner als lowestDistance
      lowestDistance = result#lowestDistance gleich result, um immer die kleinste distance zu haben   
    distances[kmer] = result #speichern in distances
  return min(distances,key = distances.get)#return des kleinsten Wertes von distances

  
k = 3#l�nge kmer
sequences = ["AAATTGACGCAT",
"GACGACCACGTT",
"CGTCAGCGCCTG",
"GCTGAGCACCGG",
"AGTACGGGACAG"]#input der Sequences

result = medianstring(k,sequences)#output in results speichern
print(result)#ausgabe des results