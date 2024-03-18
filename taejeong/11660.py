import sys

input = sys.stdin.readline


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i > 0:
            table[i][j] += table[i - 1][j]
        if j > 0:
            table[i][j] += table[i][j - 1]
        if i > 0 and j > 0:
            table[i][j] -= table[i - 1][j - 1]
for _ in range(M):
    x1, y1, x2, y2 = map(lambda i: i - 1, list(map(int, input().split())))
    ans = table[x2][y2]
    if x1 > 0:
        ans -= table[x1 - 1][y2]
    if y1 > 0:
        ans -= table[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        ans += table[x1 - 1][y1 - 1]
    print(ans)
