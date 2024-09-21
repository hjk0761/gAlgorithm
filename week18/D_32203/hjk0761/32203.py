import sys

n, m = map(int, input().split())

parent = [i for i in range(n)]

group = [[0, 0] for _ in range(n)]

c = list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in range(n):
    if c[i] % 2 == 0:
        group[i][0] +=1
    else:
        group[i][1] += 1

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global result
    x = find(x)
    y = find(y)
    if x == y:
        return
    for i in range(2):
        result += group[x][i] * group[y][(i+1)%2]
    if x < y:
        parent[y] = x
        for i in range(2):
            group[x][i] += group[y][i]
    else:
        parent[x] = y
        for i in range(2):
            group[y][i] += group[x][i]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    union(a-1, b-1)
    print(result)