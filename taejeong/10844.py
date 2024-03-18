import sys

input = sys.stdin.readline

N = int(input())
S = [[0] + [1 for _ in range(1, 10)]]
for i in range(1, N):
    P = [0 for _ in range(10)]
    for j in range(10):
        P[j] = S[i - 1][j - 1] + S[i - 1][j + 1] if j != 0 and j != 9\
            else S[i - 1][j + 1] if j == 0\
            else S[i - 1][j - 1]
    S.append(P)

print(sum(S[N - 1]) % 1_000_000_000)
