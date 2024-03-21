import sys

# 입력 받기
n, m = [int(i) for i in sys.stdin.readline().strip().split()]
grid = [[int(i) - 2 for i in sys.stdin.readline().strip().split()]
        for _ in range(n)]

# 목표 지점의 좌표얻기
goal = [-1, -1]
for i in range(n):
    for j in range(m):
        if (grid[i][j] == 0):
            goal = [i, j]


def isValid(i, j):
    # 인접 셀이 유효한 범위인지 확인
    if i < 0 or j < 0:
        return False
    if i >= n or j >= m:
        return False
    if grid[i][j] == -2:
        return False
    return True


queue = [[goal[0], goal[1], 0]]
for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if isValid(goal[0] + di, goal[1] + dj):
        queue.insert(0, [goal[0] + di, goal[1] + dj, 1])
while (len(queue) > 0):
    i, j, distance = queue.pop()
    if grid[i][j] == -1 or distance < grid[i][j]:
        grid[i][j] = distance
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if isValid(i + di, j + dj):
                queue.insert(0, [i + di, j + dj, distance + 1])

for line in grid:
    for cell in line:
        print(cell if cell >= 0 else 0 if cell == -2 else -1, end=" ")
    print()
