N = int(input())
SIZES = [int(i) for i in input().split()]
T, P = [int(i) for i in input().split()]

shirts = 0
for size in SIZES:
    shirts += size // T + int(size % T != 0)
print(shirts)

print(f"{N // P} {N % P}")
