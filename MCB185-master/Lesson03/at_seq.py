#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

length = 30
content = 0
dna = ''
for i in range(length):
    r = random.randint(1, 4) # generate a random number from 1 to 4
    if   r == 1:
        dna += 'A'
        content += 1
    elif r == 2:
        dna +='C'
    elif r == 3:
        dna += 'G'
    elif r == 4:
        dna += 'T'
        content += 1

print(length, (content/length), dna)



"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
