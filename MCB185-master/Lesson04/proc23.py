#!/usr/bin/env python3

import fileinput

# Write a program that reads a 23andme file
# Report the number of SNPs successfully assayed
# Report the heterozygosity
# Report the failure rate
# https://opensnp.org/genotypes (make sure the data is 23andme)


"""
proc23.py whatever.23andme.whatever
"""

data = []
data_mt_DNA = []
for line in fileinput.input():
    if line[0] == '#':
        continue
    line = line.rstrip() # remove newline (return character), often useful
    l = line.split('\t')
    if l[1] != 'Y' and l[1] != 'MT':
        data.append(str(l[3]))
    if l[1] == 'MT':
        data_mt_DNA.append(str(l[3]))

#print(len(data))
mt_DNA = 0
failure_mt_DNA = 0
SNP = 0
failure = 0
heterozygosity = 0

for bps in data:
    #print(bps, len(bps))
    #try without .isalpha
    #if not '-' in bps:
    # check {A, C, G, T}
    if bps[0] != '-' or bps[1] != '-':
    #if bps.isalpha() is True:
        SNP += 1
        if bps[0] != bps[1]:
            heterozygosity += 1
        else:
            continue
    elif bps.isalpha() == False and len(bps) == 2: ###
        failure +=1

for b in data_mt_DNA:
    if b.isalpha() == True and len(b) == 1: ###
        mt_DNA += 1
    elif b.isalpha() == False and len(b) == 2: ###
        failure_mt_DNA += 1
print('SNP:', SNP, 'Failure:', failure, 'MT_DNA:', mt_DNA,
      'MT_DNA_Failure:', failure_mt_DNA, 'Heterozygous:', heterozygosity, "% Heterozygous:", heterozygosity/SNP)
#print(data)
    #data.append(float(line))
