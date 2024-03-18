import sys

EPS = 1e-9
n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
else:
    suggestions = [int(sys.stdin.readline().strip()) for _ in range(n)]
    suggestions.sort()
    cuts = round(n * 0.15 + EPS)
    if cuts == 0:
        print(round(sum(suggestions)/n + EPS))
    else:
        print(round(sum(suggestions[cuts:-cuts])/(n - 2 * cuts) + EPS))
