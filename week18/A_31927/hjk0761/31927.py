import sys

n = int(input())

a = list(map(int, sys.stdin.readline().strip().split()))

print(n//2)

for i in range(n//2):
    if i == 0:
        a[i] += 1000000
        a[n-1-i] -= 1000000
        print(*a)
        continue
    gap = min(a[i-1] - a[i], a[n-1-i] - a[n-i], 1000000)
    a[i] += gap
    a[n-1-i] -= gap
    print(*a)