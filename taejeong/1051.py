N, M = [int(i) for i in input().split()]
lines = [input() for _ in range(N)]

max_size = 0
for i in range(N):
  for j in range(M):
    k = 0
    while True:
      if i + k >= N or j + k >= M:
        break
      if lines[i][j] == lines[i][j + k] and\
         lines[i][j + k] == lines[i + k][j + k] and\
         lines[i + k][j + k] == lines[i + k][j] and\
         pow(k + 1, 2) > max_size:
        max_size = pow(k + 1, 2)
      k += 1

print(max_size)