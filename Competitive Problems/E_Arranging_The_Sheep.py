from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    v = list(map(str, input().strip()))
    if v.count('*') == 0 or v.count('.') == 0:
        print(0)
        continue
    start = 0
    end = len(v)-1
    while v[start] != '*':
        start += 1
    while v[end] != '*':
        end -= 1
