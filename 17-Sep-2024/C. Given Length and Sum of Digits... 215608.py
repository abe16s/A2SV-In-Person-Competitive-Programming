# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())

if m*9 < s or (s==0 and m>1):
    print(-1,-1)
    exit()

maxi = ["0"] * m
cur = s
for i in range(m):
    if cur >= 9:
        maxi[i] = "9"
        cur -= 9
    else:
        maxi[i] = str(cur)
        break

mini = maxi[::-1]
for i in range(m):
    if mini[i] != "0" and mini[0] == "0":
        mini[0] = "1"
        mini[i] = str(int(mini[i])-1)
        break
print("".join(mini), "".join(maxi))