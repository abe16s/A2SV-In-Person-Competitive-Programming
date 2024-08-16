# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

from collections import defaultdict
if __name__ == '__main__':
    students = defaultdict(list)
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[score].append(name)            
        
    k = sorted(students.keys())
    students[k[1]].sort()
    for s in students[k[1]]:
        print(s)