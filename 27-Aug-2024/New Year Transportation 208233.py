# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
a = list(map(int, input().split()))
cur = 0

while cur <= t-1:
    cur += a[cur]
    if cur == t-1:
        print("YES")
        break
else:
    print("NO")