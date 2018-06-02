def symbolToNumber(symbol):#Definition der benötigen Funktion
  switch = { #bereits beschriebene Switch Funktion, welche für die Umwandlung von A,C,G,T in Integers verwendet wird
    "A" : 0,
    "C" : 1,
    "G" : 2,
    "T" : 3}
  return switch.get(symbol)

def patternToNumber(pattern): #Definition der patternToNumber Funktion 
  result = symbolToNumber(pattern[-1])#Anwendung von symbolToNumber auf die letzte Stelle des pattern mit Hilfe des -1 index
  if (len(pattern) > 1):#wenn Länge des pattern >1, dann....
    result += 4*patternToNumber(pattern[0:-1])#... rekursives Aufrufen der Funktion mit Faktor, welcher durch den wiederholten Aufruf zur gewünschten Potenz führt. Hinzufügen zum result
  return result#Ausgabe result als output

def numberToSymbol(number):#Definition des numberToSymbol
  switch = { #Switch funktion, wie bereits erläutert
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"}
  return switch.get(number)

def numberToPattern(number,kmer):#defintion numberToPattern
  patternsymbol = ""
  for i in range(kmer,0,-1): #Einstellung der for Schleife. i soll von kmer bis 0 gehen, daher Zusatz -1
    temp = int(number/4) #division der number durch kmer, erster Schritt zur Umwandlung ins gewünschte Zahlensystem. In diesem Fall 4er System
    if(number > 3): #wenn number größer 3...
      symbol = numberToSymbol(number % 4) #Modula von number mit kmer mit anschließender Anwendung der numberToSymbol Funktion. 
    else: #sonst ...
      symbol = numberToSymbol(number) #direkte Anwendung der numberToSymbol Funktion, da sich number bereits im definierten Bereich befindet    
    patternsymbol += symbol #Hinzufügen des symbols zu patternsymbol
    number = temp #Aktualisierung von number durch das Ergebnis der Divison
  return patternsymbol[::-1] #Ausgabe des patternsymbol

def countkmers(kmers,sequence,length):#Definition der Funktion countkmers mit den Parametern kmer, sequence, length
  for i in range (0, len(sequence)-length+1):#Einrichtung der For-Schleife
    x = sequence[i:i+length]#Abschnitt mit der Länge length aus sequence
    kmers[patternToNumber(x)] += 1#Anwendung des patternToNumber auf den Sequenzabschnitt und Erhöhung des Values um 1
  return kmers#Ausgabe von kmers

def main():
  input = "ACGCGGCTCTGAAA"#Sequence
  kmer = 2 #Länge des kmer
  for i in range (4**kmer): #Schleife, welche die Anzahl aller potentiellen k-mere der Länge kmer durchgeht
    frequencyArray[i] = 0 # frequencyArray soll die Größe der Anzahl der k-mere besitzen
  result = countkmers(frequencyArray,input,kmer) #Anwendung der countkmers Funktion mit den gegebenen Parametern, welche mit den Parametern von countkmers gemapped werden
  print("k-mer","index","frequency") #Ausgabe des kmer, index, frequency
  for i in frequencyArray: #Einrichtung For Schleife für frequencyArray
    print(numberToPattern(i,kmer),i,frequencyArray[i]) #Ausgabe des umgekehrten spezifischen kmers zum index des frequencyArray 


frequencyArray = {} #Erstellung des Dictionary
main()
