import sys

input = sys.stdin.readline

C = [0 for _ in range(11)]
for n in range(1, 11):
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    while len(stack) > 0:
        i = stack.pop()
        if i == n:
            C[n] += 1
            continue
        if i > n:
            continue
        stack.append(i + 1)
        stack.append(i + 2)
        stack.append(i + 3)

T = int(input())
for _ in range(T):
    print(C[int(input())])
