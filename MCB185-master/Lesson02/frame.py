#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'


###single loop
print("single loop v1")
n = int(len(dna)/3)
frame = list(range(3))*n ###

for a in range(0, len(dna)):
    print(a, frame[a], dna[a])

print("single loop v2")
for a in range(0, len(dna)):
    n = a%3
    print(a, frame[n], dna[a])

###nested loop
print("nested loop")
x = 0
for i in range (0, len(dna), 3):
    for j in range(0, 3):
        print(i, j, dna[i])
        i+=1
        #break

"""
python3 frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""

