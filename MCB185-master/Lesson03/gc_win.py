#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11

#gc_content = [0]

for i in range(len(seq)):
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

#print(i, stripped, f'{gc_content/11:.4f}')




"""
list_of_all = []
gc_content = []

for i in range(len(seq)):
    stripped = seq[i:i+w]
    if len(stripped) == 11:
        list_of_all.append(stripped)
    else:
        break


for i in range(len(list_of_all)):
    gc_content.append(0)
    for j in range(len(list_of_all[i])):
        if list_of_all[i][j] == 'C' or list_of_all[i][j] == 'G':
            gc_content[i] += 1

    print(i, list_of_all[i], f'{gc_content[i]/11:.4f}')
"""


'''
for j in range(len(seq)):
    num_of_gc = 0
    for i in range(len(seq[j:j+w])):
        if seq[i] == 'C' or seq[i] == 'G':
            num_of_gc += 1
        else:
            pass
print(j, seq[j:j+w],num_of_gc)
'''


"""
python3 gc_win.py
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
