#!/usr/bin/env python3

# Create a program that generates random sequences in FASTA format
# Each name should be unique
# Length should have a minimum and maximum
# GC% should be a parameter
# Use assert() to check bounds of command line values
# When creating sequences, append and join
# Command line:
#	python3 rand_seq.py <# of seqs> <min> <max> <gc>

import random
import sys

num_of_seq = int(sys.argv[1])
assert((num_of_seq) > 0)
min_seq = int(sys.argv[2])
assert(min_seq > 0)
max_seq = int(sys.argv[3])
assert(max_seq > 0)
gc_content = float(sys.argv[4])
assert(0 <= gc_content <= 1)

my_file = open('random.fasta', 'w')
for i in range(num_of_seq):
    print(('seq-%d' % (i)))
    my_file.write(('seq-%d' % (i)) + '\n')
    sequence = []
    length = random.randint(min_seq, max_seq)
    num_of_GC = int(round(gc_content*length))
    for l in range(length-(num_of_GC)):
        sequence.append(''.join(random.choice('AT')))
    for l in range(num_of_GC):
        sequence.append(''.join(random.choice('CG')))
    random.shuffle(sequence)
    sequence = ''.join(sequence)
    my_file.write(sequence + '\n')
    print(sequence)

my_file.close()

"""
python3 rand_seq.py 3 10 20 0.5
>seq-0
GCGCGACCTTAT
>seq-1
ATCCTAGAAGT
>seq-2
CTTCGCTCGTG
"""

