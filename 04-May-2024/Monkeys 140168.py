# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parentX = find(x)
    parentY = find(y)
    if parentX != parentY:
        if rank[parentX] > rank[parentY]:
            parent[parentY] = parentX
            p,c = parentX, parentY
        elif rank[parentX] < rank[parentY]:
            parent[parentX] = parentY
            p,c = parentY, parentX
        else:
            parent[parentX] = parentY
            rank[parentY] += 1
            p,c = parentY, parentX
        children[p] |= children[c]


n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1] * (n+1)
children = {i: {i} for i in range(1,n+1)}
graph = {}
for i in range(n):
    graph[i+1] = list(map(int, input().split()))
    
removed = []
for i in range(m):
    a, b = map(int, input().split())
    removed.append([a,graph[a][b-1]])
    graph[a][b-1] = -1

for v in graph:
    l, r = graph[v]
    if l != -1:
        union(l, v)
    if r != -1:
        union(r, v)

falling = [-1] * n
# for i in range(n):
#     if find(i+1) != find(1):
#         falling[i] = len(removed)-1

for i in range(len(removed)-1, -1,-1):
    a, b = removed[i]
    # print(a,b, falling)
    if find(a) != find(1) and find(b) == find(1):
        for j in children[find(a)]:
            if find(j) == find(a):
                falling[j-1] = i
    if find(b) != find(1) and find(a) == find(1):
        for j in children[find(b)]:
            if find(j) == find(b):
                falling[j-1] = i
    union(a,b)


for f in falling:
    print(f)