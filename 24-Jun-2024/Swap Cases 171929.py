# Problem: Swap Cases - https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    cout = ""
    for i in s:
        if i == i.lower():
            cout+=(i.upper())
        else:
            cout+=(i.lower())
    return cout

