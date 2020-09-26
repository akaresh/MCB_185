#!/usr/bin/env python3
#comments
from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

data = []
for line in fileinput.input():
    #if line[0] == '#': continue # skip over comments
    if line.startswith('#'):
        continue # same as above
    line = line.rstrip() # remove newline (return character), often useful
    data.append(float(line)) # store the data

mean = sum(data)/len(data)


total_sum = 0
for i in data:
    total_sum += (i-mean)**2
stdev = sqrt(total_sum/(len(data)))

data.sort()
print(data)
n = len(data)

if n % 2 == 0:
    median1 = data[n//2]
    median2 = data[n//2-1]
    total_median = (median2+median1)/2
else:
    total_median = data[n//2]


#print(data)

print('Count:', len(data))
print('Minimum:', min(data))
print('Maximum:', max(data))
print('Mean:', mean)
print('Std. dev:', f'{stdev:.3f}')
print('Median:', total_median)
"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
