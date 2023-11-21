import sys
import math

input = sys.stdin.readline

N = int(input())
S = [i for i in range(N + 1)]
for i in range(1, N + 1):
    root = int(math.sqrt(i))
    if i == root ** 2:
        S[i] = 1
        continue
    for j in range(1, root + 1):
        S[i] = min(S[i], 1 + S[i - j ** 2])
print(S[N])