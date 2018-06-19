def getDistanceBetweenPatternAndStrings(pattern, sequences):
  k = len(pattern)
  result = 0
  for sequence in sequences:
    distance = float("inf")
    for i in range(len(sequence)-k+1):
      temp = 0
      kmer = sequence[i:i+3]
      for a,b in zip(pattern, kmer)
        if a != b:
          temp = temp + 1
      if temp < distance:
        distance = temp
    result = result + distance
  return result
 
def main():
  pattern = "AAA"
  dna = ["AAATTTT", "AAACCCC", "AAAGGGG"]
  distance = getDistanceBetweenPatternAndStrings(pattern, dna)
  print(distance)
 
main()
