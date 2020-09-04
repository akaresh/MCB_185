#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math
import sys


A = 0

data = []
for line in fileinput.input():
    #assert (fileinput.input() != '')
    if line.startswith('#'):
        continue
    line = line.rstrip()
    l = line.split(' ')
    #print(l)
    data.append(float(l[1]))
for i in data:
    A = A - (i*math.log2(i))

print(f'{A:.3f}')
'''
x = 0
for char in data[x]:
    if char.isalpha() == True:
        if char == 'A':
            pass
        elif char == 'T':
        elif char == 'G':
        elif char == 'C':
    else:
        print('num:', char)


print(data)
'''
"""
python3 entropy.py nucleotides.txt
1.846
"""
