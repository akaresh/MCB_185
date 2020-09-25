#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line:
#	python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>


"""
python3 rand_fasta.py 3 10 20 0.1 0.2 0.3 0.4
>seq-0
TCGTTTTGATTACGG
>seq-1
CGGCTGTTCCGTAATGC
>seq-2
TTTCGTGTACTTTCTAGTGA
"""


import gzip
import sys

def read_fasta(filename):
    name = None
    seqs = []

    fp = None
    if filename == '-':
        fp = sys.stdin
    elif filename.endswith('.gz'):
        fp = gzip.open(filename, 'rt')
    else:
        fp = open(filename)

    for line in fp.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            if len(seqs) > 0:
                seq = ''.join(seqs)
                yield(name, seq)
                name = line[1:]
                seqs = []
            else:
                name = line[1:]
        else:
            seqs.append(line)
    yield(name, ''.join(seqs))
    fp.close()



for name, seq in read_fasta('proteins.fasta.gz'):
    print(name, len(seq))
