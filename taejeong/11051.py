import sys

input = sys.stdin.readline

C = [[0 for _ in range(1001)] for _ in range(1001)]
for n in range(1, 1001):
    for k in range(n + 1):
        if k == 0:
            C[n][k] = 1
        elif k == 1:
            C[n][k] = n
        else:
            C[n][k] = C[n - 1][k - 1] + C[n - 1][k]

N, K = map(int, input().split())

print(C[N][K] % 10007)
