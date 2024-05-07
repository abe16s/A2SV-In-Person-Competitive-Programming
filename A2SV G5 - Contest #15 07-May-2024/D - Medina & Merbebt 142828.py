# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    prefix = [[0]*31]
    for num in nums:
        cur = prefix[-1][::]
        for i in range(30,-1,-1):
            if (num & (1<<i)) != 0:
                cur[31-i-1] += 1
        prefix.append(cur)
    q = int(input())
    for j in range(q):
        l, k = map(int, input().split())
        left = l
        right = n
        while left <= right:
            mid = left + (right-left)//2
            cur = 0
            for i in range(31):
                if (prefix[mid][i] - prefix[l-1][i]) == (mid-l+1):
                    cur |= (1<<(31-i-1))
            if cur >= k:
                left = mid+1
            else:
                right = mid-1
        if left-1 < l:
            print(-1, end=" ")
        else:
            print(left-1, end=" ")
    print()

