#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
dna_com = ''

for i in range(len(dna)):
    if dna[-1-i] == 'A':
        dna_com += 'T'
    elif dna[-1-i] == 'T':
        dna_com += 'A'
    elif dna[-1-i] == 'C':
        dna_com += 'G'
    elif dna[-1-i] == 'G':
        dna_com += 'C'
    else:
        pass

print(dna_com)


"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
