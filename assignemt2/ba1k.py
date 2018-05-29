# Funktion patternToNumber wie in Aufgabe 1 erläutert
def symbolToNumber(symbol):
  switch = {
    "A" : 0,
    "C" : 1,
    "G" : 2,
    "T" : 3}
  return switch.get(symbol) 

def patternToNumber(pattern):
  result = symbolToNumber(pattern[-1])
  if (len(pattern) > 1):
    result += 4*patternToNumber(pattern[0:-1])
  return result

# Funktion numberToPattern wie in Aufgabe 2 erläutert
def numberToSymbol(number):
  switch = { 
    0 : "A",
    1 : "C",
    2 : "G",
    3 : "T"}
  return switch.get(number)

def numberToPattern(number,kmer):
  patternsymbol = ""
  basis = 4 
  for i in range(kmer,0,-1):
    if(number > 3):
      symbol = numberToSymbol(number % basis) 
    else:
      symbol = numberToSymbol(number) 
    temp = int(number/basis) 
    patternsymbol += symbol    
    number = temp  
  return patternsymbol[::-1]

frequencyArray = [] #Definition vom frequencyArray

def fasterFrequentWords(text,k): #Definition der Funktion fasterFrequentWords mit Parametern text und k
  frequentPatterns = [] #Definition des Arrays frequentPattern
  frequencyArray = computeFrequencies(text,k) #Aufruf der Funktion computeFrequencies mit Parametern text und k & Speichern des Rückgabewertes in frequencyArray   
  maxCount = max(frequencyArray) #Heraussuchen des größten Wertes in frequencyArray 
  for i in range(4**k): #Einrichtung der For-Schleife von 0 bis 4^k
    if frequencyArray[i] == maxCount: #wenn im frequencyArray an Stelle i der Wert gleich dem maxcount ist...
      pattern = numberToPattern(i,k) #...dann berechne das pattern zu dem index i...
      frequentPatterns.append(pattern) #...und füge es zum frequentPattern Array hinzu
  return frequentPatterns #gebe frequentPattern als Rückgabewert zurück

def computeFrequencies(text,k): #Definition der Funktion computeFrequencies mit Parametern text und k
  for i in range(4**k): #Einrichtung der for-Schleife von 0 bis 4^k
    frequencyArray.append(0) #füge im frequencyArray an der Stelle i den Wert 0 ein
  for i in range(len(text)-1): #Einrichtung der for-Schleife von 0 bis Länge des Eingabewertes text
    pattern = text[i:i+k] #Abschnitt mit der Länge k beginnend bei Index i aus text in pattern schreiben
    j = patternToNumber(pattern) #von pattern den entsprechenden Zahlenwert berechnen und in j schreiben
    frequencyArray[j] = frequencyArray[j] + 1 #Wert an der Stelle i im frequencyArray um eins erhöhen
  return frequencyArray #frequencyArray als Rückgabewert zurückgeben

result=(fasterFrequentWords("ACGCGGCTCTGAAA",2)) #Aufruf der Funktion fasterFrequentWords mit Parametern text und k
print(result) #Ergebnis asugeben
