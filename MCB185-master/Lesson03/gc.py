#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

num_of_GC = 0
for i in range(len(dna)):
    if dna[i] =='G' or dna[i] == 'C':
        num_of_GC += 1
    else:
        pass

content = num_of_GC/len(dna)

print('%.2f' % (content))
print('{:.2f}'.format(content))
print(f'{content:.2f}')
"""
python3 gc.py
0.42
0.42
0.42
"""
