def symbolToNumber(symbol): #Funktion definieren symbolToNumber
  switch = { # Switch einrichten für Austausch von Symbol zu Zahl
    "A" : 0,
    "C" : 1,
    "G" : 2,
    "T" : 3}
  return switch.get(symbol) #Return des Outputs

def patternToNumber(pattern): #Definition der patternToNumber Funktion
  result = symbolToNumber(pattern[-1])#Anwendung der symbolToNumber Funktion auf letzten Teil des Strings
  if (len(pattern) > 1):#Bedingung wenn Länge des Strings über 1..
    result += 4*patternToNumber(pattern[0:-1])#..rekursives Aufrufen der Funktion patterntonumber mit Faktor 4, dadurch entstehen die Potenzen
  return result#Ouput

print(patternToNumber("AGT"))#Ausgabe des Results

