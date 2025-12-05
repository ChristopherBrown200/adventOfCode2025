import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

def countRolls() -> int:
    canReach = 0
    for r in range(rows):
        for c in range(columbs):
            if not paper[r][c]: continue
            count = -1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if r+i > -1 and r+i < rows and c+j > -1 and c+j < columbs and paper[r+i][c+j]: count += 1
            if count < 4: 
                canReach += 1
                paper[r][c] = False

    if canReach == 0:
        return canReach
    else:
        return canReach + countRolls()


with open('4.txt', mode='r') as f:
    text = list(map(list, f.read().strip().split('\n')))

paper = []

rows = len(text)
columbs = len(text[0])

for row in text: paper.append(list(map(lambda x: x== '@', row)))

# part 1
answer = 0

for r in range(rows):
    for c in range(columbs):
        if not paper[r][c]: continue
        count = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if r+i > -1 and r+i < rows and c+j > -1 and c+j < columbs and paper[r+i][c+j]: count += 1
        if count < 4: answer += 1


print('Part 1:', answer)

# Part 2
answer = 0

print('Part 2:', countRolls())