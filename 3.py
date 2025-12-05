import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

def findMaxJoltage(batts: int, size: int) -> str:
    if size == 1:
        return str(max(batts))

    a = max(batts[:-1 * (size-1)])
    remaining = batts[batts.index(a)+1:]
    return f'{a}{findMaxJoltage(remaining, size-1)}'


with open('3.txt', mode='r') as f:
    banks = f.read().strip().split('\n')

# part 1
answer = 0

for b in banks:
    batts = list(map(int, list(b)))
    a = max(batts[:-1])
    b = max(batts[batts.index(a)+1:])
    answer += int(f'{a}{b}')

print('Part 1:', answer)

# Part 2
answer = 0

for b in banks:
    batts = list(map(int, list(b)))
    a = max(batts[:-1])
    b = max(batts[batts.index(a)+1:])
    answer += int(findMaxJoltage(batts, 12))


print('Part 2:', answer)