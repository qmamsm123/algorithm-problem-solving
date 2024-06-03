N, M = [int(i) for i in input().split()]

campus = [input() for _ in range(N)]

next_to_visits = []
for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            next_to_visits.append([i, j])
            break
    if len(next_to_visits) != 0:
        break

meets = 0
already_visited = {}
while len(next_to_visits):
    r, c = next_to_visits.pop()
    if campus[r][c] == "X":
        continue
    if campus[r][c] == "P":
        meets += 1
    for v, h in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_r = r + v
        next_c = c + h
        if next_r < 0 or next_r >= N:
            continue
        if next_c < 0 or next_c >= M:
            continue
        if already_visited.get((next_r, next_c)) == None:
            already_visited[(next_r, next_c)] = True
            next_to_visits.append([next_r, next_c])

if meets > 0:
    print(meets)
else:
    print("TT")
