import random
import operator

kmer_length = 8 # Länge des Kmers
seq_count = 5 # Anzahl der Sequenzen
seq_array = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
"GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
"TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
"TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
"AATCCACCAGCTCCACGTGCAATGTTGGCCTA"] # Array aller Sequenzen

def random_select(seq_array):
  kmer_array = [""] * seq_count
  for i in range(0,len(seq_array)):
    sequence = seq_array[i]
    rand = random.randint(0,len(sequence)-kmer_length)
    kmer = sequence[rand:rand+kmer_length]
    kmer_array[i] = kmer
  return kmer_array

def profile_creator(kmer_array):
  profile = {"A":[1]*kmer_length,
      "C": [1]*kmer_length,
      "G": [1]*kmer_length,
      "T": [1]*kmer_length}
  for j in range(0,kmer_length):
    for kmer in kmer_array:
      profile[kmer[j]][j] += 1/seq_count
      profile[kmer[j]][j] = round(profile[kmer[j]][j],1)
  return profile

def best_kmer(profile):
  motif = []
  for sequence in seq_array:
    best_kmer = ""
    best_probability = 0
    for k in range(0, len(sequence)-kmer_length+1):
      kmer = sequence[k:k+kmer_length]
      probability = 1
      for l in range(0,kmer_length):
        probability *= profile[kmer[l]][l]
        if (probability > best_probability):
          best_kmer = kmer
          best_probability = probability
    motif.append(best_kmer)
  return motif

def get_consensus(motif):
  consensus = ""
  for n in range(0, kmer_length):
    profile = {"A":0,
      "C": 0,
      "G": 0,
      "T": 0}
    for kmer in motif:
      profile[kmer[n]] += 1
    maxi = max(profile.items(), key=operator.itemgetter(1))[0]
    consensus += maxi
  return consensus

def get_score(motif, consensus):
  score = 0
  for o in range(0, kmer_length):
    for kmer in motif:
      if (consensus[o] != kmer[o]):
        score += 1
  return score

best_score = float('inf')
best_motif = random_select(seq_array)

for m in range(0, 1000):
  profile = profile_creator(best_motif)
  motif = best_kmer(profile)
  consensus = get_consensus(motif)
  score = get_score(motif, consensus)
  if (score < best_score):
    best_motif = motif
    best_score = score
  motif = random_select(seq_array)
print(best_motif)
