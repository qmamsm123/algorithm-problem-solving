import sys

input = sys.stdin.readline

N = int(input())
W = list(int(input()) for _ in range(N))
S = []
for i in range(N):
    candidate1 = S[i - 2] + W[i] if i >= 2 else W[i]
    candidate2 = S[i - 1] if i >= 1 else 0
    candidate3 = S[i - 3] + W[i - 1] + W[i] if i >= 3 else W[i - 1] + W[i] if i >= 1 else W[i]
    S.append(max(candidate1, candidate2, candidate3))
print(S[N - 1])