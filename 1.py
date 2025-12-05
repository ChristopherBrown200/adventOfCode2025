import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('1.txt', mode='r') as f:
    instructions = f.read().split('\n')

# part 1
count = 0
curr = 50

for i in instructions:
    dir = -1 if i[0] == 'L' else 1
    change = dir * int(i[1:])
    curr += change
    curr %= 100
    if curr == 0: count += 1

print('Part 1:', count)

# Part 2
count = 0
curr = 50

for i in instructions:
    dir = -1 if i[0] == 'L' else 1
    change = int(i[1:])
    for _ in range(change):
        curr += dir
        curr %= 100
        if curr == 0: count += 1

print('Part 2:', count)