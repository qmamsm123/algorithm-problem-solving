import sys

input = sys.stdin.readline

N = int(input())
Triangle = []
for _ in range(N):
    Triangle.append(list(map(int, input().split())))

for i in range(1, len(Triangle)):
    length = len(Triangle[i])
    for j in range(length):
        if j == 0:
            Triangle[i][j] += Triangle[i - 1][j]
        elif j == length - 1:
            Triangle[i][j] += Triangle[i - 1][j - 1]
        else:
            Triangle[i][j] += max(Triangle[i - 1][j - 1], Triangle[i - 1][j])

print(max(Triangle[-1]))
