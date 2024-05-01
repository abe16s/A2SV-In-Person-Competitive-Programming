# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for t in range(int(input())):
    num = int(input())
    bit = bin(num)[2:]
    n = len(bit)
    for i in range(n-1, -1, -1):
        if bit[i] == "1":
            break
    cout = ["0"] * n
    cout[(i)] = "1"
    flag = False
    if int("".join(cout), 2) ^ num:
        print(int("".join(cout), 2))
        continue
    for j in range(n-1, -1, -1):
        if j != i:
            if bit[j] == "1":
                cout[j] = "0"
            else:
                cout[j] = "1"
            flag = True
            break
    if flag:
        print(int("".join(cout), 2))
    else:
        print(int("1" + "".join(cout), 2))
