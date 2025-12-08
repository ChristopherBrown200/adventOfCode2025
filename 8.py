import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('8.txt', mode='r') as f:
    text = f.read().strip().split('\n')

points = [list(map(int, t.split(','))) for t in text]
print(points)

def calDis(a: list[int, int, int], b: list[int, int, int]) -> float:
    x = math.abs(a[0] - b[0])
    y = math.abs(a[1] - b[1])
    z = math.abs(a[2] - b[2])

    return math.sqrt(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))

# part 1
answer = 0

print('Part 1:', answer)

# Part 2
answer = 0

print('Part 2:', answer)