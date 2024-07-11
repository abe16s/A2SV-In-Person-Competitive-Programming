# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
mini = float("inf")
maxi = -1
recipes = []
for i in range(n):
    l, r = map(int, input().split())
    mini = min(mini, l)
    maxi = max(maxi, r)
    recipes.append([l,r])

temp_prefix = [0] * (maxi-mini+2)
for i in range(n):
    temp_prefix[recipes[i][0]-mini] += 1
    temp_prefix[recipes[i][1]+1-mini] -= 1

admissible = [0]
if temp_prefix[0] >= k:
    admissible.append(admissible[-1]+1) 
else:
    admissible.append(admissible[-1])

for i in range(1,len(temp_prefix)):
    temp_prefix[i] += temp_prefix[i-1]
    if temp_prefix[i] >= k:
        admissible.append(admissible[-1]+1) 
    else:
        admissible.append(admissible[-1])
    

# print(temp_prefix)
for l in range(q):
    a, b = map(int, input().split())
    # print(a,b)
    if a < mini:
         a = admissible[0]
    elif a > maxi:
        a = admissible[-1]
    else:
        a = admissible[a-mini]

    if b < mini:
        b = admissible[0]
    elif b > maxi:
        b = admissible[-1]
    else:
         b = admissible[b-mini+1]

    # print(a,b)
    print(b-a)
    
