def getDistanceBetweenPatternAndStrings(pattern, dna):
  k = len(pattern)
  result = 0
  for text in dna:  #Schleife, für jeden DNA String aus der Liste
    distance = float("inf") #initialisiere distance mit 'unendlich' damit beim ersten Durchlauf temp garantiert kleiner ist    
    for i in range(len(text)-len(pattern)+1): #Schleife enimal durch den DNA String (aber nur so weit, dass noch eine 3-lange Sequenz erstellt werden kann)
      temp = 0
      dnaSequence = text[i:i+3] #Sequenz aus dna String rausnehmen
      for a,b in zip(pattern, dnaSequence): #gehe durch Sequenz und Pattern
        if a != b: #wenn pattern und dnaSequence an der selben Stelle nicht den selben Wert haben, dann...
          temp = temp + 1 #erhöhe temp um eins
      if temp < distance: #wenn temp kleiner als die distance, dann...
        distance = temp #überschreibe distance mit der neuen temp
    result = result + distance #füge alle distances zum result hinzu
  return result #gebe result zurück

def main():
  pattern = "AAA"
  dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
  distance = getDistanceBetweenPatternAndStrings(pattern, dna) #führe Funktion aus und speichere Ergebnis in distance
  print(distance)

main()

