#!/usr/bin/env python3

import gzip
import sys

# Write a program that computes typical stats for sequence files
# See below for command line and output

genes = {}
bases = ['A', 'C', 'G', 'T']
with gzip.open('transcripts.fasta.gz', 'rt') as fp:
    for line in fp.readlines():
        #print(line)


        if line.startswith('>'):
            #genes[line.replace('\n','')] = ''
            name = line.replace('\n','')
            seq = ''
        else:
            print(seq)
            seq = seq + line.replace('\n', '')
            #seq.append(line.replace('\n', ''))

            genes[name] = seq


for g in genes.keys():
    print(g)
    print(genes[g])

#print(genes)
                #print(c)
        #print(l)
        #snps.append(l[0].replace('\n', ''))

#print(genes)


"""

print('Count:', len(genes))
print('Total:')
print('Min')
print("Max")
print('Mean')
print(NTs)
python3 fasta_stats.py transcripts.fasta.gz
Count: 232
Total: 278793
Min: 603
Max: 1991
Mean: 1201.7
NTs: 0.291 0.218 0.210 0.281
"""
