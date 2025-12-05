import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('5.txt', mode='r') as f:
    ranges, all = f.read().strip().split('\n\n')

ranges = ranges.split('\n')
ranges = [list(map(int, r.split('-'))) for r in ranges]
all = list(map(int, all.split('\n')))

# part 1
answer = 0

fresh = set()

for a, b in ranges:
    if a == b:
        if a in all : fresh.add(a)
        continue

    if a in all:
        removeA = True
        fresh.add(a)
    else:
        all.append(a)

    if b in all:
        removeB = True
        fresh.add(b)
    else:
        all.append(b)

    all.sort()
    fresh = fresh.union(set(all[all.index(a) + 1 : all.index(b)]))
    all.remove(a)
    all.remove(b)

print('Part 1:', len(fresh))

# Part 2
answer = 0
ranges.sort(key=lambda r: r[0])

i = 0
while i < len(ranges)-1:
    a, b = ranges[i]
    c, d = ranges[i+1]

    if b < c: 
        i += 1
        continue
    if b < d: 
        ranges[i][1] = d
    else:
        ranges[i][1] = b
    ranges.remove((ranges[i+1]))

for r in ranges:
    a, b = r
    answer += b - a + 1

print('Part 2:', answer)