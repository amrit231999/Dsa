from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):

    n, l, r = map(int, input().split())

    v = list(map(int, input().split()))
    d = defaultdict(list)
    for i in range(len(v)):
        if i < l:
            d[v[i]].append('l')

        else:
            d[v[i]].append('r')

    cntl = 0
    cntr = 0
    ans = 0
    for i in d:
        x = d[i].count('l')
        y = d[i].count('r')

        if x > y:
            d[i] = ['l']*(x-y)
            cntl += x-y
        elif y > x:
            d[i] = ['r']*(y-x)
            cntr += y-x
        else:
            d[i] = [0]

    freq = []
    ans += min(cntl, cntr)
    # print("ans is :",ans)
    if(cntl == cntr):
        print(cntl)
        continue
    for i in d:
        if cntl < cntr:
            z = d[i].count('r')
            freq.append(z)

        elif cntr < cntl:
            z = d[i].count('l')
            freq.append(z)

    freq.sort()
    # print(freq)
    cur = 0
    i = 0
    ind = 0
    while cur < min(cntl, cntr) and i < len(freq):

        if cur+1 < min(cntl, cntr) and freq[i] % 2:

            cur += 1
            freq[i] -= 1

        elif cur+1 == min(cntl, cntr) and freq[i] % 2:
            freq[i] -= 1
            cur += 1
            break

        i += 1

    freq.sort(reverse=True)
    i = 0
    while cur < min(cntl, cntr) and i < len(freq):

        if cur+freq[i] < min(cntl, cntr):

            cur += freq[i]
            freq[i] = 0
            i += 1

        elif cur+freq[i] >= min(cntl, cntr):
            freq[i] -= min(cntl, cntr)-cur
            break
    cnt_final = 0
    for i in range(0, len(freq)):
        ans += freq[i]//2
        if freq[i] % 2:
            cnt_final += 1

    ans += cnt_final

    print(ans)
