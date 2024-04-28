# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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


n, m, k = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [1] * (n+1)
edges = [input() for _ in range(m)]
queries = [input().split() for _ in range(k)]

answer = []
for q in range(k-1, -1, -1):
    q = queries[q]
    if q[0] == "ask":
        if find(int(q[1])) == find(int(q[2])):
            answer.append("YES")
        else:
            answer.append("NO")
    else:
        union(int(q[1]), int(q[2]))

for _ in range(len(answer)-1, -1,-1):
    print(answer[_])