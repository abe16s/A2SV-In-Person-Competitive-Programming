# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

for t in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    for i in range(30, -1, -1):
        unset = 0
        for j in range(n):
            if (nums[j] & (1<<i)) == 0:
                unset += 1
        if unset <= k:
            k -= unset
            ans |= (1<<i)
    print(ans)
