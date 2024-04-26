# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

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
            p, c = parentX, parentY
        elif rank[parentX] < rank[parentY]:
            parent[parentX] = parentY
            p, c = parentY, parentX
        else:
            parent[parentX] = parentY
            rank[parentY] += 1
            p, c = parentY, parentX
        family[p][0] = min(family[p][0], family[c][0])
        family[p][1] = max(family[p][1], family[c][1])
        family[p][2] += family[c][2]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
rank = [1] * (n+1)
family = [[i, i, 1] for i in range(n+1)]

for q in range(m):
    q = input().split()
    if q[0] == "union":
        union(int(q[1]), int(q[2])) 
    else:
        cur = find(int(q[1]))
        print(*family[cur])