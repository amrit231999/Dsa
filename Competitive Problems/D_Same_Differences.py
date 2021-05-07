from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(len(v)):
        d[v[i]-i] += 1
    ans = 0
    for i in d:
        if d[i] > 1:
            ans += (d[i]*(d[i]-1))//2

    print(ans)
