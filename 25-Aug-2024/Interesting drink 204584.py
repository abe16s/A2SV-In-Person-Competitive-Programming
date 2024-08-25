# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

n = int(input())
nums = sorted(list(map(int, input().split())))
for q in range(int(input())):
    m = int(input())
    l = 0
    r = n-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] > m:
            r = mid - 1
        else:
            l = mid+1

    print(l)