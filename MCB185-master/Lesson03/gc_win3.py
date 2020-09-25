#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Step size is 5 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
s = 5

for i in range(0, len(seq), s):
    stripped = seq[i:i+w]
    if len(stripped) == 11:
        gc_content = 0
        for j in range(len(stripped)):
            if stripped[j] == 'C' or stripped[j] == 'G':
                gc_content += 1
            else:
                continue
        print(i, stripped, f'{gc_content/11:.4f}')
    else:
        break

"""
python3 gc_win3.py
0 ACGACGCAGGA 0.6364
5 GCAGGAGGAGA 0.6364
10 AGGAGAGTTTC 0.4545
15 AGTTTCAGAGA 0.3636
20 CAGAGATCACG 0.5455
25 ATCACGAATAC 0.3636
30 GAATACATCCA 0.3636
35 CATCCATATTA 0.2727
40 ATATTACCCAG 0.3636
45 ACCCAGAGAGA 0.5455
"""
