# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import defaultdict
n = int(input())
s = input()
flats = float("inf")
pokemons = set(s)
cur = defaultdict(int)
l = 0
for r in range(n):
    cur[s[r]] += 1
    while len(cur) == len(pokemons):
        flats = min(flats, r-l+1)     
        if cur[s[l]] > 1:
            cur[s[l]] -= 1
            l += 1
        else:
            break
print(flats)