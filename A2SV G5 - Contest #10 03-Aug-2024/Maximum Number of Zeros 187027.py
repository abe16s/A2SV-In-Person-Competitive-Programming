# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

from collections import defaultdict
import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = defaultdict(int)

zeros = 0
maxi = 0 
for i in range(n):
    if a[i] == 0 and b[i] == 0:
        zeros += 1
    elif a[i]:
        g = math.gcd(a[i],-b[i])
        if (a[i] >= 0 and -b[i] >= 0) or (a[i]<0 and -b[i]<0):
            x = f"{abs(b[i]//g)}/{abs(a[i]//g)}"
        else:
            be = -b[i]
            if be > 0:
                be = b[i]
            x = f"{(be//g)}/{abs(a[i]//g)}"
        d[x] += 1
        maxi = max(maxi, d[x])

print(maxi + zeros)