import sys

input = sys.stdin.readline

W = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            if a < b and b < c:
                W[a][b][c] = W[a][b][c - 1] + \
                    W[a][b - 1][c - 1] - W[a][b - 1][c]
            else:
                W[a][b][c] = W[a - 1][b][c] + W[a - 1][b - 1][c] + \
                    W[a - 1][b][c - 1] - W[a-1][b - 1][c-1]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return W[20][20][20]
    return W[a][b][c]


while True:
    A, B, C = map(int, input().split())
    if A == -1 and B == -1 and C == -1:
        break
    print(f"w({A}, {B}, {C}) = {w(A,B,C)}")
