# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = list(map(int, input().split()))
players = [int(input()) for _ in range(m+1)]
friends = 0
for i in range(m):
    diff = (players[-1] ^ players[i]).bit_count()
    if diff <= k:
        friends += 1
print(friends)