import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('2.txt', mode='r') as f:
    ids = f.read().strip().split(',')

# part 1
answer = 0

for interval in ids:
    a, b = map(int, interval.split('-'))
    for id in range(a, b+1):
        string = str(id)
        if len(string) % 2 == 1: continue
        if string[:len(string)//2] == string[len(string)//2:]: answer += id

print('Part 1:', answer)

# Part 2
answer = 0

for interval in ids:
    a, b = map(int, interval.split('-'))
    for id in range(a, b+1):
        string = str(id)
        for i in range(1, len(string)//2 + 1):
            sequence = string[0:i]
            if string.count(sequence) == len(string) / len(sequence):
                answer += id
                break

print('Part 2:', answer)