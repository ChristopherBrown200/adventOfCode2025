import hashlib
import math
import sys
from collections import Counter
sys.setrecursionlimit(10**6)

with open('6.txt', mode='r') as f:
    text = f.read().strip().split('\n')

# part 1
splitText = [t.split() for t in text]
numbers = [list(map(int, t)) for t in splitText[:-1]]
ops = splitText[-1]

answer = 0

for i in range(len(ops)):
    nums = []
    for n in numbers:
        nums.append(n[i])
    if ops[i] == '+':
        answer += sum(nums)
    else:
        answer += math.prod(nums)

print('Part 1:', answer)

# Part 2
answer = 0

while len(text[0]) != 0:
    op = text[-1][0]
    star = text[-1][1:].find('*')
    plus = text[-1][1:].find('+')

    end = -1
    if star != -1 and star < plus:
        end = star
    elif plus != -1:
        end = plus
    else:
        end = len(text[0])

    nums = []
    for i in range(end):
        char = []
        for n in text[:-1]:
            char.append(n[i])
        nums.append(int(''.join(char)))

    if op == '+':
        answer += sum(nums)
    else:
        answer += math.prod(nums)
    
    text = [t[end+1:] for t in text]

print('Part 2:', answer)