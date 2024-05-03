# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def dc(nums):
    global ctr
    if len(nums) == 1:
        return nums[0]
    middle = len(nums)//2
    l = dc(nums[:middle])
    r = dc(nums[middle:])
    if not l or not r or max(l,r) - min(l,r) > len(nums) - 1:
        ctr = -1
        return False
    if l > r:
        ctr += 1
    return min(l,r)


for t in range(int(input())):
    ctr = 0
    n = int(input())
    nums = list(map(int, input().split()))
    dc(nums)
    print(ctr)
