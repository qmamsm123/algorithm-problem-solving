import sys

input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
S = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    S[i] = P[i]
    for j in range(1, i // 2 + 1):
        S[i] = max(S[i], S[j] + S[i - j])
print(S[N])
