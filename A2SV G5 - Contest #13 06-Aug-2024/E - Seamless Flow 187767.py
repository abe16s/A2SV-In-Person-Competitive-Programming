# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import deque, defaultdict
for t in range(int(input())):
    n, m = map(int, input().split())
    directed = []
    undirected = []
    indegree = defaultdict(int)
    nbrs = defaultdict(list)
    for i in range(m):
        t, a, b = map(int, input().split())
        if t:
            directed.append((a,b))
            indegree[b] += 1
            nbrs[a].append(b)
        else:
            undirected.append((a,b))
    
    topsort = []
    queue = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        for i in range(len(queue)):
            cur = queue.popleft()
            topsort.append(cur)
            for nbr in nbrs[cur]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
    
    if len(topsort) != n:
        print("NO")
        continue

    idxs = [0] * (n+1)
    for t in range(len(topsort)):
        idxs[topsort[t]] = t 

    for undi in undirected:
        a, b = undi
        if idxs[a] < idxs[b]:
            directed.append((a,b))
        else:
            directed.append((b,a))

    print("YES")
    for edge in directed:
        a, b = edge
        print(a,b) 
