from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    v = list(map(str, input().strip()))
    d = defaultdict(int)
    flag = 0
    for i in range(len(v)):
        if d[v[i]] > 0 and i > 0 and v[i-1] != v[i]:
            flag = 1
        d[v[i]] += 1

    print(["YES", "NO"][flag])
