from collections import defaultdict
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    v = [[0]*n for i in range(n)]
    startx = 0
    starty = 0
    orgx = 0
    orgy = 0
    cur = 1
    cnt = 0
    flag = 0
    for k in range(2*n-1):
        while startx < n and starty < n:
            v[startx][starty] = cur
            cur += 1
            startx += 1
            starty += 1
        cnt += 1
        if cnt % 2:
            startx = orgx+(cnt+1)//2
            starty = 0
        else:
            startx = 0
            starty = orgy+cnt//2

    for i in range(n):
        for j in range(n):
            if i > 0 and abs(v[i][j] - v[i-1][j]) == 1:
                flag = 1
            elif j > 0 and abs(v[i][j] - v[i][j-1]) == 1:
                flag = 1
            elif i+1 < n and abs(v[i][j] - v[i+1][j]) == 1:
                flag = 1
            elif j+1 < n and abs(v[i][j] - v[i][j+1]) == 1:
                flag = 1

    if flag > 0:
        print(-1)
        continue
    for i in range(n):
        for j in range(n):
            print(v[i][j], end=" ")

        print("")
