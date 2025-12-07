import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('7.txt', mode='r') as f:
    text = f.read().strip().split('\n')

for i in range(len(text)-1, 0, -2):
    del text[i]

splits = [list(map(lambda x: x == '^', t)) for t in text[1:]]

# part 1
answer = 0

beams = list(map(lambda x: x == 'S', text[0]))

for s in splits:
    for i in range(len(s)):
        if s[i] and beams[i]:
            beams[i-1] = True
            beams[i] = False
            beams[i+1] = True
            answer += 1

print('Part 1:', answer)

# Part 2
answer = 0

timelines = list(map(lambda x: 1 if x == 'S' else 0, text[0]))

for s in splits:
    for i in range(len(s)):
        if s[i] and timelines[i] != 0:
            timelines[i-1] += timelines[i]
            timelines[i+1] += timelines[i]
            timelines[i] = 0

print('Part 2:', sum(timelines))