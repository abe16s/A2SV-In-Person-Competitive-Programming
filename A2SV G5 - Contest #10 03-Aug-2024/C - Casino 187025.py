# Problem: C - Casino - https://codeforces.com/gym/514644/problem/C

n = int(input())
nums = list(map(int, input().split()))
lcm = nums[0]
for i in range(n):
    while nums[i] % 2 == 0:
        nums[i] //= 2

    while nums[i] % 3 == 0:
        nums[i] //= 3
    
if nums.count(nums[0]) != n:
    print("No")
else:
    print("Yes")