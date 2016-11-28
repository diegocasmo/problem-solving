# Problem: http://rosalind.info/problems/rna/

def solution(dna_string):
  rna_string = []
  for index, char in enumerate(dna_string):
    if char == 'T':
      rna_string = rna_string +  ['U']
    else:
      rna_string = rna_string + [char]
  return ''.join(rna_string)
