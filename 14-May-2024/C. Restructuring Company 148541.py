# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

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
        elif rank[parentX] < rank[parentY]:
            parent[parentX] = parentY
        else:
            parent[parentX] = parentY
            rank[parentY] += 1

n, q = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1] * (n+1)
type2={i:i+1 for i in range(1, n+1)}
for i in range(q):
    ty, x, y = map(int, input().split())
    if ty == 1:
        union(x, y)
    elif ty == 2:
        new_dep=type2[x]
        while new_dep <=y:
            union(new_dep,x)
            temp=type2[new_dep]
            type2[new_dep]=type2[y]
            new_dep=temp
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
