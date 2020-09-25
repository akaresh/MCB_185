#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>
from math import factorial
import random
import sys


days = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])
birthdays = []
probabilities = []
for i in range(trials):
    for x in range(people):
        birthdays.append(random.randint(1, days))
    if x in birthdays:
        probability = factorial(days)/(days**people*factorial(days-people))
        probabilities.append(probability)
    else:
        continue
print(birthdays)
#print(probabilities)
total = sum(probabilities)/len(probabilities)

print(total)

"""
python3 birthday.py 365 1000 23
0.520
"""

###two people having the same birthday

