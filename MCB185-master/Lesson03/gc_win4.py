#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops (as in gc_win2.py)

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5

import re
gc_content = 0

for j in range(w):
    if seq[j] == 'G' or seq[j] == 'C':
        gc_content += 1
print(f'0 {seq[:w]} {gc_content/w:.4f}')

for i in range(s, len(seq)-w+1, s):
    gc_content -= seq.count('G',i-s, i) + seq.count('C', i-s, i)
    #print(seq[i-s:i])
    gc_content += seq.count('G', i+w-s, i+w) + seq.count('C', i+w-s, i+w)
    #print(seq[i+w-s:i+w])

    #stripped = seq[i:i+w]

    #gc_content = len(re.findall('C|G', stripped))
    print(i, seq[i:i+w], f'{gc_content/w:.4f}')


"""
python3 gc_win4.py
0 ACGAC GCAGGA 0.6364
5 GCAGGA GGAGA 0.6364
10 AGGAGAGTTTC 0.4545
15 AGTTTCAGAGA 0.3636
20 CAGAGATCACG 0.5455
25 ATCACGAATAC 0.3636
30 GAATACATCCA 0.3636
35 CATCCATATTA 0.2727
40 ATATTACCCAG 0.3636
45 ACCCAGAGAGA 0.5455
"""
