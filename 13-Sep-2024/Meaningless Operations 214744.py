# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import math

def invertBits(n, length):     
    m = 1 << length
    m = m | m - 1
    n = n ^ m
    return n
    
for q in range(int(input())):
    a = int(input())
    max_gcd = -1
    x = int(math.log(a, 2))
    if invertBits(a, x) != 0:
        m = 1 << x
        m = m | m - 1
        print(m)
    else:
        d = 2
        while d*d <= a:
            if a % d == 0:
                break
            d += 1
        if a % d == 0:
            print(max(d, a//d))
        else:
            print(1)