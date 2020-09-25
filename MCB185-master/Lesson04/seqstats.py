#!/usr/bin/env python3

import fileinput

# Write a program that computes typical sequence stats
# No, you cannot import any other modules!
# Use rand_seq to generate the sequences
# Expected output is shown below

data = []
number_of_seq = 0
number_of_letters = 0
A = 0
C = 0
G = 0
T = 0
for line in fileinput.input():
    #if line[0] == '#': continue # skip over comments
    if line.startswith('seq'):
        number_of_seq += 1 # same as above
    if line.startswith(('A', 'T', 'C', 'G')):
        line = line.rstrip() # remove newline (return character), often useful
        data.append((line)) # store the data

        number_of_letters += len(line)
        for i in line:
            if i == 'A':
                A += 1
            elif i == 'C':
                C += 1
            elif i == 'G':
                G += 1
            elif i == 'T':
                T += 1

data_sorted = sorted(data, key=len)

reverse_data_sorted = sorted(data, key=len, reverse = True)
half = int(round(number_of_letters/2))
running_sum = 0

for i in range(len(reverse_data_sorted)):
    running_sum += len(reverse_data_sorted[i])
    if running_sum < half:
        #print(reverse_data_sorted[i])
        #print(running_sum)
        #print(half)
    else:
        N50 = reverse_data_sorted[i]
        #print(N50)
        #print('reverse', len(reverse_data_sorted[i]))
        break



print('Number of sequences:', number_of_seq)
print('Number of letters:', number_of_letters)
print('Minimum length:', len(data_sorted[0]))
print('Maximum length:', len(data_sorted[-1]))
print('N50:', len(N50))
print('Composition:', 'A:', f'{A/number_of_letters:.3f}', 'C:', f'{C/number_of_letters:.3f}',
       'G:', f'{G/number_of_letters:.3f}', 'T:', f'{T/number_of_letters:.3f}')




"""
python3 rand_seq.py 100 100 100000 0.35 | python3 seqstats.py
Number of sequences: 100
Number of letters: 4957689
Minimum length: 219
Maximum length: 99853
N50: 67081
Composition: A=0.325 C=0.175 G=0.175 T=0.325
"""
