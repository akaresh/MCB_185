#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'


list_codons = []

for i in range (0, len(dna),3):
    splitting = dna[i:i+3]
    list_codons.append(splitting)

print(list_codons)
print(len(list_codons))
"""
python3 codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
