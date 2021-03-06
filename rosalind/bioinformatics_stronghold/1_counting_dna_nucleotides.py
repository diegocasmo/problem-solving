# Problem: http://rosalind.info/problems/dna/

def solution(dna_string):
  symbols = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
  valid_symbols = symbols.keys()
  for element in dna_string:
    if element in valid_symbols:
      symbols[element] += 1
  return "%s %s %s %s" % (symbols['A'], symbols['C'], symbols['G'], symbols['T'])
